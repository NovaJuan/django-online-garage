from django import forms


class ReviewForm(forms.Form):
    author = forms.CharField(label='Author', max_length=100, required=True)
    content = forms.CharField(label='Review', required=True)
    rating = forms.IntegerField(
        label='Rating', min_value=1, max_value=5, required=True)
