import os

# Superset specific config
ROW_LIMIT = 5000

#SUPERSET_WEBSERVER_PORT = os.environ['PORT']

SUPERSET_WORKERS = 1  # for it to work in heroku basic/hobby dynos increase as you like

# Flask App Builder configuration
# Your App secret key
SECRET_KEY = 'lK-Ef8QDSHyQ_eCuPuS26h7EER19IRDfy9D0N5rcHtA='

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = 'postgres://mkksdclxfvuzqi:d48a32b37dea6621dc303a981d0cfac93c17cb52bc95fd57e27a8218b6e87032@ec2-18-215-111-67.compute-1.amazonaws.com:5432/d8cj90v5okhm5a'

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = CSRF_ENABLED = True

# use inserted X-Forwarded-For/X-Forwarded-Proto headers
ENABLE_PROXY_FIX = True
SQLLAB_ASYNC_TIME_LIMIT_SEC = 300
SQLLAB_TIMEOUT = 300
SUPERSET_WEBSERVER_TIMEOUT = 300