from django.urls import path, include
from django.contrib.auth import views as auth_views
from property_rental_marketplace.property_market.views import PropertyListView
from . import views

profile_denpendencies = [
    path('details/', views.UserProfileView.as_view(), name='profile_details'),
    path('update/', views.UserProfileUpdateView.as_view(), name='update_profile'),
    path('delete/', views.UserProfileDeleteView.as_view(), name='delete_profile'),
    path(
        'reset-password/', 
        auth_views.PasswordResetView.as_view(template_name="passwords/password_reset.html"), 
        name='reset_password'
    ),
    path(
        'reset-password-sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="passwords/password_reset_sent.html"), 
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="passwords/password_reset_form.html"), 
        name='password_reset_confirm'
    ),
    path(
        'reset-password-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="passwords/password_reset_done.html"), 
        name='password_reset_complete'
    ),
]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('properties/list_properties/<str:property_type>/', PropertyListView.as_view(), name='list_properties'),
    path('saved-properties/', views.SavedPropertiesCollectionView.as_view(), name='saved_properties_collection'),
    path('profile/', include(profile_denpendencies)),
]