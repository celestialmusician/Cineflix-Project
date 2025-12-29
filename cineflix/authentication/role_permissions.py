from django.template import Library

from subscriptions.models import UserSubscriptions
register = Library()


# @register.simple_tag
# def display_message(msg):

#     return f"Message is {msg}"



# # @register.simple_tag
# # def add_number(a, b):

# #     return a + b

@register.simple_tag
def allowed_roles(request,roles) :

    roles=eval(roles)

    if request.user.is_authenticated and request.user.role in roles :

        return True
    
    return False



@register.simple_tag

def active_subscription_plan(request):

    if request.user.is_authenticated and request.user.role == 'User' :

        user = request.user

        try :                           

            plan = UserSubscriptions.objects.filter(profile=user,active=True).latest('created_at')

            return plan 
    
        except:

            pass

        
    return None