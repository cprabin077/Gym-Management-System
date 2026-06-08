from django.urls import path

from subscription.api.views import MembershipPayment, SubscriptionUpdateAndDelete, SubscriptionView, MembershipView


urlpatterns = [
    path('', SubscriptionView.as_view(), name="subscription"),
    path('<int:pk>', SubscriptionUpdateAndDelete.as_view(), name="subscription-update"),
    path('membership', MembershipView.as_view(), name="membership-update"),
    path('payment/<int:id>',MembershipPayment.as_view())
]