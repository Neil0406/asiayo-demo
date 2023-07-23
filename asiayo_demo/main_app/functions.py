import re
from common import errorcode
from demo_source.currency_data import currency_data

def convert_currency(from_currency, to_currency, amount):
    code = errorcode.OK
    converted_amount = None
    msg = 'success'
    try:
        amount = float(re.sub("[$, ]", "", str(amount)))
        if from_currency not in currency_data["currencies"] or to_currency not in currency_data["currencies"]:
            code =errorcode.DATA_NOT_EXISTS
            msg = "Invalid currency codes"
            return code, {"msg": msg, "amount": converted_amount}

        if amount <= 0:
            code = errorcode.INPUT_ERROR
            msg = "Invalid amount"
            return code, {"msg": msg, "amount": converted_amount}
        
        conversion_rate = currency_data["currencies"][from_currency][to_currency]
        converted_amount = amount * conversion_rate
        converted_amount = f"${converted_amount:,.2f}"
        return code, {"msg": "success", "amount": converted_amount}
    except ValueError as v:
        code = errorcode.INPUT_TYPE_ERROR
        return code, {"msg": str(v), "amount": converted_amount}
    
