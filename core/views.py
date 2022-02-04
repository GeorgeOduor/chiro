from django.shortcuts import render
from django.views import View
# Create your views here.

class Index(View):

    def get(self,request):
        context = {

        }
        return render(request,"core/landing.html",context)


class Home(View):

    def get(self,request):
        context = {

        }
        return render(request,"core/home.html",context)

class Actions(View):

    def get(self,request):
        context = {

        }
        return render(request,"core/actions.html",context)

class LoanDetails(View):

    def get(self,request):
        context = {

        }
        return render(request,"core/loan_details.html",context)

class ProductServicePurchase(View):

    def get(self,request):
        context = {

        }
        return render(request,"core/product_service_purchase.html",context) 

class AccountDetails(View):

    def get(self,request):
        context = {

        }
        return render(request,"core/account_details.html",context)

class LoanRepayment(View):
    
        def get(self,request):
            context = {
    
            }
            return render(request,"core/loan_repayment.html",context)

