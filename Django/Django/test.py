from django.test import TestCase
from Temage.models import User
from Temage.models import Profile
from Temage.models import Style
from Temage.models import Collection
from Temage.models import Product
from Temage.models import Theme
from Temage.models import Card
from django.contrib.auth import authenticate
from django.test.client import Client
from django.core.files import File

# Create your tests here.
class ModelTest(TestCase):
# Test Set Up
    def setUp(self):
        img1 = open("../test_file/img/good.jpg", "rb")
        img2 = open("../test_file/img/bad.jpg", "rb")
        User.objects.create_user(id=1,username=1234, is_superuser=True, email='1234@qq.com', password="1234")
        user1 = User.objects.create_user(username="qxy", password="123", id=1)
        user2 = User.objects.create_user(username="wxm", password="123")
        style1 = Style.objects.create(name="style_1")
        style2 = Style.objects.create(name="style_2", id=2)
        theme1 = Theme.objects.create(name="theme_1", id=1)
        theme2 = Theme.objects.create(name="theme_2", id=2)
        profile1 = Profile.objects.create(user = user1, phone = "+8618217508975", sex = 1)
        profile2 = Profile.objects.create(user = user2, phone = "+8612334443223", sex = 0)
        profile1.interest.add(theme1)
        profile1.interest.add(theme2)
        product1 = Product.objects.create(title="product_1", html="<p>good day</p>", creator=profile1,style=style1, score=0.1)
        product2 = Product.objects.create(title="product_2", html="<p>bad day</p>", creator=profile1,style=style2, score=0.9)
        product1.imag.save('good.jpg', File(img1), save=True)
        product2.imag.save('bad.jpg', File(img2), save=True)
        product1.theme.add(theme1)
        product2.theme.add(theme2)
        card1 = Card.objects.create(product=product1, url="http://temage/goodday", title="positive", prompt="A positive people said...")
        card2 = Card.objects.create(product=product2, url="http://temage/goodday", title="negative", prompt="A negative people said...")
        collection = Collection.objects.create(name = "quote", user=profile1)
        collection.cards.add(card1)
        collection.cards.add(card2)

        

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
#  测试单元描述: 测试model
#  用例目的: 测试model能否正常工作
#  前提条件: 通过数据库操作创建相应的带有相互关系的对象们
#  特殊的规程说明: 通过对象间的关系输出用于前端显示的json
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 一个包含所需信息的json字符串
# 		  实际输出:
# 		  备注:
#     步骤2
#         ······
#  测试结果综合分析及建议:
#  测试经验总结:

    def test_api(self):
        c = Client()
        response = c.get('/api/')
        print(response.content)
        self.assertEqual(response.content, '\{\}')

#  用例编号: 102
#  测试单元描述: 测试model
#  用例目的: 测试model能否正常工作
#  前提条件: 通过数据库操作创建相应的带有相互关系的对象们
#  特殊的规程说明: 通过对象间的关系输出用于前端显示的json
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 一个包含所需信息的json字符串
# 		  实际输出:
# 		  备注:
#     步骤2
#         ······
#  测试结果综合分析及建议:
#  测试经验总结:

    def test_api(self):
        c = Client()
        response = c.get('/api/')
        print(response.content)
        self.assertEqual(response.content, '\{\}')




#  用例编号: 102
#  测试单元描述: 登录功能测试
#  用例目的: 测试login登录功能
#  前提条件: 数据库中已存在username="qxy", password="123"的用户
#  特殊的规程说明: 无
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: {username:"qxy", password:"123"}
# 		  期望输出: status_code = 200
# 		  实际输出: "200"
# 		  备注: 无
#  测试结果综合分析及建议: Succeed
#  测试经验总结: 无
    def test_login(self):
        c = Client()
        response = c.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        self.assertEqual(response.status_code, 200)

