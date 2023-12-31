from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

properties_operations = [
    path('', views.PropertyDetailsView.as_view(), name='property_details'),
    path('update/', views.PropertyUpdateView.as_view(), name='property_update'),
    path('delete/', views.PropertyDeleteView.as_view(), name='property_delete')
]

payment_processes = [
    path('<int:property_id>', views.product_page, name='payment'),
    path('successful/<int:property_id>/', views.payment_successful, name='payment_successful'),
    path('cancelled/', views.payment_cancelled, name='payment_cancelled'),
]

urlpatterns = [
    path('list-properties/', views.PropertyListView.as_view(), name='property_list'),
    path('create-properties/', views.PropertyCreateView.as_view(), name='property_create'),
    path('get_additional_form_fields/', views.get_additional_form_fields, name='additional_form_fields'),
    path('save-property/<int:pk>/', views.SavePropertyView.as_view(), name='save_property'),
    path('unsave-property/<int:pk>/', views.UnsavePropertyView.as_view(), name='unsave_property'),
    path('estimate-calculator/', views.EstimatePropertyView.as_view(), name='estimate'),
    path('estimated-result/', views.EstimatePropertyResultView.as_view(), name='estimated_result'),
    path('payment/', include(payment_processes)),
    path('property/<int:pk>/', include(properties_operations))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)