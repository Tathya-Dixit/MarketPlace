from django import forms

from .models import Item

tailclasses = 'rounded-lg bg-gray-200 pl-3'

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image',)
        
        widgets = {
            'category' : forms.Select(attrs={
                'class' : tailclasses
            }),
            'name' : forms.TextInput(attrs={
                'class' : tailclasses
            }),
            'description' : forms.Textarea(attrs={
                'class' : tailclasses
            }),
            'price' : forms.TextInput(attrs={
                'class' : tailclasses
            }),
            'image' : forms.FileInput(attrs={
                'class' : tailclasses+ " py-2 text-sm"
            }),
            
        }