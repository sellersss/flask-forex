from forex_python.converter import CurrencyRates, CurrencyCodes

"""Python Forex Methods"""
cr = CurrencyRates()
cc = CurrencyCodes()


def currency_code_check(currency_code):
    """Get currency name from code"""

    return cc.get_currency_name(currency_code) is not None


def currency_rate(c_from, c_to, amt):
    """Convert currency rate"""

    res = round(cr.convert(c_from, c_to, amt), 2)
    return res


def currency_code(c_to):
    """Get currency code"""

    res = cc.get_symbol(c_to)
    return res