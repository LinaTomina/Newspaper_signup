from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Category

class CategorySubscriberView(View):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categorysubscriber'

    def get_object (self, **kwargs):
        id = self.kwargs.get('pk')
        return Category.objects.get(pk=id)

    def get (self, request, *args, **kwargs):
        return render (request, "category.html", {})

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        current_user = self.request.user
        current_category = self.request.category_name
        subscription = Category(
            subscribers = current_user.username, category_name = current_category
        )
        subscription.save() 
        
html_content = render_to_string(
    'subscription_created.html',
    {
        'subscription': subscription,
    }
)


msg = EmailMultiAlternatives(
    subject = f'{subscription.subscriber.username}',
    body = subscription.category_name,
    from_email = '',
    to =[subscription.subscriber.email]
)
msg.attach_alternative(html_content, "text/html")

msg.send()

Category.objects.get(pk=id).subscribers.add(current_user)

return redirect('news:id')