from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from .models import Choice, Question
def add_question(request): 
    return render(request, 'polls/add_question.html', '')
def testchoice(request): 
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/testchoice.html',  context)

def add_question_todb(request):
    error_message = 0
    try:
        question = request.POST['question']
    except :
        error_message = 1 
    else:
        if question == "":
            error_message = 1 
        else :
            q=Question(question_text=question, pub_date=timezone.now())
            q.save()
        return render(request, 'polls/add_question_todb.html', {'question':question,'error_message':error_message})

def add_choice_todb(request): 
    choice = request.POST['choice']
    nquestion = request.POST['nquestion']
    for i in range (Question.objects.count()):
        if (nquestion == Question.objects.get(pk=i)):
            q=Question.objects.get(pk=i)
            q.choice_set.create(choice_text=choice, votes=0)
    return render(request, 'polls/add_choice_todb.html', {'choice':choice})

def add_choice(request, question_id):  
    choice = request.POST['choice']
    q = Question.objects.get(pk=question_id)
    q.choice_set.create(choice_text=choice, votes=0)
    return render(request, 'polls/add_choice.html',{'choice':choice})
       
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
