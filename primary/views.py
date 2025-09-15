from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from .control.view_ctl import allow_methods


# index page
@allow_methods("GET")
def index(req: HttpRequest) -> HttpResponse:
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request=req))


