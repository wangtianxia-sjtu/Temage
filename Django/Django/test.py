from django.test import TestCase
from Temage.models import User
from django.contrib.auth import authenticate
from django.test.client import Client

# Create your tests here.
class ModelTest(TestCase):
# Test Set Up
    def setUp(self):
        User.objects.create_user(id=1,username=1234, is_superuser=True, email='1234@qq.com', password="1234")
        User.objects.create_user(username="qxy", password="123")

#  用例编号: 001{前端} 101{后端}
#  测试单元描述: {{测试文件中文}}
#  用例目的: {{带数据实例的过程描述}}
#  前提条件: {{数据背景，环境要求}}
#  特殊的规程说明: {{无， or必须的流程}}
#  用例间的依赖关系: {{多个用例测试之间的关系}}
#  具体流程:
#     步骤1
#         输入:
# 		  期望输出:
# 		  实际输出:
# 		  备注:
#     步骤2
#         ······
#  测试结果综合分析及建议:
#  测试经验总结:

    def test_superuser(self):
        super_user = User.objects.filter(is_superuser=True)
        print(super_user)
        self.assertEqual(len(super_user),1)


#  用例编号: 101
#  测试单元描述: 登录功能测试
#  用例目的: 测试login登录功能
#  前提条件: 数据库中已存在username="qxy", password="123"的用户
#  特殊的规程说明: 无
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: username="qxy"、password="123"
# 		  期望输出: 正确码"200"
# 		  实际输出: "200"
# 		  备注: 无
#  测试结果综合分析及建议: Succeed
#  测试经验总结: 无
    def test_login(self):
        c = Client()
        response = c.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        print(response)
        self.assertEqual(response.content.decode('utf-8'), '\"201\"')
