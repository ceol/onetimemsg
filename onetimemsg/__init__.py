from flask import escape, Flask, Markup, render_template
from werkzeug.routing import BaseConverter
import markdown2

app = Flask(__name__)
app.config.from_object('onetimemsg.settings')

# @see: http://stackoverflow.com/a/5872904
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]
app.url_map.converters['regex'] = RegexConverter

@app.template_filter('markdown')
def markdown(s):
    return Markup(markdown2.markdown(escape(s)))

# @see: http://flask.pocoo.org/docs/patterns/packages/#simple-packages
from onetimemsg.views import *

if __name__ == '__main__':
    app.run()