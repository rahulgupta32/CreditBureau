from django import forms
from scoring.models import Question, UserResponse

class UserResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['answer']
