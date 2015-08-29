# make sure this is at the top if it isn't already
from django import forms
from django.core.exceptions import ValidationError
from home.models import Contact
from django.forms.util import ErrorList

class ContactForm(forms.ModelForm):
    
   

    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 30, 'rows': 5}))

    class Meta:
        model = Contact
        fields = ('email',)

    def send_email(self):
    	pass

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        domain_list = ["gmail.com", "yahoo.com", "hotmail.com","outlook.com","yahoo.co.in",'yahoo.in','']

        email = cleaned_data.get('email')

        if email is not None:
        	domain = email.split('@')[1]

        	if domain in domain_list:

        	   self._errors["email"] = ErrorList([u"Please use your company email id"])

        # Required only if Django version < 1.7 :
        return cleaned_data



  


        
