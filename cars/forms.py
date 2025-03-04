from django import forms
from cars.models import Brand, Car

### DJANGO FORMS
class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) #BUSCAR BRAND COM QUERY
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo']
         
        )
        car.save()
        return car
    
### DJANGO MODEL FORMS

class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        #fields = ('model', 'brand', 'factory_year', 'model_year', 'plate', 'value', 'photo' )
        fields = '__all__'

    def clean_value(self):
        #value = self.cleaned_data['value'] #VARIAÇÃO DE SELEÇÃO CAMPO
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'O valor do carro deve ser maior que R$ 20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'O ano de fabricação deve ser maior que 1975')
        return factory_year
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo:
            self.add_error('photo', 'Favor Importar uma Foto!')
        return photo