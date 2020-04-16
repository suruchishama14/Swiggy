from django import forms
from Restaurant.models import RestaurantModel,Food

class RestaurantForm(forms.ModelForm):
    restro_password = forms.CharField(max_length=30,widget=forms.PasswordInput)
    class Meta:
        model = RestaurantModel
        fields = "__all__"
        exclude = ('restro_otp','restro_status')

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"
