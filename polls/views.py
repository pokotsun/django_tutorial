from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from .models import Question


# Create your views here.
#def index(request):
#    # return HttpResponse("Hello, world. You're at the polls index.")
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#
#    # 下と同義
#    #template = loader.get_template('polls/index.html')
#    #context = {
#    #    'latest_question_list': latest_question_list,
#    #}
#    #return HttpResponse(template.render(context, request))
#
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)
#
#def detail(request, question_id):
#    # 下と同義
#    # get_list_or_404()という関数もある
#    #try:
#    #    question = Question.objects.get(pk=question_id)
#    #except Question.DoesNotExist:
#    #    raise Http404("Question does not exist")
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question})
#
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', { 'question': question })
#    #response = f"You're looking at the results of question {question_id}"
#    #return HttpResponse(response)
#    #return HttpResponse(response, question_id)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    #def get_queryset(self):
    #    """Return the last five published questions."""
    #    return Question.objects.order_by('-pub_date')[:5]
    def get_queryset(self): 
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_query_set(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist): # request.POST['choice']が存在しなければ
        # Redisplay the question voting home
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



