from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index(default="foo"):
    query = request.args.get('query', default)
    return "Word to your mother, {}.".format(query)

@app.route('/powerlevel/')
@app.route('/powerlevel/<int:pl>')
def power_level_over_9000(pl):
    if pl > 9000:
        return "It's over 9000!"
    #elif pl == 'None':
        #return "check PL at /powerlevel/(your PL here)"
    else:
        return "Nope."




app.run(debug=True, port=8080, host='0.0.0.0')