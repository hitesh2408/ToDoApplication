from django.shortcuts import render

def custom_404_view(request, exception):
    """Custom 404 view"""
    return render(request, '404.html', {}, status=404)
