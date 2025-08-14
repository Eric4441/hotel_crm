from django import forms
from .models import *

class RoomForm(forms.ModelForm):
    class Meta:
        model = rooms
        fields = "__all__"

class DealForm(forms.ModelForm):
    class Meta:
        model = deal
        fields = "__all__"

class Employee(forms.ModelForm):
    class Meta:
        model = employee
        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = users
        fields = "__all__"



