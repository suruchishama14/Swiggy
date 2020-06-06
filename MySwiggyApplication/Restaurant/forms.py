from django import forms
from Restaurant.models import RestaurantModel, FoodModel
from adminpage.forms import AreaForm, RestaurantTypeForm
from adminpage.models import AreaModel, RestaurantTypeModel


class RestaurantForm(forms.ModelForm):
    restro_name = forms.CharField( max_length=30,label="")
    restro_contact = forms.IntegerField(label="")
    restro_email= forms.EmailField(max_length=100,label="")
    restro_area = forms.ModelChoiceField(queryset=AreaModel.objects.all(),label="")
    restro_type = forms.ModelChoiceField(queryset=RestaurantTypeModel.objects.all(),label="")
    restro_password = forms.CharField(max_length=30,widget=forms.PasswordInput,label="")
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