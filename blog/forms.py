from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    
    class Meta:
        
        model = Post
        fields = ['title', 'slug', 'introtext', 'fulltext']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'introtext': forms.Textarea(attrs={'class': 'form-control'}),
            'fulltext': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        slug = self.cleaned_data['slug'].lower()
        if slug == 'create':
            raise ValidationError('Неверное название url!')
        if Post.objects.filter(slug__iexact=slug).count():
            raise ValidationError('Такой url уже есть!')
        return slug
    