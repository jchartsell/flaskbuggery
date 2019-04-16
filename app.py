from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<who>')
def index(who="foo"):
    query = request.args.get('person', who)
    return render_template("index.html", name=query)

@app.route('/powerlevel/')
@app.route('/powerlevel/<int:pl>')
def power_level_over_9000(pl=None):
    if type(pl) != int or pl == None:
        over = "check integer as power level at /powerlevel/<integer>"
    elif pl > 9000:
        over = "It's over 9000!"
    else:
        over = "Nope."
    return render_template("powerlevel.html", over=over)




app.run(debug=True, port=8080, host='0.0.0.0')