from django import forms
from .models import get_feedback

class get_to_know(forms.ModelForm):
    # name = forms.CharField(label='Name ', required=False)
    # email = forms.EmailField(label='Email ')
    # remarks = forms.CharField(label='Message ')    
        
    def __init__(self, *a, **k):
        super(get_to_know,self).__init__(*a, **k)
        self.fields['name'].required = False
        self.fields['name'].widget = forms.TextInput(attrs={'placeholder':'your full name',})
        self.fields['email'].widget = forms.TextInput(attrs={'placeholder':'your email ID',})
        self.fields['remarks'].widget = forms.Textarea(attrs={'placeholder':'Hey Aseem...','rows':'5',})  
    class Meta:
        model = get_feedback
        fields = "__all__"
    def clean(self):
        cleaned_dt = super(get_to_know,self).clean()
        name = cleaned_dt.get('name')
        email = cleaned_dt.get('email')
        remarks = cleaned_dt.get('remarks')
        if not name and not email and not remarks:
            raise forms.ValidationError("Don't leave it empty")


