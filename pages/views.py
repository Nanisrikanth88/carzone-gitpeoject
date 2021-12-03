from django.shortcuts import render

# Create your views here.
def home(request):
    print("+"*100)
    return render(request, 'pages/home.html')
