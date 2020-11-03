from django import forms
from django.contrib.auth.models import User
from testapp.models import monday_model1,column_model1
class signup_forms(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']

class mondayupdate_forms(forms.ModelForm):
    class Meta:
        model=monday_model1
        fields='__all__'

class columninsert_forms(forms.ModelForm):
    class Meta:
        model=column_model1
        fields='__all__'
