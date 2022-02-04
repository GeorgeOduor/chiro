from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, SignupForm
from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.views import View
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from core.loanmanager import LoanManager
from core.loanmanager import checkProfile
from core.models import tbl_Clients

User = get_user_model()


# Create your views here.
class LoginPage(View):
    loginform = LoginForm
    profilecheck = checkProfile
    template_name = 'accounts/signin.html'

    def get(self, request):
        form = self.loginform()

        user = request.user
        if user.is_authenticated:
            return redirect('core:home')
        else:
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        try:
            phone_no = request.POST.get('phone_no')
            password = request.POST.get('password')
            user = authenticate(phone_no=phone_no, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # filter tbl_clients and return client Type
                    clients = tbl_Clients.objects.filter(user_id=user.id)
                    client_type = clients.values_list('ClientType')[0][0]
                    self.profilecheck(user.id, client_type)
                    return redirect('home')
                else:
                    return HttpResponse('Your account is not active!')
            else:
                return redirect('accounts:signin')
        except Exception as  e:
            return HttpResponse(e)
        

class SignUp(View):
    formclass = SignupForm
    initial = {'key': 'value'}
    template_name = 'accounts/signup.html'
    loanmanager = LoanManager

    def get(self, request):
        form = self.formclass(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.formclass(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # create a new user profile and save it
            client = lambda x :'C' if x == '1' else '2'
            self.loanmanager().createProfile(
                client_type = client(form_data['accountType']) ,
                mobile_no = form_data['phone_no'],client_id=user.id)
            # current_site = get_current_site(request)
            # mail_subject = 'Activate your blog account.'
            # message = render_to_string('accounts/acc_activa_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),#.decode('utf-8'),
            #     'token': account_activation_token.make_token(user),
            # })
            to_email = form.cleaned_data.get('email')
            # email = EmailMessage(
            #     mail_subject, message, to=[to_email]
            # )
            # email.send()
            return redirect('accounts:signin')
            # print('email sent')
        else:
            print(form.errors)
            return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')


class ResetPasswordView(SuccessMessageMixin,PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('/')


def ProfileView(request):
    return render(request, 'accounts/profile.html')
     