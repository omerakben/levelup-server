"""levelup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from levelupapi.views import EventView, GameTypeView, GameView
from levelupapi.views.auth import check_user, register_user  # Import auth views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"gametypes", GameTypeView, "gametype")
router.register(r"games", GameView, "game")
router.register(r"events", EventView, "event")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("checkuser", check_user, name="check_user"),  # Add check_user path
    path("register", register_user, name="register_user"),  # Add register_user path
    path("", include(router.urls)),
]
