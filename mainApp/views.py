from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
def home(requests):
    return HttpResponse('Dastru ishladi')

def bosh_sahifa(requests):
    context = {'markaz': "Codial It Academy"}
    return render(requests, 'index.html', context)

def students(request):
    students = Talaba.objects.all()
    if request.GET.get('search'):
        students = students.filter(ism__contains=request.GET['search'])
    context = {
        'students': students,
    }
    return render(request, 'students.html', context)


def student(requests, pk):
    s = Talaba.objects.get(id=pk)
    context = {
        'studnet': s
    }
    return render(requests, 'student.html', context)


def studensts_kiotb__gt0(requests):
    students = Talaba.objects.filter(kitob_soni__gt=0)
    context = {
        'students': students
    }
    return render(requests, 'students_kitob__gt0.html', context)


def student_qoshish(requests):
    if requests.method == 'POST':
        # if requests.POST.get('ism') in Talaba.objects.values_list('ism', flat=True):
        #     return HttpResponse("Bu ism mavjud")
        Talaba.objects.create(
            ism=requests.POST.get('ism'),
            kurs=requests.POST.get('kurs'),
            guruh=requests.POST.get('guruh'),
            kitob_soni=requests.POST.get('kitob_soni')
        )
        return redirect('/students/')
    return render(requests, 'student_qoshish.html')

def muallif_qoshish(request):
    if request.method == 'POST':
        Muallif.objects.create(
            ism=request.POST.get('ism'),
            jins=request.POST.get('jins'),
            t_sana=request.POST.get('t_sana'),
            kitob_soni=request.POST.get('kitob_soni'),
            tirik=request.POST.get('tirik')

        )
        return redirect('/muallif_q/')
    return render(request, 'muallif_qoshish.html')

def kitoblar(requests):
    if requests.method == 'POST':
        Kitob.objects.create(
            nom=requests.POST.get('nom'),
            janr=requests.POST.get('janr'),
            sahifa=requests.POST.get('sahifa'),
            muallif=Muallif.objects.get(id=requests.POST.get('muallif_id'))
        )
        return redirect('/kitoblar/')
    kitoblar = Kitob.objects.all()
    mualliflar = Muallif.objects.all()
    context = {
        'kitoblar': kitoblar,
        'mualliflar': mualliflar
    }
    return render(requests, 'kitoblar.html')


def muallif_form(request, pk):
    muallif = Muallif.objects.get(id=pk)
    if request.method == 'POST':
        form = MuallifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mualliflar/')
    context = {
        'maullif': muallif,
        'form': MuallifForm(instance=muallif)
    }
    return render(request, 'muallif_form.html', context)