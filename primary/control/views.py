import logging
from functools import wraps

from django.http import HttpRequest, HttpResponse

from primary.control.keycloak import get_realm_roles


def allow_methods(*methods: str):
    """
    restrict a view to specific HTTP methods
    """
    allowed = {m.upper() for m in methods}

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(req: HttpRequest, *args, **kwargs) -> HttpResponse:
            if req.method.upper() not in allowed:
                logging.warning(f"Forbidden request: {req.method} @ {req.path} by {req.get_host()} "
                                f"(allowed: {sorted(allowed)})")
                return HttpResponse("Forbidden", status=403)
            return view_func(req, *args, **kwargs)

        return _wrapped

    return decorator

def allow_krole(realm_role: str):
    """
    restrict a view to users with a given keycloak realm role
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(req: HttpRequest, *args, **kwargs) -> HttpResponse:
            user = req.user
            if realm_role not in get_realm_roles(user):
                logging.warning(f"Forbidden request: {req.method} @ {req.path} by {req.get_host()} "
                                f"(allowed: {realm_role})")
                return HttpResponse("Forbidden", status=403)
            return view_func(req, *args, **kwargs)
        return _wrapped
    return decorator
