from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')  

def chart(request):
    return render(request, 'chart.html')

def developers(request):
    return render(request, 'developers.html')
