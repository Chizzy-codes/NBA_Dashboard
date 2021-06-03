import os
# ---------------------------------------------------------
# Superset specific config
# ---------------------------------------------------------
ROW_LIMIT = 5000
SUPERSET_WORKERS = 4  # for it to work in heroku basic/hobby dynos increase as you like
SUPERSET_WEBSERVER_PORT = os.environ['PORT']
# ---------------------------------------------------------
MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY')

# ---------------------------------------------------------
# Flask App Builder configuration
# ---------------------------------------------------------
# Your App secret key
SECRET_KEY = 'Enter your secret key here'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# Superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# CACHE_CONFIG = {
#     'CACHE_TYPE': 'redis',
#     'CACHE_DEFAULT_TIMEOUT': 86400,
#     'CACHE_KEY_PREFIX': 'superset_results',
#     'CACHE_REDIS_URL': 'redis://localhost:6379/0'}

SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask-WTF flag for CSRF.
WTF_CSRF_ENABLED = CSRF_ENABLED = True

# use inserted X-Forwarded-For/X-Forwarded-Proto headers
ENABLE_PROXY_FIX = True
SQLLAB_ASYNC_TIME_LIMIT_SEC = 300
SQLLAB_TIMEOUT = 300
SUPERSET_WEBSERVER_TIMEOUT = 300

PUBLIC_ROLE_LIKE = 'Gamma'