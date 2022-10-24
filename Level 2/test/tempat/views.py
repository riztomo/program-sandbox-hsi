from django.shortcuts import render
from django.http import HttpResponse
from . import soal
import random



# Create your views here.
def tempat_menjawab(request):
    option1 = random.randint(0, 4)
    option2 = option1
    while option2 == option1:
        option2 = random.randint(0, 4)
    option1 = str(option1)
    option2 = str(option2)

    return render(request, 'hal_soal.html', {
        'soalpertama':soal.soal[option1]['tanya'],
        'jwbpertama1':soal.soal[option1]['jawaban']['0'],
        'jwbpertama2':soal.soal[option1]['jawaban']['1'],
        'jwbpertama3':soal.soal[option1]['jawaban']['2'],
        'jwbpertama4':soal.soal[option1]['jawaban']['3'],
        'jwbpertama':soal.soal[option1]['benar'],
        'soalkedua':soal.soal[option2]['tanya'],
        'jwbkedua1':soal.soal[option2]['jawaban']['0'],
        'jwbkedua2':soal.soal[option2]['jawaban']['1'],
        'jwbkedua3':soal.soal[option2]['jawaban']['2'],
        'jwbkedua4':soal.soal[option2]['jawaban']['3'],
        'jwbkedua':soal.soal[option2]['benar'],
    })

def tampilkan_soal(request):
    return render(request, 'admin.html')