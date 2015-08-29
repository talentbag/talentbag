from django.views.generic import FormView
from home.forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.models import Contact
from django.contrib import messages

# Create your views here.




class HomeView(FormView):

    form_class = ContactForm
    template_name = 'home/index.html'
    success_url = '/'


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(HomeView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        type_plan = request.POST.get('type', '')
        if form.is_valid():
            # <process form cleaned data>
            email = request.POST.get('email', '')
            
            email_obj = Contact(email=email)
            email_obj.validate_unique(exclude=None);
            email_obj.save()

            messages.add_message(self.request, messages.SUCCESS, 'Email sent.We will reach out asap!')


            return HttpResponseRedirect('/')



        return render(request, self.template_name, {'form': form, 'type_plan':type_plan})