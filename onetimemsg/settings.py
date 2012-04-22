"""
Settings for OneTimeMsg

@see: http://flask.pocoo.org/docs/config/

"""

# Name and port number of the server
SERVER_NAME = None
# Optional subdirectory where the app lives (e.g. '/app/')
APPLICATION_ROOT = None

DEBUG = True
TESTING = True

SECRET_KEY = 'make me secret'

SESSION_COOKIE_NAME = 'OTMSESS'
PERMANENT_SESSION_LIFETIME = (60 * 60 * 24 * 30) # 30 days

# This URI generally takes the form of
#     driver://username:password@host:port/database
# SQLite URIs don't use the hostname, so there's an additional slash
# for relative paths:
#     sqlite:///test.db
# and two additional slashes for absolute paths:
#     sqlite:////tmp/test.db
# To create an SQLite database in memory, omit the path:
#     sqlite://
# 
# @see: http://docs.sqlalchemy.org/en/latest/core/engines.html#supported-databases
SQLALCHEMY_DATABASE_URI = 'sqlite:////abs/path/to/db'