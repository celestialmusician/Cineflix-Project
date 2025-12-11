from django.template import Library

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