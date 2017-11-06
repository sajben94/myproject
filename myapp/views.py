from django.shortcuts import render
from myapp.models import Users
from django.contrib.auth.models import User

from myapp import forms
# Create your views here.
def index(request):
    users_list = Users.objects.order_by('first_name')
    index_dict = {'message':users_list}
    return render(request,'myapp/index.html',context=index_dict)

def help(request):
    help_dict = {'help_msg':'This is help page!'}
    return render(request,'myapp/help.html',context=help_dict)

def form_name_view(request):
    form = forms.FormName()
    users_list = Users.objects.order_by('-id')

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            #DO SOMETHING Code
            print('VALIDATION SUCCESS!')
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = Users.objects.get_or_create(first_name=first_name,
                                               last_name=last_name,
                                               email=email)[0]
            form = forms.FormName() #return emply form

    return render(request,'myapp/form_page.html',{'form':form,'message':users_list})



def form_users_views(request):
    form = forms.FormUser()

    if request.method == 'POST':
        form = forms.FormUser(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get_or_create(first_name=first_name,
                                              last_name=last_name,
                                              email=email,
                                              username=username,
                                              is_staff = True)[0]
            user.set_password(password)
            user.save()
            form = forms.FormUser()

    return render(request,'myapp/form_users.html',{'form':form})
