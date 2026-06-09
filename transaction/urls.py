from django.urls import path

from transaction.views import callback_view

urlpatterns = [
    # Exercise Category
    path('callback/',callback_view),

]