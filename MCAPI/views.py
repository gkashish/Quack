from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from allennlp.predictors.predictor import Predictor
from .forms import QuestionForm

app_name = 'Mcapi'

predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz")

def func(request):
    ans = ''
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            passage = form.cleaned_data['para']
            question = form.cleaned_data['ques']
            print(passage)
            ans = predictor.predict(passage=passage, question=question)['best_span_str']
            print(ans)
            return render(request, 'Mcapi/base.html', {
                'form': form,
                    'answer': ans
            })
    else:
        form = QuestionForm()
    return render(request, 'Mcapi/base.html', {
            'form': form,
            'answer': ans,
        })