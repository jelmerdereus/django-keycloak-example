import logging
from django.http import HttpRequest, HttpResponse
from functools import wraps

def allow_methods(*methods: str):
    """
    Decorator to restrict a view to specific HTTP methods.
    If the request method is not allowed, return 403 Forbidden.
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
