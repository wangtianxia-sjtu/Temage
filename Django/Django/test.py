#-*-coding:utf-8-*-
from django.test import TestCase
from Temage.models import User
from Temage.models import Profile
from Temage.models import Style
from Temage.models import Collection
from Temage.models import Product
from Temage.models import Theme
from Temage.models import Card
from Temage.models import Cache
from django.contrib.auth import authenticate
from django.core.files import File
import jwt
import json
from django.core.files.base import ContentFile

# global variable of html string for test
htmlmessi = '<p> Messi is Back! </p>'

# Create your tests here.
class ModelTest(TestCase):
# Test Set Up
    def setUp(self):
        img1 = open("./test_file/img/good.jpg", "rb")
        img2 = open("./test_file/img/bad.jpg", "rb")
        img3 = open("./test_file/img/cold.jpg", "rb")
        img4 = open("./test_file/img/hot.jpg", "rb")
        avator1 = open("./test_file/img/girl.jpg", "rb")
        avator2 = open("./test_file/img/boy.jpg", "rb")
        style_file1 = open("./test_file/css/style1.css", "rb")
        style_file2 = open("./test_file/css/style2.css", "rb")
        style_file3 = open("./test_file/css/style3.css", "rb")
        style_file4 = open("./test_file/css/style4.css", "rb")
        User.objects.create_user(id=1,username=1234, is_superuser=True, email='1234@qq.com', password="1234")
        user1 = User.objects.create_user(username="user1", password="123", id=2)
        user2 = User.objects.create_user(username="user2", password="123")
        theme1 = Theme.objects.create(name="constellation", id=1)
        theme2 = Theme.objects.create(name="economics", id=2)
        theme3 = Theme.objects.create(name="education", id=3)
        theme4 = Theme.objects.create(name="entertainment", id=4)                      
        theme5 = Theme.objects.create(name="fashion", id=5)
        theme6 = Theme.objects.create(name="furniture", id=6)
        theme7 = Theme.objects.create(name="game", id=7)
        theme8 = Theme.objects.create(name="lottery", id=8)
        theme9 = Theme.objects.create(name="politics", id=9)
        theme10 = Theme.objects.create(name="real-estate", id=10)                      
        theme11 = Theme.objects.create(name="science-technology", id=11)
        theme12 = Theme.objects.create(name="society", id=12)
        theme13 = Theme.objects.create(name="sport", id=13)
        theme14 = Theme.objects.create(name="stock", id=14)
        theme15 = Theme.objects.create(name="NONE", id=15)
        style1 = Style.objects.create(name="style1")
        style2 = Style.objects.create(name="style2")
        style3 = Style.objects.create(name="style3")
        style4 = Style.objects.create(name="style4")
        style1.css.save('style1.css', File(style_file1), save=True)
        style2.css.save('style2.css', File(style_file1), save=True)
        style3.css.save('style3.css', File(style_file1), save=True)
        style4.css.save('style4.css', File(style_file1), save=True)
        
        theme1.styles.add(style4)
        theme2.styles.add(style4)
        theme3.styles.add(style1)
        theme4.styles.add(style1)
        theme5.styles.add(style2)
        theme6.styles.add(style4)
        theme7.styles.add(style4)
        theme8.styles.add(style2)
        theme9.styles.add(style4)
        theme10.styles.add(style4)
        theme11.styles.add(style3)
        theme12.styles.add(style3)
        theme13.styles.add(style1)
        theme14.styles.add(style3)
        theme15.styles.add(style3)

        profile1 = Profile.objects.create(user = user1)
        # cache = Cache.objects.create(user = profile1)
        profile2 = Profile.objects.create(user = user2)
        profile1.avator.save('girl.jpg', File(avator1), save=True)
        profile2.avator.save('boy.jpg', File(avator2), save=True)
        profile1.theme.add(theme1)
        profile1.theme.add(theme2)
        profile1.theme.add(theme3)
        product1 = Product.objects.create(title="product_1", html="<p>good day</p>", creator=profile1, score=0.1, id=11, width=400)
        product2 = Product.objects.create(title="product_2", html="<p>bad day</p>", creator=profile1, score=0.9, id=12, width=400)
        product3 = Product.objects.create(title="product_3", html="<p>cold day</p>", creator=profile1, score=0.8, id=13, width=400)
        product4 = Product.objects.create(title="product_4", html="<p>hot day</p>", creator=profile1, score=0.7, id=14, width=400)
        product5 = Product.objects.create(title="product_5", html="<p>hot day</p>", creator=profile1, score=0.7, id=15, width=400)
        product6 = Product.objects.create(title="product_6", html="<p>hot day</p>", creator=profile1, score=0.7, id=16, width=400)
        product7 = Product.objects.create(title="product_7", html="<p>hot day</p>", creator=profile1, score=0.7, id=17, width=400)
        product8 = Product.objects.create(title="Messi is Back!", html = htmlmessi, creator=profile1, score=0.9, id=18, width=400)
        product8.html_file.save("html_18.html", ContentFile(htmlmessi))
        product1.image_src.save('good.jpg', File(img1), save=True)
        product2.image_src.save('bad.jpg', File(img2), save=True)
        product3.image_src.save('cold.jpg', File(img3), save=True)
        product4.image_src.save('hot.jpg', File(img4), save=True)
        product5.image_src.save('hot.jpg', File(img4), save=True)
        product6.image_src.save('hot.jpg', File(img4), save=True)
        product7.image_src.save('hot.jpg', File(img4), save=True)
        product8.image_src.save('hot.jpg', File(img4), save=True)
        product1.theme.add(theme1)
        product1.theme.add(theme2)
        product2.theme.add(theme2)
        product8.theme.add(theme1)
        product8.theme.add(theme6)
        product3.theme.add(theme1)
        product4.theme.add(theme2)
        product5.theme.add(theme2)
        product6.theme.add(theme1)
        product7.theme.add(theme6)
        card1 = Card.objects.create(creator=profile1, product=product1, title="positive", prompt="A positive people said...", head="head content", foot_text="foot content")
        card2 = Card.objects.create(creator=profile1, product=product2, title="negative", prompt="A negative people said...", head="head content", foot_text="foot content")
        card3 = Card.objects.create(creator=profile1, product=product3, title="cold", prompt="A cold people said...", head="head content", foot_text="foot content")
        card4 = Card.objects.create(creator=profile1, product=product4, title="hot", prompt="A hot people said...", head="head content", foot_text="foot content")
        card5 = Card.objects.create(creator=profile1, product=product5, title="hot", prompt="A hot people said...", head="head content", foot_text="foot content")
        card6 = Card.objects.create(creator=profile1, product=product6, title="hot", prompt="A hot people said...", head="head content", foot_text="foot content")
        card7 = Card.objects.create(creator=profile1, product=product7, title="hot", prompt="A hot people said...", head="head content", foot_text="foot content")
        card8 = Card.objects.create(creator=profile1, product=product8, title = "Messi is Back!", prompt="Messi the Best", head="head content", foot_text="foot content")
        collection = Collection.objects.create(name = "quote", user=profile1)
        collection.cards.add(card1)
        collection.cards.add(card2)
        collection.cards.add(card3)
        collection.cards.add(card4)
        cache1 = Cache.objects.create(imgs_urls="[]", title="小明与小红", text="[\"我是小明，我今天会去买菜,买菜当然是最吼的呀\", \"我是小红，我今天要去钓鱼,我觉得我可以钓到大的。\"]", match_list="[]", user = profile1)
    

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

    def test_polymorphic_manytomany(self):
        user = Profile.objects.get(user__username='user1')
        themelist_of_user = user.theme.all().values('name')
        list1 = list(themelist_of_user)
        themelist_of_product = Product.objects.get(id=11).theme.all().values('name')
        list2 = list(themelist_of_product)
        self.assertEqual(list1[0]['name'], list2[0]['name'])


#  用例编号: 102
#  测试单元描述: 登录功能测试
#  用例目的: 测试login登录功能
#  前提条件: 数据库中已存在username="user1", password="123"的用户
#  特殊的规程说明: 无
#  用例间的依赖关系: 无
#  具体流程:
#     步骤1
#         输入: {username:"user1", password:"123"}
# 		  期望输出: status_code = 200
# 		  实际输出: "200"
# 		  备注: 无
#  测试结果综合分析及建议: Succeed
#  测试经验总结: 无
    def test_login(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        self.assertEqual(response.status_code, 200)


#  用例编号: 103
#  测试单元描述: 测试/api/explore/接口
#  用例目的: 测试给前端/api/explore/返回的数据是否符合规范
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
# 		  期望输出: 有四个元素（四种信息）的list
# 		  实际输出: 有四个元素（四种信息）的list
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def test_api_explore(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/explore/', HTTP_AUTHORIZATION=token)
        self.assertEqual(responseAPI.status_code, 200)
        responseList = json.loads(responseAPI.content.decode('utf-8'))
        self.assertEqual(len(responseList), 4)


#  用例编号: 104
#  测试单元描述: 测试/api/explore/product接口
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
# 		  期望输出: product所需的四种信息
# 		  实际输出: product所需的四种信息
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def test_product(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/explore/product/', {'productID': '11'}, HTTP_AUTHORIZATION=token, content_type="application/json")
        responseList = json.loads(responseAPI.content.decode('utf-8'))
        self.assertEqual(responseList['id'], '11')


#  用例编号: 105
#  测试单元描述: 测试api接口
#  用例目的: 测试给前端/api/explore/collection返回的数据是否符合规范
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
# 		  期望输出: collection中的六张卡片内容
# 		  实际输出: collection中的六张卡片内容
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def test_collection(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/explore/collection/', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content.decode('utf-8'))
        self.assertEqual(len(responseList[0]), 6)


#  用例编号: 106
#  测试单元描述: 测试/api/explore/get_recent/接口
#  用例目的: 测试给前端/api/explore/get_recent/返回的数据是否符合规范
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
# 		  期望输出: 最近修改的四个work的信息
# 		  实际输出: 最近修改的四个work的信息
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    def test_recent(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/explore/get_recent/', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content.decode('utf-8'))
        self.assertEqual(len(responseList), 4)


#  用例编号: 107
#  测试单元描述: 测试/api/user/register/接口
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

    def test_register(self):
        response = self.client.post('/api/user/register/',  {'password': '123', 'username': 'tmg','email': '123123@qq.com','interest': ['society','sport'],'desc': 'love and peace'}, content_type="application/json")
        self.assertEqual(response.status_code, 200)


#  用例编号: 108
#  测试单元描述: 测试/api/explore/gallery/接口
#  用例目的: 测试/api/explore/gallery/返回的数据是否符合规范
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

    def test_gallery(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/explore/gallery/', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content.decode('utf-8'))
        self.assertEqual(len(responseList), 7)


#  用例编号: 109
#  测试单元描述: 测试/api/explore/gallery/more_cards接口
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

    def test_gallery_more_card(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.get('/api/explore/gallery/more_cards/', HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content.decode('utf-8'))
        self.assertEqual(len(responseList), 4)


#  用例编号: 110
#  测试单元描述: 测试/api/workflow/store_passage接口
#  用例目的: 测试/api/workflow/store_passage初步存储数据是否成功
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
# 		  期望输出: 返回创建的作品的id和状态码“200”
# 		  实际输出: 状态码和“200”
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:

    # def test_store_passage(self):
    #     response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
    #     token = response.content
    #     payload = jwt.decode(token, "Temage")
    #     payloadID = payload['id']
    #     self.assertEqual(payloadID, 2)
    #     responseAPI = self.client.post('/api/workflow/store_passage/', {'styles' : ['society','sport'], 'res_html': htmlmessi, 'title': 'Messi is Back!', 't_width': '200'}, content_type="application/json", HTTP_AUTHORIZATION=token)
    #     responseList = json.loads(responseAPI.content.decode('utf-8'))
    #     self.assertEqual(len(responseList), 1)
    #     self.assertEqual(responseAPI.status_code, 200)


#  用例编号: 111
#  测试单元描述: 测试/api/workflow/finished_work接口
#  用例目的: 测试/api/workflow/finished_work返回预览信息是否正确
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
#         输入: 带有步骤1中token的request，和当前处理的product的id
# 		  期望输出: 返回作品的html文件路径，和生成图片的宽度
# 		  实际输出: 作品html的url和宽度width=400
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:
    def test_finished_work(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/workflow/finished_work/', {'productID': '18'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content.decode('utf-8'))
        self.assertEqual(responseList['width'], 400)
        self.assertEqual(responseList['url'][-5:], '.html')


#  用例编号: 112
#  测试单元描述: 测试/api/workflow/download_picture接口
#  用例目的: 测试/api/workflow/download_picture返回的下载信息是否正确
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
#         输入: 带有步骤1中token的request，和需要下载的product的id
# 		  期望输出: 返回下载地址
# 		  实际输出: 返回下载地址
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:
    def test_download(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/workflow/download_picture/', {'productID': '18'}, content_type="application/json", HTTP_AUTHORIZATION=token)


#  用例编号: 113
#  测试单元描述: 测试/api/workflow/confirm_store接口
#  用例目的: 测试/api/workflow/confirm_store的操作是否成功
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
#         输入: 带有步骤1中token的request，还包含最终保存的product的id和用户评分stars
# 		  期望输出: 返回成功状态码200
# 		  实际输出: “200”
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:
    def test_confirm_store(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/workflow/confirm_store/', {'productID': '18', 'stars': '4.5', 'vector': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content.decode('utf-8'))
        self.assertEqual(responseAPI.status_code, 200)


#  用例编号: 114
#  测试单元描述: 测试/api/explore/delete接口
#  用例目的: 测试/api/explore/delete的操作是否成功
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
#         输入: 带有步骤1中token的request，还包含需要删除的product的id
# 		  期望输出: 返回成功状态码200
# 		  实际输出: “200”
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:
    def test_delete(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/explore/delete/', {'productID': '18'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        self.assertEqual(responseAPI.status_code, 200)


#  用例编号: 115
#  测试单元描述: 测试/api/explore/post_collect/接口
#  用例目的: 测试/api/explore/post_collect/的加入收藏夹操作是否成功
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
#         输入: 带有步骤1中token的request，还包含需要加入收藏夹的product的id
# 		  期望输出: 返回成功状态码200
# 		  实际输出: “200”
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:
    def test_collect(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/explore/post_collect/', {'productID': '18'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        self.assertEqual(responseAPI.status_code, 200)


#  用例编号: 116
#  测试单元描述: 测试/api/explore/cancel_collect/接口
#  用例目的: 测试/api/explore/cancel_collect/的操作是否成功
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
#         输入: 带有步骤1中token的request，还包含需要从收藏夹取消的product的id
# 		  期望输出: 返回成功状态码200
# 		  实际输出: “200”
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:
    def test_cancel_collect(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/explore/cancel_collect/', {'productID': '18'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content.decode('utf-8'))
        self.assertEqual(responseAPI.status_code, 402)
        self.client.post('/api/explore/post_collect/', {'productID': '18'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseAPI = self.client.post('/api/explore/cancel_collect/', {'productID': '18'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        responseList = json.loads(responseAPI.content.decode('utf-8'))
        self.assertEqual(responseAPI.status_code, 200)


#  用例编号: 117
#  测试单元描述: 测试/api/explore/cancel_collect/接口
#  用例目的: 测试/api/explore/cancel_collect/的操作是否成功
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
#         输入: 带有步骤1中token的request，还包含需要从收藏夹取消的product的id
# 		  期望输出: 返回成功状态码200
# 		  实际输出: “200”
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:
    def test_post_search(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/explore/post_search/', {'keywords':'xxx'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        self.assertEqual(responseAPI.status_code, 200)



#  用例编号: 118
#  测试单元描述: 测试/api/workflow/post_text/接口
#  用例目的: 测试/api/workflow/post_text/的操作是否成功
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
#         输入: 带有步骤1中token的request，上传的文字
# 		  期望输出: 返回成功状态码200
# 		  实际输出: “200”
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:
    def test_post_text(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/workflow/post_text/', {
            "text": "我是小明，我今天会去买菜,买菜当然是最吼的呀\n我是小红，我今天要去钓鱼,我觉得我可以钓到大的。", "title": "小明与小红"
            }, content_type="application/json", HTTP_AUTHORIZATION=token)
        self.assertEqual(responseAPI.status_code, 200)


#  用例编号: 119
#  测试单元描述: 测试/api/workflow/post_picture/接口
#  用例目的: 测试/api/workflow/post_picture/的操作是否成功
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
#         输入: 带有步骤1中token的request，上传的图片
# 		  期望输出: 返回成功状态码200
# 		  实际输出: “200”
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:
    def test_post_picture(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        with open('./test_file/img/good.jpg', 'rb') as fp:
            responseAPI = self.client.post('/api/workflow/post_picture/', {'file':  fp}, HTTP_AUTHORIZATION=token)
        self.assertEqual(responseAPI.status_code, 200)


#  用例编号: 120
#  测试单元描述: 测试/api/workflow/confirm_style/接口
#  用例目的: 测试/api/workflow/confirm_style/的操作是否成功
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
# 		  期望输出: 返回成功状态码200
# 		  实际输出: “200”
# 		  备注:
#  测试结果综合分析及建议: 测试成功
#  测试经验总结:
    def test_confirm_style(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        payload = jwt.decode(token, "Temage")
        payloadID = payload['id']
        self.assertEqual(payloadID, 2)
        responseAPI = self.client.post('/api/workflow/confirm_style/', {"styles": ["sport", "society"]}, content_type="application/json", HTTP_AUTHORIZATION=token)
        self.assertEqual(responseAPI.status_code, 200)

################################################
##############    集成测试    ###################
################################################
    def test_integrated_explore(self):
        response = self.client.post('/api/user/register/',  {'password': '123', 'username': 'tmg','email': '123123@qq.com','interest': ['society','sport'],'desc': 'love and peace'}, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_login = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        self.assertEqual(response_login.status_code, 200)
        token = response_login.content
        response = self.client.get('/api/explore/', HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)
        # res = json.loads(response.content.decode('utf-8'))
        # print(res)
        response = self.client.get('/api/explore/gallery/', HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)
        # res = json.loads(response.content.decode('utf-8'))
        # print(res)
        response = self.client.get('/api/explore/gallery/more_cards/', HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)
        # res = json.loads(response.content.decode('utf-8'))
        # print(res)
        response = self.client.get('/api/explore/collection/', HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)
        # res = json.loads(response.content.decode('utf-8'))
        # print(res)
        response = self.client.get('/api/explore/get_recent/', HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)
        # res = json.loads(response.content.decode('utf-8'))
        # print(res)
        response = self.client.post('/api/explore/product/', {'productID': '11'}, HTTP_AUTHORIZATION=token, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        # res = json.loads(response.content.decode('utf-8'))
        # print(res)
        response = self.client.post('/api/explore/post_collect/', {'productID': '18'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/api/explore/cancel_collect/', {'productID': '18'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/api/explore/delete/', {'productID': '18'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)


    def test_integrated_workflow(self):
        response = self.client.post('/api/user/login/', {'username': 'user1', 'password': '123'}, content_type="application/json")
        token = response.content
        self.assertEqual(response.status_code, 200)
        responseAPI = self.client.post('/api/workflow/post_text/', {
            "text": "我是小明，我今天会去买菜,买菜当然是最吼的呀\n我是小红，我今天要去钓鱼,我觉得我可以钓到大的。", "title": "小明与小红"
            }, content_type="application/json", HTTP_AUTHORIZATION=token)
        self.assertEqual(responseAPI.status_code, 200)
        with open('./test_file/img/good.jpg', 'rb') as fp:
            responseAPI = self.client.post('/api/workflow/post_picture/', {'file':  fp}, HTTP_AUTHORIZATION=token)
        self.assertEqual(responseAPI.status_code, 200)
        # response = json.loads(responseAPI.content.decode('utf-8'))
        # print(response)
        responseAPI = self.client.post('/api/workflow/push_match_event/', content_type="application/json", HTTP_AUTHORIZATION=token)
        # match_list = json.loads(responseAPI.content.decode('utf-8'))
        # print(match_list)
        responseAPI = self.client.post('/api/workflow/confirm_style/', {"styles": ["sport", "society"]}, content_type="application/json", HTTP_AUTHORIZATION=token)
        
        html = json.loads(responseAPI.content.decode('utf-8'))['html']
        print(html)
        self.assertEqual(responseAPI.status_code, 200)
        responseAPI = self.client.post('/api/workflow/store_passage/', {'styles' : ['sport', 'society'], 'res_html': html, 'title': 'xiao ming!', 't_width': '200'}, content_type="application/json", HTTP_AUTHORIZATION=token)
        self.assertEqual(responseAPI.status_code, 200)
        res = json.loads(responseAPI.content.decode('utf-8'))
        print(res)
        ID = res['ID']
        responseAPI = self.client.post('/api/workflow/finished_work/', {'productID': ID}, content_type="application/json", HTTP_AUTHORIZATION=token)
        res = json.loads(responseAPI.content.decode('utf-8'))
        print(res)
        self.assertEqual(responseAPI.status_code, 200)
        responseAPI = self.client.post('/api/workflow/confirm_store/', {'productID': ID, 'stars': '4.5', 'vector': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, content_type="application/json", HTTP_AUTHORIZATION=token)
        # res = json.loads(responseAPI.content.decode('utf-8'))
        # print(res)
        self.assertEqual(responseAPI.status_code, 200)
        responseAPI = self.client.post('/api/workflow/download_picture/', {'productID': ID}, content_type="application/json", HTTP_AUTHORIZATION=token)
        self.assertEqual(responseAPI.status_code, 200)