from django.shortcuts import render, redirect
from .forms import ResultForm
from .models import Result

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ResultForm()

    results = Result.objects.all()
    return render(request, 'myapp/index.html',{'form': form, 'result': results})