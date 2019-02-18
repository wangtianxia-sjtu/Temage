#coding=utf-8
from django.test import TestCase
from Temage.models import User
from Temage.models import Profile
from Temage.models import Style
from Temage.models import Collection
from Temage.models import Product
from Temage.models import Theme
from Temage.models import Card
from django.contrib.auth import authenticate
from django.core.files import File
import jwt
import json

# global variable of html string for test
htmlmessi = '<p> Messi is Back! </p>'

# Create your tests here.
class ModelTest(TestCase):
# Test Set Up
    def setUp(self):
        img1 = open("../test_file/img/good.jpg", "rb")
        img2 = open("../test_file/img/bad.jpg", "rb")
        img3 = open("../test_file/img/cold.jpg", "rb")
        img4 = open("../test_file/img/hot.jpg", "rb")
        avator1 = open("../test_file/img/girl.jpg", "rb")
        avator2 = open("../test_file/img/boy.jpg", "rb")
        User.objects.create_user(id=1,username=1234, is_superuser=True, email='1234@qq.com', password="1234")
        user1 = User.objects.create_user(username="qxy", password="123", id=2)
        user2 = User.objects.create_user(username="wxm", password="123")
        style1 = Style.objects.create(name="style_1")
        style2 = Style.objects.create(name="style_2")
        style3 = Style.objects.create(name="style_4")
        style4 = Style.objects.create(name="style_5")
        style5 = Style.objects.create(name="style_6")
        style6 = Style.objects.create(name="style_7")
        style7 = Style.objects.create(name="style_8")
        style8 = Style.objects.create(name="style_9")
        style9 = Style.objects.create(name="style_a")
        style10 = Style.objects.create(name="style_b")
        style11 = Style.objects.create(name="style_c")
        style12 = Style.objects.create(name="style_d")
        style13 = Style.objects.create(name="style_e")
        style14 = Style.objects.create(name="style_f")
        style15 = Style.objects.create(name="style_g")
        style16 = Style.objects.create(name="style_h")
        style17 = Style.objects.create(name="style_i")
        style18 = Style.objects.create(name="style_j")
        style19 = Style.objects.create(name="style_k")
        style20 = Style.objects.create(name="style_l")
        theme1 = Theme.objects.create(name="Sports", id=1)
        theme2 = Theme.objects.create(name="Art", id=2)
        theme3 = Theme.objects.create(name="Tech", id=3)
        theme4 = Theme.objects.create(name="Movie", id=4)                      
        theme5 = Theme.objects.create(name="Porn", id=5)
        theme6 = Theme.objects.create(name="Celebrity", id=6)
        profile1 = Profile.objects.create(user = user1)
        profile2 = Profile.objects.create(user = user2)
        profile1.avator.save('girl.jpg', File(avator1), save=True)
        profile2.avator.save('boy.jpg', File(avator2), save=True)
        profile1.theme.add(theme1)
        profile1.theme.add(theme2)
        profile1.theme.add(theme3)
        product1 = Product.objects.create(title="product_1", html="<p>good day</p>", creator=profile1,style=style1, score=0.1, id=11, width=400)
        product2 = Product.objects.create(title="product_2", html="<p>bad day</p>", creator=profile1,style=style2, score=0.9, id=12, width=400)
        product3 = Product.objects.create(title="product_3", html="<p>cold day</p>", creator=profile1,style=style4, score=0.8, id=13, width=400)
        product4 = Product.objects.create(title="product_4", html="<p>hot day</p>", creator=profile1,style=style5, score=0.7, id=14, width=400)
        product5 = Product.objects.create(title="product_5", html="<p>hot day</p>", creator=profile1,style=style6, score=0.7, id=15, width=400)
        product6 = Product.objects.create(title="product_6", html="<p>hot day</p>", creator=profile1,style=style7, score=0.7, id=16, width=400)
        product7 = Product.objects.create(title="product_7", html="<p>hot day</p>", creator=profile1,style=style8, score=0.7, id=17, width=400)
        product8 = Product.objects.create(title="Messi is Back!", html = htmlmessi, creator=profile1,style=style10, score=0.9, id=18, width=400)
        product1.imagesrc.save('good.jpg', File(img1), save=True)
        product2.imagesrc.save('bad.jpg', File(img2), save=True)
        product3.imagesrc.save('cold.jpg', File(img3), save=True)
        product4.imagesrc.save('hot.jpg', File(img4), save=True)
        product5.imagesrc.save('hot.jpg', File(img4), save=True)
        product6.imagesrc.save('hot.jpg', File(img4), save=True)
        product7.imagesrc.save('hot.jpg', File(img4), save=True)
        product8.imagesrc.save('hot.jpg', File(img4), save=True)
        product1.theme.add(theme1)
        product1.theme.add(theme2)
        product2.theme.add(theme2)
        product8.theme.add(theme1)
        product8.theme.add(theme6)
        card1 = Card.objects.create(creator=profile1, product=product1, title="positive", prompt="A positive people said...", head="head content", foottext="foot content", id=1)
        card2 = Card.objects.create(creator=profile1, product=product2, title="negative", prompt="A negative people said...", head="head content", foottext="foot content")
        card3 = Card.objects.create(creator=profile1, product=product3, title="cold", prompt="A cold people said...", head="head content", foottext="foot content")
        card4 = Card.objects.create(creator=profile1, product=product4, title="hot", prompt="A hot people said...", head="head content", foottext="foot content")
        card5 = Card.objects.create(creator=profile1, product=product5, title="hot", prompt="A hot people said...", head="head content", foottext="foot content")
        card6 = Card.objects.create(creator=profile1, product=product6, title="hot", prompt="A hot people said...", head="head content", foottext="foot content")
        card7 = Card.objects.create(creator=profile1, product=product7, title="hot", prompt="A hot people said...", head="head content", foottext="foot content")
        card8 = Card.objects.create(creator=profile1, product=product8, title = "Messi is Back!", prompt="Messi the Best", head="head content", foottext="foot content", id=10086)
        collection1 = Collection.objects.create(name = "quote", user=profile1, id=1)
        collection1.cards.add(card1)
        collection1.cards.add(card2)
        collection1.cards.add(card3)
        collection1.cards.add(card4)
        collection2 = Collection.objects.create(name="requote", user=profile1)
        collection2.cards.add(card1)
    

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

    def testSuperuser(self):
        super_user = User.objects.filter(is_superuser=True)
        self.assertEqual(len(super_user),1)


#  用例编号: 101
#  测试单元描述: 测试Models的多态多对多关系
#  用例目的: 测试model多态多对多关系能否正常工作
#  前提条件: 通过数据库操作创建相应的带有多态多对多关系的对象们
#  特殊的规程说明: Profile与Product的对象可以同时拥有同一个Theme，且它们分别与Theme成多对多关系
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: user和第一个product拥有同一个theme
# 		  实际输出: 两者的theme相等
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testPolymorphicManytomany(self):
        user = Profile.objects.get(user__username='qxy')
        themelist_of_user = user.theme.all().values('name')
        list1 = list(themelist_of_user)
        themelist_of_product = Product.objects.get(id=11).theme.all().values('name')
        list2 = list(themelist_of_product)
        self.assertEqual(list1[0]['name'], list2[0]['name'])


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
    def testLogin(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        self.assertEqual(response.status_code, 200)

#  用例编号: 103
#  测试单元描述: 测试api接口
#  用例目的: 测试给前端/api返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 用户需要先登录才能获取这些信息
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request
# 		  期望输出: 有三个元素的list
# 		  实际输出: 有三个元素的list
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApi(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        self.assertEqual(len(responseList), 4)

#  用例编号: 104
#  测试单元描述: 测试/api/work接口
#  用例目的: 测试给前端/api/work返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 用户需要先登录才能获取这些信息
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request，work的id
# 		  期望输出: 所有的style的数据和该work的html内容
# 		  实际输出: 所有的style的数据和该work的html内容
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApiWork(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/work/11/', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        self.assertEqual(len(responseList), 3)

#  用例编号: 105
#  测试单元描述: 测试api接口
#  用例目的: 测试给前端/api/collection返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 用户需要先登录才能获取这些信息
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request
# 		  期望输出: collection的内容
# 		  实际输出: collection的内容
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApiCollection(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/collection/', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        self.assertEqual(len(responseList[0]), 6)

#  用例编号: 106
#  测试单元描述: 测试api/recent接口
#  用例目的: 测试给前端/api/recent返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 用户需要先登录才能获取这些信息
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request
# 		  期望输出: 七张card
# 		  实际输出: 七张card
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApiRecent(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/recent/', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        self.assertEqual(len(responseList), 4)


#  用例编号: 107
#  测试单元描述: 测试register接口
#  用例目的: 测试用户注册功能
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 无
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 注册成功状态码“200”
# 		  实际输出: “200”
# 		  备注: 
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testRegister(self):
        response = self.client.post('/register/',  {'password': '123', 'username': 'tmg','email': '123123@qq.com','interest': ['Porn','Sports'],'desc': 'love and peace'}, content_type="application/json")
        self.assertEqual(response.status_code, 200)

#  用例编号: 108
#  测试单元描述: 测试/api/gallery接口
#  用例目的: 测试/api/gallery返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 需登陆后操作
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request
# 		  期望输出: 返回相应gallery数据
# 		  实际输出：返回了相应的gallery数据
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApiGallery(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/gallery/', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        self.assertEqual(len(responseList), 7)

#  用例编号: 109
#  测试单元描述: 测试/api/gallery/more_cards接口
#  用例目的: 测试/api/gallery/more_cards返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 需登陆后操作
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request
# 		  期望输出: 随机返回4条gallery数据
# 		  实际输出: 随机返回4条gallery数据
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApiGalleryMoreCard(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/gallery/more_cards/', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        self.assertEqual(len(responseList), 4)

#  用例编号: 110
#  测试单元描述: 测试/api/text接口
#  用例目的: 测试/api/text返回的数据是否符合规范
#  前提条件: 通过数据库操作创建相应的对象们
#  特殊的规程说明: 需登陆后操作
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: 无
# 		  期望输出: 登录后response中带有身份象征的token，token解码后id为2
# 		  实际输出: id为2
# 		  备注: 根据setup的改动，id可能有所变动
#     步骤2
#         输入: 带有步骤1中token的request
# 		  期望输出: 返回所请求的card的信息
# 		  实际输出: 返回所请求的card的信息
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def testApiText(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/text/', {'id' : '10086'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        self.assertEqual(responseList['id'], '10086')


    def testStorePassage(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/store_passage/', {'styles' : ['Porn','Sports'], 'res_html': htmlmessi, 'title': 'Messi is Back!', 't_width': '200'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        print(responseList)

    def testFinishedWork(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/finished_work/', {'workID': '11'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        print("testFinished")
        print(responseList)

    def testDownload(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/download/', {'workID': '11'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        print(responseList)

    def testConfirmStore(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/confirm_store/', {'workID': '11', 'stars': '4.5'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        print(responseList)

    def testDestroy(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/destroy/', {'workID': '11'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        print(responseList)

    def testCollect(self):
        response = self.client.post('/login/submit/', {'username': 'qxy', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/collect/', {'id': '10086'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content)
        print(responseList)