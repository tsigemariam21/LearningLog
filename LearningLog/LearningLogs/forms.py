from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """A form for creating and editing topics."""
    class Meta(forms.ModelForm):
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        
class EntryForm(forms.ModelForm):
    """A form for creating and editing entries.""" 
    class Meta(forms.ModelForm):
        model = Entry
        fields = ['text'] 
        labels ={'text': ''} 
        Widgets = {'text': forms.Textarea(attrs={'cols': 60})}
        
        