from django import forms


class ProductCreateForm (forms.Form):
    title = forms.CharField(max_length=200)
    price = forms.IntegerField()
    text = forms.CharField(max_length=200)

class ReviewCreateForm(forms.Form):
    author = forms.CharField(max_length=200)
    text = forms.CharField()
