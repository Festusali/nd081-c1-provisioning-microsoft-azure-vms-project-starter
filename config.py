import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'flaskcmsassets'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'Yis62UohLNIK+cXrK+HqxBrpgSygPCnNZusjikJcJO0qGy49HrAp4PlwRJ63HfSWB/QQTwFd+ZtR+P4vt14dzg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'cms-asset'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'flask-cms-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'flask-cms-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'demo-flask'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'JUST-pass'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://' + SQL_USER_NAME + ':' + SQL_PASSWORD + '@' + SQL_SERVER + '/' + SQL_DATABASE
    'mssql+pyodbc://' + SQL_USER_NAME + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "da78eb78-ff76-41cf-9334-ceaef7dfb2cf"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/ebf53a13-57e2-4a4d-b658-32d4ab27fd58"

    CLIENT_ID = "6603f630-b33a-4058-9115-a70edf7c388e"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session