from django.db.models import Q
from django import forms
from property_rental_marketplace.profile_management.models import (
    ContactMessage,
    NewsletterFollower,
    AdminNewsLetterPost,
)
from property_rental_marketplace.user_authentication.models import UserProfile


class UserProfileBaseForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)


class UserProfileUpdateForm(UserProfileBaseForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["id"] = field_name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        current_user_email = self.instance.user.email

        if (
            email != current_user_email
            and UserProfile.objects.filter(
                ~Q(user=self.instance.user), email=email
            ).exists()
        ):
            raise forms.ValidationError("This email is already in use.")

        return email

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name:
            if len(first_name) < 2:
                self.add_error(
                    "first_name", "First name should be at least 2 characters long."
                )
            elif any(char.isdigit() for char in first_name):
                self.add_error("first_name", "First name cannot contain digits.")
            elif first_name[0].islower():
                self.add_error(
                    "first_name", "First name should start with an uppercase letter."
                )

        if last_name:
            if len(last_name) < 2:
                self.add_error(
                    "last_name", "Last name should be at least 2 characters long."
                )
            elif any(char.isdigit() for char in last_name):
                self.add_error("last_name", "Last name cannot contain digits.")
            elif last_name[0].islower():
                self.add_error(
                    "last_name", "Last name should start with an uppercase letter."
                )

        return cleaned_data


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }


class NewsLetterSubscriberForm(forms.ModelForm):
    class Meta:
        model = NewsletterFollower
        exclude = ("email",)


class AdminNewsLetterPostForm(forms.ModelForm):
    class Meta:
        model = AdminNewsLetterPost
        fields = "__all__"

        widgets = {
            "newsletter_type": forms.TextInput(
                attrs={"placeholder": "Type newsletter"}
            ),
            "content": forms.Textarea(attrs={"placeholder": "Title news content"}),
            "url_redirect": forms.TextInput(attrs={"placeholder": "Url to redirect"}),
        }
