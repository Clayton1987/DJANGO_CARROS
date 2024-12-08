from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Car

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
    cars = Car.objects.all()
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

