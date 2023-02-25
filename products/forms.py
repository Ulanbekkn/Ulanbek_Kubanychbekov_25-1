from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(min_length=5, max_length=255)
    description = forms.CharField(widget=forms.Textarea())
    phone_status = forms.IntegerField()


class ReviewCreateForm(forms.Form):
    text = forms.CharField(max_length=355)
    rate = forms.IntegerField()
