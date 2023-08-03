from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from property_rental_marketplace.property_market.models import BaseProperty, AdditionalField, Apartment \
    ,Villa, Shop, Building, Office
from property_rental_marketplace.profile_management.views import UserProfileMixin
from property_rental_marketplace.property_market.forms import BasePropertyForm, ApartmentForm \
    ,VillaForm, OfficeForm, ShopForm, BuildingForm

PROPERTY_TYPE_MAPPING = {
    'Apartment': {
        'model': Apartment,
        'form': ApartmentForm,
    },
    'Villa': {
        'model': Villa,
        'form': VillaForm,
    },
    'Office': {
        'model': Office,
        'form': OfficeForm,
    },
    'Shop': {
        'model': Shop,
        'form': ShopForm,
    },
    'Building': {
        'model': Building,
        'form': BuildingForm,
    },
}

class PropertyListView(UserProfileMixin, views.ListView):
    model = BaseProperty
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset().select_related(
            'apartment', 'villa', 'office', 'shop', 'building'
        )
        
        search_by_title = self.request.GET.get('search_by_title', '')
        search_by_property_type = self.request.GET.get('property_type', '')
        search_by_location = self.request.GET.get('location', '')

        if search_by_title:
            queryset = queryset.filter(title__icontains=search_by_title)

        if search_by_property_type:
            queryset = queryset.filter(property_type__icontains=search_by_property_type)

        if search_by_location:
            queryset = queryset.filter(location__icontains=search_by_location)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_by_title'] = self.request.GET.get('search_by_title', '')
        context['search_by_property_type'] = self.request.GET.get('property_type', '')
        context['search_by_location'] = self.request.GET.get('location', '')
        context['property_types'] = BaseProperty.TYPE_CHOICES
        context['user_profile'] = self.get_user_profile()

        return context
    
class PropertyCreateView(UserProfileMixin, views.CreateView):
    model = BaseProperty
    form_class = BasePropertyForm
    template_name = 'properties/property_create.html'
    success_url = reverse_lazy('property_list')

    def form_valid(self, form):
        property_type = form.cleaned_data['property_type']
        form.instance.owner = self.request.user

        specific_property_info = PROPERTY_TYPE_MAPPING.get(property_type)

        if specific_property_info:
            specific_property_form = specific_property_info['form']

            specific_form = specific_property_form(self.request.POST)
            if specific_form.is_valid():
                base_property = form.save(commit=False)
                base_property.property_type = property_type
                base_property.save()

                specific_property = specific_form.save(commit=False)
                specific_property.property = base_property  
                specific_property.save()

                return super().form_valid(form)
            
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.get_user_profile()
        return context

def get_additional_form_fields(request):
    property_type = request.GET.get('property_type')
    form_classes = {
        'Apartment': ApartmentForm,
        'Villa': VillaForm,
        'Office': OfficeForm,
        'Shop': ShopForm,
        'Building': BuildingForm,
    }

    form_class = form_classes.get(property_type)
    if form_class:
        form = form_class()
        html = ''
        for field in form:
            html += str(field)
    else:
        html = ''

    return JsonResponse({'html': html})

class PropertyDetailsView(UserProfileMixin, views.DetailView):
    model = BaseProperty
    template_name = 'properties/property_details.html'
    context_object_name = 'property'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.get_user_profile()
        context['owner_first_name'] = self.object.owner.userprofile.first_name
        context['owner_last_name'] = self.object.owner.userprofile.last_name
        context['owner_phone'] = self.object.owner.userprofile.phone  
        context['owner_email'] = self.object.owner.userprofile.email 
        return context


class PropertyUpdateView(UserProfileMixin, views.UpdateView):
    model = BaseProperty
    form_class = BasePropertyForm
    template_name = 'properties/property_update.html'

    def get_success_url(self):
        return reverse('property_details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.object.pk
        context['user_profile'] = self.get_user_profile()
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Property updated successfully.')
        return super().form_valid(form)

class PropertyDeleteView(views.DeleteView):
    model = BaseProperty
    template_name = 'properties/property_delete.html'
    success_url = reverse_lazy('property_list')

    def form_valid(self, form):
        messages.success(self.request, 'Property successfully deleted.')
        return super().form_valid(form)