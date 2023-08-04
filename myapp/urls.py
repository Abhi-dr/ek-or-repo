from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    # path("signup", views.signup, name="signup"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("invalid", views.invalid, name="invalid"),
    path("notes", views.notes, name="notes"),
    
    path("edit_note/<int:id>", views.edit_note, name="edit_note"),
    path("delete_note/<int:id>", views.delete_note, name="delete_note"),
        
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = "myapp.views.page_not_found_view"