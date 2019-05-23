from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import *

class CarrierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CarrierForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if self.fields[field].widget.__class__.__name__ in ('TextInput' , 'Textarea' , 'NumberInput' , 'Select'):
                self.fields[field].widget.attrs.update({ 'class': 'form-control' })
            else:
                self.fields[field].widget.attrs.update({ 'id': 'imageUpload' })
    class Meta:
        model = Carrier
        fields = '__all__'
