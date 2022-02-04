
from django.urls import path
from .views import Home, Index,Actions, LoanDetails
app_name = 'core'
urlpatterns = [
    path('',Index.as_view(),name='home'),
    path('profile_landing',Home.as_view(),name='profile_landing'),
    path('actions',Actions.as_view(),name='actions'),
    path('loan_details',LoanDetails.as_view(),name='loan_details'),
]
