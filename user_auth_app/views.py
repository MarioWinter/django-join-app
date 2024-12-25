from django.shortcuts import render
from django.shortcuts import redirect


def redirect_to_admin(request):
    """
    Redirects the user to the Django admin interface.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponseRedirect: A redirect response to the Django admin index page.
    """
    
    return redirect('admin:index')