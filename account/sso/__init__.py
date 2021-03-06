import os
from django.conf import settings
# from login.models import Role


def _load_setting(n, default):
    return getattr(settings, n) if hasattr(settings, n) else default


REMOTE_AUTH_TOKEN_URL = "/uams/authtoken"
REMOTE_AUTH_USER_URL = "/uams/authuser"
REMOTE_SSO_LOGIN_URL = "/uams/login"
REMOTE_SSO_LOGOUT_URL = "/uams/logout"
REMOTE_SSO_SIGNUP_URL = "/uams/signup"
REMOTE_SSO_RESETPWD_URL = "/uams/resetpwd"
REMOTE_SSO_CHANGEPWD_URL = "/uams/changepwd"
REMOTE_SSO_CHANGEMAIL_URL = "/uams/changemail"

logined_users = {}  # logging users

