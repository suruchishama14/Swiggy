from django import forms
from Restaurant.models import RestaurantModel, FoodModel


class RestaurantForm(forms.ModelForm):
    restro_password = forms.CharField(max_length=30,widget=forms.PasswordInput)
    class Meta:
        model = RestaurantModel
        fields = "__all__"
        exclude = ('restro_id', 'restro_otp', 'restro_status')

class RestroLoginForm(forms.Form):
    contactno = forms.IntegerField()
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)
class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodModel
        fields = ('food_name',)