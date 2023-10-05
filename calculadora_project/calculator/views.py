from django.shortcuts import render, HttpResponse

def home(request):
    resultado = None  # Inicializamos resultado a None
    if request.method == "POST":
        numero1 = float(request.POST.get('numero1', 0))
        numero2 = float(request.POST.get('numero2', 0))

        operacion = request.POST.get('operaciones')

        resultado = calcular_resultado(numero1, numero2, operacion)

    return render(request, 'home.html', {'resultado': resultado})

def calcular_resultado(numero1, numero2, operacion):
    if operacion == 'sumar':
        return numero1 + numero2
    elif operacion == 'restar':
        return numero1 - numero2
    elif operacion == 'multiplicar':
        return numero1 * numero2
    elif operacion == 'dividir':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return 'Error: División por cero'

def calculate(request):
    return HttpResponse("Requisito inválido")  # No se utiliza esta función
