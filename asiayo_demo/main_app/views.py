from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from common.decorators import KeyCheck
from common.helperfunc import api_response
from common import errorcode
from main_app.functions import convert_currency

key_check_ = KeyCheck(SystemName='api')

class ConvertCurrency(APIView):
    permission_classes = (IsAuthenticated,)
    
    required_data = ['source', 'target', 'amount']
    @key_check_.key_check(required_data)
    @swagger_auto_schema(
        operation_summary='匯率轉換',
        operation_description='匯率轉換API，轉換金額請四捨五入到小數點第二位，且轉換後的金額顯示格式以逗點分隔做為千分位表示。',
        responses = {'200': openapi.Response(
            description = 'message',
            examples={
                'application/json':{
                    "msg": "success",
                    "amount": "$111,801.00",
                    "code": 0
                }
            }
        )},
        manual_parameters=[
            openapi.Parameter(
                name='source',
                in_=openapi.IN_QUERY,
                description='source',
                type=openapi.TYPE_STRING,
                default='USD',
                required = True
            ),
            openapi.Parameter(
                name='target',
                in_=openapi.IN_QUERY,
                description='target',
                type=openapi.TYPE_STRING,
                default='JPY',
                required = True
            ),
            openapi.Parameter(
                name='amount',
                in_=openapi.IN_QUERY,
                description='amount',
                type=openapi.TYPE_STRING,
                default= '$1,525',
                required = True
            )
        ]
    )
    def get(self, request, input_data, router):
        '''
        param:
            必填欄位：
                source, target, amount
            非必填欄位：
                -
        '''
        source = input_data.get('source')
        target = input_data.get('target')
        amount = input_data.get('amount')
        code, ret = convert_currency(source, target, amount)
        if code != errorcode.OK:
            return api_response(ret, code=code)
        return api_response(ret)
 