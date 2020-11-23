from flask import Flask, render_template, flash, request, session
from conversion import currency_code_check, currency_rate, currency_code
from forex_python.converter import RatesNotAvailableError
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SECRET_KEY"] = "not0so0secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    """Renders homepage"""

    return render_template("home.html")


@app.route("/res", methods=["POST"])
def res_page():
    """Render results via post request"""

    err = []
    c_from = request.form["c_from"].upper()
    c_to = request.form["c_to"].upper()
