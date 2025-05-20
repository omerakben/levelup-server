"""View module for handling requests about games"""

from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from levelupapi.models import Game, Gamer, GameType


class GameView(ViewSet):
    """Level up games view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()
        game_type_query = request.query_params.get("type", None)
        if game_type_query is not None:
            games = games.filter(game_type_id=game_type_query)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""

    class Meta:
        model = Game
        fields = (
            "id",
            "title",
            "maker",
            "game_type",
            "number_of_players",
            "skill_level",
            "gamer",
        )
        depth = 1
