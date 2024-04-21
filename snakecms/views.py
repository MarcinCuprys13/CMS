from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Profile
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth import login

@login_required(login_url='/accounts/login/') 
def page_creator(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        person_text = request.POST.get("personText")
        head_color = request.POST.get('headColor')
        project_text = request.POST.get("projectText")
        body_color = request.POST.get('bodyColor')
        footer_color = request.POST.get('footerColor')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        user_photo = request.FILES.get('user_photo')
        website_photo = request.FILES.get('website_photo')

        profile = Profile(
            title=title,
            first_name=first_name,
            last_name=last_name,
            person_text=person_text,
            head_color=head_color,
            project_text=project_text,
            body_color=body_color,
            footer_color=footer_color,
            phone=phone,
            email=email,
            user_photo=user_photo,
            website_photo=website_photo,
            user=request.user  
        )
        profile.save()
        return redirect('home')
    else:
        return render(request, 'page_creator.html')

@login_required(login_url='/accounts/login/') 
def my_view(request):
    if request.user.is_authenticated:
        user_profiles = Profile.objects.filter(user=request.user)
        return render(request, 'home.html', {'user_profiles': user_profiles})
    else:
        return render(request, 'base.html')

def my_register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def page(request, id):
    profile = get_object_or_404(Profile, pk=id)
    return render(request, 'index.html', {'profile': profile})


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['title', 
              'first_name', 
              'last_name',
              'person_text',
              'head_color',
              'project_text',
              'body_color', 
              'footer_color', 
              'phone', 
              'email', 
              'user_photo', 
              'website_photo']
    
    template_name = 'profile_edit_form.html'
    success_url = reverse_lazy('home') 

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
