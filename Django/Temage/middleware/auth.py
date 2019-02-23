#-*-coding:utf-8-*-
from django.http import JsonResponse
import jwt
from Temage.models import User
class TokenMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
 
    def __call__(self, request):
        response = self.get_response(request)
        print("中间件结束")
        return response
 
    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path
        print(path)
        if (path == '/login/submit/' or path == '/register/' or path == '/admin/' or path=='/admin/login/'):
            return None
        token = request.META.get("HTTP_AUTHORIZATION")
        if token:
            payload = jwt.decode(token, "Temage")
            # print(payload)
            user = User.objects.get(id=payload['id'])
            if user.username != payload['name']:
                return JsonResponse({"msg":"Invalid Token", "code": 400})
            return None
        return JsonResponse({"msg":"No token", "code": 400})
        
    '''
    def process_exception(self, request, exception):
        print("程序异常时执行")
        return JsonResponse({"msg": exception.args[0], "code": -1})
    '''
    

        