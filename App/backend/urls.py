from django.contrib import admin
from django.urls import path
from users import views as user_views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from systemFord import views as ford_views
from fleetCommand import views as fleetcommand_views
from fleetLocation import views as fleetlocation_views
from veh import views as vehicle_views
from carrental import views as rent_views
from notification import views as notification_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('getuserinfo/', user_views.GetUserInfo.as_view()),
    path('create/', user_views.CustomUserCreate.as_view(), name="create_user"),
    path('getvehicles/', ford_views.SystemFord.as_view()),
    path('fleetcommand/', fleetcommand_views.FleetCommand.as_view()),
    path('carlist/', vehicle_views.CarsList.as_view()),
    path('fleetlocation/', fleetlocation_views.CarLocation.as_view()),
    path('rent/', rent_views.Rental.as_view()),
    path('notifcations/', notification_views.Notification.as_view())
]
