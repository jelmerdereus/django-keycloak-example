from django.http import HttpRequest, HttpResponse
from primary.control.role_ctl import get_realm_roles
from django.template import loader
from primary.control.view_ctl import allow_methods


# index page
@allow_methods("GET")
def index(req: HttpRequest) -> HttpResponse:
    # log data about the user when it is logged in
    realm_roles = get_realm_roles(req.user)

    # render the index page
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request=req, context={
        "realm_roles": realm_roles,
    }))
