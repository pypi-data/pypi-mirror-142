from django.forms import ModelForm,Textarea,EmailInput,URLInput,ValidationError
from django.utils.translation import gettext as _
from .models import Comment
import mistune

class CommentForm(ModelForm):
    class Meta:
        model  = Comment
        fields = ('nickname','email','website','content')
        labels = {
            'nickname': _('昵称'),
            'content': _('内容'),
            'email': _('邮箱'),
            'website' : _('网站'),
        }
        widgets = {
            'nickname' :Textarea(attrs = {'class': 'form-control', 'style': "width: 60%;"}),
            'content' : Textarea(attrs = {'rows' : 6, 'cols' : 60}),
            'email' : EmailInput(attrs = {'class': 'form-control', 'style': "width: 60%;"}),
            'website' : URLInput(attrs = {'class': 'form-control', 'style' : "width: 60%"})
        }
        max_length = {
            'nickname' : 50,
            'email' : 50,
            'website': 100,
            'content': 500,

        }
    def clean_content(self):
        content = self.cleaned_data.get('content')

        if len(content) < 10:
            raise ValidationError('内容太短了')
        content = mistune.markdown(content)
        return content

