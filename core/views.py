from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def index(request):
     return render(request, 'base.html')


def load_partial(request, page):
     """
     Load a partial template based on the page parameter.
     """
     try:
          # Render the specified partial template
          html = render_to_string(f'core/{page}.html')
          return HttpResponse(html)
     except:
          # If the template does not exist
          return HttpResponse('<p>Page not found.</p>', status=404)