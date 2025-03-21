from django.urls import path
from . import views, admin
from .views import Publie_Annonce ,mes_annonces,suprimer_Annonce,signup_view, login_view, logout_view,list_annonces,admin_annonces,change_status ,modifier_annonce ,admin_dashboard

urlpatterns = [
    path("annonces/", views.list_annonces, name="list_annonces"),
    path("Publie_Annonce/", Publie_Annonce, name="Publie_Annonce"),
    path("Mes_Annonces/", mes_annonces, name="mes_annonces"),
    path("suprimer_Annonce/<int:annonce_id>/", suprimer_Annonce, name="suprimer_Annonce"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("admin_annonces/", admin_annonces, name="admin_annonces"),
    path("change-status/<int:annonce_id>/<str:status>/", change_status, name="change_status"),
    path("modifier_annonce/<int:annonce_id>/", modifier_annonce, name="modifier_annonce"),
path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
]

