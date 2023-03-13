from django.urls import path
from .views import SuccessView, CancelView,CreateCheckoutSessionView, ProductLandingPageView, stripe_webhook, StripeIntentView, CustomPaymentView


urlpatterns = [
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', ProductLandingPageView.as_view(), name='landing'),
    path('webhook/stripe/', stripe_webhook, name='stripe-webhook'),
    path('custom-payment/', CustomPaymentView.as_view(), name='create-payment-intent'),
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
]