from django.shortcuts import render
from django.http import HttpResponse, Http404
from polls.models import Course

# Create your views here.
from django.template import loader

from polls.models import Question


def index(request):
    object_list = Course.objects.all()
    # template = loader.get_template('polls/index.html')
    context = {
        'object_list': object_list
    }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists")
    # return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/index.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def course(request, question_id):
    pass

# def home_view(request):
#     object_list = [1, 2, 3]
#     return render(request, 'index.html', {
#         'object_list': object_list
#     })
