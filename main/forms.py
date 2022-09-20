from .models import BlogPost, MyUser
from django.forms import ModelForm, TextInput, DateInput, EmailInput, Textarea, PasswordInput


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'message', 'email', 'date']
        widgets = {
            "title": TextInput(attrs={
                'class': 'blog_input',
                'placeholder': 'Заголовок',
                'name': 'subject',
                'type': 'text'
            }),
            "message": Textarea(attrs={
                'class': 'blog_input_txt-ar',
                'placeholder': 'Повідомлення'
            }),
            "email": EmailInput(attrs={
                'class': 'blog_input',
                'placeholder': 'Email',
                'type': 'email'
            }),
            "date": DateInput(attrs={
                'class': 'blog_input',
                'placeholder': 'Дата надсилання',
                'type': 'date'
            })
        }


class MyUserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password']
        widgets = {
            "username": TextInput(attrs={
                'class': 'vns_input',
                'placeholder': 'Ім\'я',
                'name': 'name',
                'type': 'text'
            }),
            "email": EmailInput(attrs={
                'class': 'vns_input',
                'placeholder': 'Email',
                'name': 'email',
                'type': 'email'
            }),
            "password": PasswordInput(attrs={
                'class': 'vns_input',
                'placeholder': 'Пароль',
                'name': 'password',
                'type': 'password'
            })
        }
