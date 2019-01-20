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
            theme1 = Theme.objects.create(name="sport", id=1)
            theme2 = Theme.objects.create(name="art", id=2)
            theme3 = Theme.objects.create(name="history", id=3)
            profile1 = Profile.objects.create(user = user1, phone = "+8618217508975", sex = 1)
            profile2 = Profile.objects.create(user = user2, phone = "+8612334443223", sex = 0)
            profile1.theme.add(theme1)
            profile1.theme.add(theme2)
            product1 = Product.objects.create(title="product_1", html="<p>good day</p>", creator=profile1,style=style1, score=0.1, id=11)
            product2 = Product.objects.create(title="product_2", html="<p>bad day</p>", creator=profile1,style=style2, score=0.9, id=12 )
            product1.imgsrc.save('good.jpg', File(img1), save=True)
            product2.imgsrc.save('bad.jpg', File(img2), save=True)
            product1.theme.add(theme1)
            product1.theme.add(theme2)
            product2.theme.add(theme2)
            card1 = Card.objects.create(creator=profile1, product=product1, url="http://temage/goodday", title="positive", prompt="A positive people said...")
            card2 = Card.objects.create(creator=profile1, product=product2, url="http://temage/goodday", title="negative", prompt="A negative people said...")
            collection1 = Collection.objects.create(name = "quote", user=profile1)
            collection1.cards.add(card1)
            collection1.cards.add(card2)
            collection2 = Collection.objects.create(name="requote", user=profile1)
            collection2.cards.add(card1)
        except:
            raise CommandError("The seed command has something wrong.")
        else:
            self.stdout.write('Successfully init the database')