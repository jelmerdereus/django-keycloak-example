from django.http import HttpRequest, HttpResponse
from django.template import loader

from primary.control.keycloak import get_realm_roles
from primary.control.views import allow_methods, allow_krole


# index page
@allow_methods("GET")
def index(req: HttpRequest) -> HttpResponse:
    # log data about the user when it is logged in
    realm_roles = get_realm_roles(req.user)
    special_permission = "django_special_test" in realm_roles

    # render the index page
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request=req, context={
        "realm_roles": realm_roles,
        "special_permission": special_permission
    }))

@allow_methods("GET")
@allow_krole("django_special_test")
def special(req: HttpRequest) -> HttpResponse:
    # render the special page
    template = loader.get_template('special.html')
    return HttpResponse(template.render(request=req, context={}))
