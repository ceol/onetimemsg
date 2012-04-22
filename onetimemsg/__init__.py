from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)
app.config.from_object('onetimemsg.settings')

# @see: http://stackoverflow.com/a/5872904
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]
app.url_map.converters['regex'] = RegexConverter

# @see: http://flask.pocoo.org/docs/patterns/packages/#simple-packages
import onetimemsg.views

if __name__ == '__main__':
    app.run()