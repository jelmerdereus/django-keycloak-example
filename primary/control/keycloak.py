import logging

from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User


def get_realm_roles(usr: User) -> list[str]:
    """
    Get the realm roles for a user that are stated in the userinfo field
    e.g. ['django_generic_access', 'offline_access', 'default-roles-jaylabs',
    'uma_authorization', 'django_special_test']
    """
    try:
        social_account = SocialAccount.objects.get(user=usr)
        extra_data = social_account.extra_data

        return extra_data["userinfo"]["realm_access"]["roles"]

    except Exception as ex:
        logging.debug(f"No realm roles for user <{usr.username}> in userinfo: {ex}")
        return []
