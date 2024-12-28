from django.shortcuts import render, redirect
from django.http import HttpResponse
from cars.models import Car
from cars.forms import CarForm, CarModelForm
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.


# def cars_view(request):
#     # return render(request, 'cars.html')  # render the cars.html template
#     html = '''
#         <html>
#             <head>
#                 <title>My Cars</title>
#             </head>
#             <body>
#                 <h1>My Cars</h1>
#                 <h3>So carro top<h3>
#                 <p>This is a list of my cars</p>
#             </body>
#         </html>
#     '''
#     #return HttpResponse(html)  # return the html as a response
#     return HttpResponse('This is cars view = MEUS CARROS')  # return a simple HTTP response

def cars_view(request):
    #cars = Car.objects.all()
    #cars = Car.objects.filter(brand__name='Fiat')  #consulta marca em outra tabela
    # cars = Car.objects.filter(model='UNO DA FIRMA') # NOME EXATADO DA STRING
    #cars = Car.objects.filter(model__contains='FIRMA') # CONTAINS NA STRING
    #print(request)
    print(request.GET)# buscar por GET /cars/?search=Teste123&nome=PycodeBR
    request.GET.get('search') # buscar por GET /cars/?search=Teste123&nome=PycodeBR
    print(request.GET.get('search'))
    #RESULTADO:
    # <QueryDict: {'search': ['Teste123'], 'nome': ['PycodeBR']}>
    # Teste123
    # [07/Dec/2024 11:07:21] "GET /cars/?search=Teste123&nome=PycodeBR HTTP/1.1" 200 321

    ##########################################
    # FAZENDO FILTRO DO USUARIO NO NAVEGADOR
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search') #informação  dode busca do ususario
    if search:
        #cars = Car.objects.filter(model__contains=search) # busca no banco com filter
        #cars = Car.objects.filter(model__icontains=search) # busca no banco com filter igorando casesensitive
        cars = Car.objects.filter(model__icontains=search).order_by('model') # busca no banco com filter igorando casesensitive


    #print(cars)
    #return render(request, 'cars.html')  # render the cars.html template
    #return render(request, 'cars.html', {'cars': {'model' : 'Astra 2.0'}})  # render the cars.html
    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )

#CRIANDO CBV PARA SUBTITUIR AS FUNCOES BV

class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search') #informação  dode busca do ususario
        
        if search:
            cars = Car.objects.filter(model__icontains=search).order_by('model') # busca no banco com filter igorando casesensitive
        
        return render(
            request, 
            'cars.html', 
            {'cars': cars}
        )

#CRIANDO CBV PARA SUBTITUIR AS FUNCOES BV USANDO CBV

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    #queryset = Car.objects.all().order_by('model')

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search') #informação  dode busca do usus
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

def new_car_view(request):

    if request.method == 'POST':
        #new_car_form = CarForm(request.POST, request.FILES)
        new_car_form = CarModelForm(request.POST, request.FILES)
        print(new_car_form.data)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        #new_car_form = CarForm()
        new_car_form = CarModelForm()

   
    return render(request, 'new_car.html', {'new_car_form': new_car_form })



#CRIANDO CBV PARA SUBTITUIR AS FUNCOES BV
class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', {'new_car_form': new_car_form })
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form': new_car_form })
    
    
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

class CarDetailView(DeleteView):
    model = Car
    template_name = 'car_detail.html'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/cars/'

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'