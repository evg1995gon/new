from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('text', 'group',)

    def clean_text(self):
        data = self.cleaned_data['text']
        if str(data) == 0:
            raise ValidationError('Это поле обязательно к заполнению')
        return data

