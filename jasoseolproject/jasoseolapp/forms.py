from django import forms
from .models import Jasoseol, Comment

class JasoseolForm(forms.ModelForm):
    
    # 메타 클래스란 클래스 안에 선언해서 상위의 클래스에게 메타데이터, 즉 옵션이나 데이터를 추가해줄 수 있는 것
    class Meta:
        model = Jasoseol
        fields = ('title', 'body')

    def __init__(self, *args, **kwargs):
        # super() => 자식 클래스(JasosoelForm)에서 부모 클래스(ModelForm)의 내용을 사용하고 싶을 때 사용
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update(
            {'placeholder': "자기소개서를 입력하세요",
             'class': 'jss_content'})


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body','post',)

