from django.core.management.base import BaseCommand, CommandError
from Temage.models import User
from Temage.models import Profile
from Temage.models import Product
from Temage.models import Card
from Temage.models import Style
from Temage.models import Collection
from Temage.models import Theme
from django.core.files import File

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
                product6 = Product.objects.create(title="product_6", html="<p>hot day</p>", creator=profile1,style=style7, score=0.7, id=16)
            product7 = Product.objects.create(title="product_7", html="<p>hot day</p>", creator=profile1,style=style8, score=0.7, id=17)
            product1.imagesrc.save('good.jpg', File(img1), save=True)
            product2.imagesrc.save('bad.jpg', File(img2), save=True)
            product3.imagesrc.save('cold.jpg', File(img3), save=True)
            product4.imagesrc.save('hot.jpg', File(img4), save=True)
            product5.imagesrc.save('hot.jpg', File(img4), save=True)
            product6.imagesrc.save('hot.jpg', File(img4), save=True)
            product7.imagesrc.save('hot.jpg', File(img4), save=True)
            product1.theme.add(theme1)
            product1.theme.add(theme2)
            product2.theme.add(theme2)
            card1 = Card.objects.create(creator=profile1, product=product1, title="positive", prompt="A positive people said...", id=1)
            card2 = Card.objects.create(creator=profile1, product=product2, title="negative", prompt="A negative people said...")
            card3 = Card.objects.create(creator=profile1, product=product3, title="cold", prompt="A cold people said...")
            card4 = Card.objects.create(creator=profile1, product=product4, title="hot", prompt="A hot people said...")
            card5 = Card.objects.create(creator=profile1, product=product5, title="hot", prompt="A hot people said...")
                card6 = Card.objects.create(creator=profile1, product=product6, title="hot", prompt="A hot people said...")
            card7 = Card.objects.create(creator=profile1, product=product7, title="hot", prompt="A hot people said...")
            collection1 = Collection.objects.create(name = "quote", user=profile1)
            collection1 = Collection.objects.create(name = "quote", user=profile1)
            collection1 = Collection.objects.create(name = "quote", user=profile1)
            collection1.cards.add(card1)
            collection1.cards.add(card2)
            collection2 = Collection.objects.create(name="requote", user=profile1)
            collection2.cards.add(card1)
        except:
            raise CommandError("The seed command has something wrong.")
        else:
            self.stdout.write('Successfully init the database')