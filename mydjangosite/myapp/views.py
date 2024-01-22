from django.shortcuts import render, redirect
from .forms import ResultForm
from .models import Result

# Create your views here.
def calculate_average(maths, english, science):
    if maths > 0 and english > 0 and science > 0:
        return (english + maths + science) / 3
    else:
        return 0
def index(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            average = (90 + 90 + 100)/3

            return redirect('index')
    else:
        form = ResultForm()
        average = ResultForm()

        results = Result.objects.all()
    return render(request, 'myapp/index.html', {'form': form, 'result': results, 'average':average })
