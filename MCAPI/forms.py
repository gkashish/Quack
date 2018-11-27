from django import forms


class QuestionForm(forms.Form):
    para = forms.CharField(label='Enter para', max_length=100000)
    ques = forms.CharField(label='Enter ques', max_length=1000)
   # answ = forms.CharField(label='Answer here : ', max_length=1000)
