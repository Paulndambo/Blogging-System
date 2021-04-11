from django import forms

from . models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category',
                  'body', 'snippet', 'blog_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'username', 'type': 'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body', 'snippet', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }
