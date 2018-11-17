from django.test import TestCase
from Temage.models import User

# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        User.objects.create(id=1,username=1234, is_superuser=False, email='1234@qq.com')
    def test_superuser(self):
        super_user = User.objects.all()
        print(super_user)
        self.assertEqual(len(super_user),1)

