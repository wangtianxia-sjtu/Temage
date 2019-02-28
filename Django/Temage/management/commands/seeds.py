#-*-coding:utf-8-*-
from django.core.management.base import BaseCommand, CommandError
from Temage.models import User
from Temage.models import Profile
from Temage.models import Product
from Temage.models import Card
from Temage.models import Style
from Temage.models import Collection
from Temage.models import Theme
from Temage.models import Cache
from django.core.files import File
from django.core.files.base import ContentFile

htmlmessi = '<p> Messi is Back! </p>'

class Command(BaseCommand):
    # for simply init the db
    def handle(self, *args, **options):
        try:
            # do something to init the db
            img1 = open("../test_file/img/good.jpg", "rb")
            img2 = open("../test_file/img/bad.jpg", "rb")
            img3 = open("../test_file/img/cold.jpg", "rb")
            img4 = open("../test_file/img/hot.jpg", "rb")
            avator1 = open("../test_file/img/girl.jpg", "rb")
            avator2 = open("../test_file/img/boy.jpg", "rb")
            css = open("../test_file/css/test.css", "rb")
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
            style1 = Style.objects.create(name="style_1")
            style2 = Style.objects.create(name="style_2")
            style3 = Style.objects.create(name="style_4")
            style4 = Style.objects.create(name="style_5")
            style5 = Style.objects.create(name="style_6")
            style6 = Style.objects.create(name="style_7")
            theme5.styles.add(style1)
            style1.css.save('test.css', File(css), save=True)
            style2.css.save('test.css', File(css), save=True)
            style3.css.save('test.css', File(css), save=True)
            style4.css.save('test.css', File(css), save=True)
            style5.css.save('test.css', File(css), save=True)
            style6.css.save('test.css', File(css), save=True)
            profile1 = Profile.objects.create(user = user1)
            cache = Cache.objects.create(user = profile1)
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
            product6 = Product.objects.create(title="product_6", html="<p>hot day</p>", creator=profile1,style=style1, score=0.7, id=16, width=400)
            product7 = Product.objects.create(title="product_7", html="<p>hot day</p>", creator=profile1,style=style2, score=0.7, id=17, width=400)
            product8 = Product.objects.create(title="Messi is Back!", html = htmlmessi, creator=profile1,style=style3, score=0.9, id=18, width=400)
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
        except:
            raise CommandError("The seed command has something wrong.")
        else:
            self.stdout.write('Successfully init the database')