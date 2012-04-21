from flask import abort
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from onetimemsg import app

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# @see: https://github.com/mitsuhiko/flask-sqlalchemy/blob/master/flask_sqlalchemy.py#L354
def get_or_404(self, ident):
    rv = self.get(ident)
    if rv is None:
        abort(404)
    return rv
Base.get_or_404 = get_or_404

# @see: https://github.com/mitsuhiko/flask-sqlalchemy/blob/master/flask_sqlalchemy.py#L363
def first_or_404(self):
    rv = self.first()
    if rv is None:
        abort(404)
    return rv
Base.first_or_404 = first_or_404

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import onetimemsg.models
    Base.metadata.create_all(bind=engine)

# @see: http://flask.pocoo.org/docs/patterns/sqlalchemy/
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()