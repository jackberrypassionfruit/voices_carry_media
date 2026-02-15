from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "base/index.html", context)

def demos(request):
    return render(request, "demos/index.html")

