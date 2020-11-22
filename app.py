from flask import Flask, render_template, flash, request, session
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError
from flask_debugtoolbar import DebugToolbarExtension, FlaskDebugToolbar

app = Flask(__name__)

app.config["SECRET_KEY"] = "not0so0secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

c = CurrencyRates()
c.get_rates("USD")
