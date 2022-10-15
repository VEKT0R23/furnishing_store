from django import forms
# from .models import Gallery
from .models import Feedback, ShopGallery


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'phone_number': 'Номер телефона',
            'feedback': 'Адрес и предпочтительное время замера',
        }
