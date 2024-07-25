from django.shortcuts import render
from datetime import datetime

# Create your views here.

def greet(request):
    current_time = datetime.now()
    hour = current_time.hour

    if hour < 12:
        greeting = "Good morning."
    elif hour < 17:
        greeting = "Good afternoon."
    else:
        greeting = "Good Evening."
        
    return render(request, 'greet.html', {'greeting': greeting})
