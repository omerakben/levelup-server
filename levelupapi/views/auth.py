from django.contrib.auth.models import (
    User,
)  # Import User model if you are linking Gamer to Django's User
from levelupapi.models import Gamer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def check_user(request):
    """Checks to see if User has Associated Gamer

    Method arguments:
      request -- The full HTTP request object
    """
    uid = request.data.get("uid")

    # Use the built-in User model lookup if using Django's auth
    # Or use your custom Gamer model lookup if not using Django's User for Firebase UID
    try:
        # Assuming your Gamer model has a 'uid' field for Firebase UID
        gamer = Gamer.objects.get(uid=uid)
        # If you are linking Gamer to Django's User model and UID is on User:
        # user = User.objects.get(username=uid) # Or however you store Firebase UID
        # gamer = Gamer.objects.get(user=user)

        return Response(
            {
                "id": gamer.id,
                "uid": gamer.uid,
                "bio": gamer.bio,
                # Add any other gamer fields you want to return
                "valid": True,  # Indicates an existing user
            }
        )
    except Gamer.DoesNotExist:
        # If Gamer does not exist, this is a new user or a user that needs to register their Gamer profile
        return Response(
            {"valid": False}, status=404
        )  # Or status=200 and let client handle 'valid: false'
    except Exception as e:
        return Response({"message": str(e)}, status=500)


@api_view(["POST"])
def register_user(request):
    """Handles the creation of a new gamer for an authenticated user

    Method arguments:
      request -- The full HTTP request object
    """

    # This assumes that your client sends all necessary Gamer info
    # including the uid from Firebase.
    # If you are linking to Django's User model, you might create/get the User first.

    # Example: Create a new Gamer instance
    # You might need to get or create a Django User first if Gamer is linked via ForeignKey
    # For simplicity, this example assumes Gamer directly stores UID and other info.

    uid = request.data.get("uid")
    bio = request.data.get("bio")
    # Potentially first_name, last_name if your Gamer model has them
    # and if they are being sent from the client.
    # The `RegisterForm.js` currently only sends `bio` and `uid`.

    try:
        # Check if a Gamer with this UID already exists to prevent duplicates
        if Gamer.objects.filter(uid=uid).exists():
            gamer = Gamer.objects.get(
                uid=uid
            )  # Or update existing one if that's the desired logic
            gamer.bio = bio  # Example: updating bio if user re-registers
            gamer.save()
            return Response(
                {
                    "id": gamer.id,
                    "uid": gamer.uid,
                    "bio": gamer.bio,
                    "message": "User already registered. Profile updated if necessary.",
                },
                status=200,
            )  # Or 409 Conflict if re-registration isn't allowed/handled this way

        gamer = Gamer.objects.create(
            uid=uid,
            bio=bio,
            # Add other fields as necessary based on your Gamer model
        )

        return Response(
            {
                "id": gamer.id,
                "uid": gamer.uid,
                "bio": gamer.bio,
                # Add any other gamer fields you want to return
            },
            status=201,
        )
    except Exception as e:
        return Response({"message": str(e)}, status=500)
