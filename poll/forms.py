from dataclasses import fields
import imp
from django import forms
from django.forms import ModelForm
from .models import *

class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question','option_one','option_two','option_three']