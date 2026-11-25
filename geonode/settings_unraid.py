from .settings import *  # noqa: F401,F403

# The dedicated Nginx configuration overwrites this header.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
