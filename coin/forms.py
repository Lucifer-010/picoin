from django import forms
from .models import PassPhrase
class PhraseForm(forms.ModelForm):
    class  Meta:
        model = PassPhrase
        fields = ("phrase",)
    def __init__(self,*arg,**kwarg):
        super(PhraseForm,self).__init__(*arg,**kwarg)
        self.fields['phrase'].widget.attrs['class']='form-control' 
        self.fields['phrase'].widget.attrs['placeholder']='Enter your 24-word passphrase here' 
