from django.test import TestCase
from main_app.functions import convert_currency
from decimal import Decimal, ROUND_HALF_UP
import re
from common import errorcode

class ConvertCurrencyTestCase(TestCase):
    def test_valid_conversion(self):
        # 有效匯率轉換
        from_currency = "USD"
        to_currency = "JPY"
        amount = 1525
        expected_amount = Decimal(str(amount)) * Decimal(str(111.801))                        #Python浮點數精確度問題處理
        expected_amount = expected_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        code, result = convert_currency(from_currency, to_currency, amount)
    
        self.assertEqual(code, 0)
        self.assertEqual(result["msg"], "success")
        self.assertEqual(result["amount"], f"${expected_amount:,.2f}")

    def test_valid_conversion_str(self):
        # 有效匯率轉換(字串input)
        from_currency = "USD"
        to_currency = "JPY"
        amount = '$1,525 '
        amount = float(re.sub("[$, ]", "", str(amount)))
        expected_amount = Decimal(str(amount)) * Decimal(str(111.801))                        #Python浮點數精確度問題處理
        expected_amount = expected_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        code, result = convert_currency(from_currency, to_currency, amount)
        self.assertEqual(code, 0)
        self.assertEqual(result["msg"], "success")
        self.assertEqual(result["amount"], f"${expected_amount:,.2f}")

    def test_invalid_currency_codes(self):
        # 無效貨幣
        from_currency = "EUR"
        to_currency = "USD"
        amount = 500

        code, result = convert_currency(from_currency, to_currency, amount)
        self.assertEqual(code, errorcode.DATA_NOT_EXISTS)
        self.assertEqual(result["msg"], "Invalid currency codes")

    def test_invalid_amount(self):
        # 無效金额
        from_currency = "USD"
        to_currency = "TWD"
        amount = -100

        code, result = convert_currency(from_currency, to_currency, amount)

        self.assertEqual(code, errorcode.INPUT_ERROR)
        self.assertEqual(result["msg"], "Invalid amount")

    def test_input_type_error(self):
        # 數入類型錯誤
        from_currency = "TWD"
        to_currency = "USD"
        amount = "abc"

        code, result = convert_currency(from_currency, to_currency, amount)
        self.assertEqual(code, errorcode.INPUT_TYPE_ERROR)
        self.assertEqual(result["msg"], "could not convert string to float: 'abc'")

