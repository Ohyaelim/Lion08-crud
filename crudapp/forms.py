from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Blog

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'pub_date']
        widgets ={
            'pub_date' : forms.DateInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'date'
                }
            )
        }