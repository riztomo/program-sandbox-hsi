from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import is_valid_path
from .models import Questions, Answer
import random

# Create your views here.
def home(request):
    return render(request, 'evaluasi/home.html')

def evaluasi(request):
    passed = 0
    
    max = Questions.objects.count()
    questions = Questions.objects.all()
    answer = Answer()

    if max >= 2:

        choice1 = random.randint(0, max-1)

        while passed == 0:
            choice2 = random.randint(0, max-1)
            if choice2 != choice1:
                passed = 1

        question1 = questions[choice1]
        question2 = questions[choice2]
        
        if request.method == 'POST':
            answer.Name = request.POST['user']
            
            answer.question1 = question1.question
            answer.option_one1 = question1.option_one
            answer.option_two1 = question1.option_two
            answer.option_three1 = question1.option_three
            answer.option_four1 = question1.option_four
            answer.ans1 = question1.ans
            answer.question2 = question2.question
            answer.option_one2 = question2.option_one
            answer.option_two2 = question2.option_two
            answer.option_three2 = question2.option_three
            answer.option_four2 = question2.option_four
            answer.ans2 = question2.ans

            selected_option1 = request.POST['question1']
            if selected_option1 == 'option_one1': answer.yourAnswer1 = answer.option_one1
            elif selected_option1 == 'option_two1': answer.yourAnswer1 = answer.option_two1
            elif selected_option1 == 'option_three1': answer.yourAnswer1 = answer.option_three1
            elif selected_option1 == 'option_four1': answer.yourAnswer1 = answer.option_four1
            else: return HttpResponse(400, 'Invalid form')

            selected_option2 = request.POST['question2']
            if selected_option2 == 'option_one2': answer.yourAnswer2 = answer.option_one2
            elif selected_option2 == 'option_two2': answer.yourAnswer2 = answer.option_two2
            elif selected_option2 == 'option_three2': answer.yourAnswer2 = answer.option_three2
            elif selected_option2 == 'option_four2': answer.yourAnswer2 = answer.option_four2
            else: return HttpResponse(400, 'Invalid form')

            answer.save()

            return redirect('/')

        context = { 'question1': question1, 
                    'question2': question2
                    }
    
        return render(request, 'evaluasi/evaluasi.html', context)

    else:
        return render(request, 'evaluasi/error-insufficient-questions.html')

def hasil(request):
    answers = Answer.objects.all()
    context = {'hasil': answers}
    return render(request, 'evaluasi/hasil.html', context)

def tambah(request):
    question = Questions()
    if request.method == 'POST':
        
        question.question = request.POST['question']
        question.option_one = request.POST['option1']
        question.option_two = request.POST['option2']
        question.option_three = request.POST['option3']
        question.option_four = request.POST['option4']
        answer = request.POST['answer']
        if answer == 'option_one': question.ans = question.option_one
        elif answer == 'option_two': question.ans = question.option_two
        elif answer == 'option_three': question.ans = question.option_three
        elif answer == 'option_four': question.ans = question.option_four
        question.save()
        return redirect('/admin/daftar-soal')
    else:
        question = Questions()
    return render(request, 'evaluasi/tambah_soal.html')

def ubah(request, id):
    soalDiubah = Questions.objects.get(id=id)
    if request.method == 'POST':
        soalDiubah.question = request.POST['question']
        soalDiubah.option_one = request.POST['option1']
        soalDiubah.option_two = request.POST['option2']
        soalDiubah.option_three = request.POST['option3']
        soalDiubah.option_four = request.POST['option4']
        answer = request.POST['answer']
        if answer == 'option_one': soalDiubah.ans = soalDiubah.option_one
        elif answer == 'option_two': soalDiubah.ans = soalDiubah.option_two
        elif answer == 'option_three': soalDiubah.ans = soalDiubah.option_three
        elif answer == 'option_four': soalDiubah.ans = soalDiubah.option_four
        soalDiubah.save()
        
        return redirect('/admin/daftar-soal')

    context = {'soalDiubah' : soalDiubah}
    return render(request, 'evaluasi/ubah_soal.html', context)

def daftar(request):
    semuaPertanyaan = Questions.objects.all()
    return render(request, 'evaluasi/daftar_soal.html', context = {'pertanyaan': semuaPertanyaan})

def admin(request):
    return render(request, 'evaluasi/admin.html')