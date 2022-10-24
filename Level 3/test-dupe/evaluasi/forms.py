from django.forms import ModelForm
from .models import Answer, Questions

class CreateQuestion(ModelForm):
    class Meta:
        model = Questions
        fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four', 'ans']

class InsertName(ModelForm):
    class Meta:
        model = Answer
        fields = ['Name']