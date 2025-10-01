from django.shortcuts import render

def calculate_power(request):
    power = None
    if request.method == 'POST':
        try:
            I = float(request.POST.get('intensity'))
            R = float(request.POST.get('resistance'))
            power = I ** 2 * R
        except (ValueError, TypeError):
            power = "Invalid input. Please enter numbers."
    return render(request, 'mathapp/math.html', {'power': power})
