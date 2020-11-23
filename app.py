from flask import Flask, render_template, flash, request, redirect
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

    try:
        amt = int(request.form["amt"])
        res = currency_rate(c_from, c_to, amt)

    # error handling
    except (TypeError, ValueError, RatesNotAvailableError):

        # handle if number is NaN
        err.append(f"Is the amount a real number?")

        if not currency_code_check(c_from):
            # handle converting from an invalid code
            err.append(f'"{c_from}" is not a valid currency code!')

        if not currency_code_check(c_to):
            # handle converting to an invalid code
            err.append(f'"{c_to}" is not a valid currency code!')

        # for any error returned store in msg
        if err:
            for error in err:
                flash(error, "msg")

        return redirect("/")

    code = currency_code(c_to)
    return render_template("res.html", res=res, code=code)