from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import UsersEmails , Items
from .forms import EmailsForm

# Create your views here.
def index(request):
	ityms = Items.objects.all()
	
	return render(request,'items/index.html',{'ityms':ityms})

def landing_page(request):
	if request.method=='POST':
		form = EmailsForm(request.POST)
		if form.is_valid():
			b = form.save(commit=False)
			b.save()
			redirect('items/thankyou.html')
	else : 
			form = EmailsForm()
			
	
	return render(request,'items/landing_page.html',{'form':form} )
	