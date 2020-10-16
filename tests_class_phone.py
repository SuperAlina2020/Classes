from class_Phone import Phone,Iphone,Samsung
from  unittest import TestCase

class TestPhone(TestCase):

    def test_battery(self):
        new_phone = Iphone('XS MAX','2018','6.5','12','IOS')
        new_phone.battery = 0
        self.assertEqual(new_phone.battery,0)

    def test_camera(self):
        new_phone1 = Iphone('XS MAX','2018','6.5','12','IOS')
        new_phone1.camera = 0
        self.assertEqual(new_phone1.camera,0)

    def test_power(self):
        new_phone2 = Iphone('XS MAX','2018','6.5','12','IOS')
        new_phone2.power = 0
        self.assertEqual(new_phone2.power,0)

    def test_processor(self):
        new_phone3 = Iphone('XS MAX','2018','6.5','12','IOS')
        new_phone3.processor = 'A12'
        self.assertEqual(new_phone3.processor,'A12')

    def test_model(self):
        new_phone4 = Iphone('XS MAX','2018','6.5','12','IOS')
        new_phone4.model = 'XS MAX'
        self.assertEqual(new_phone4.model,'XS MAX')

    def test_pincode(self):
        new_phone5 = Samsung('Galaxy S10','2018','6.4','12','Daniel','Android')
        new_phone5.pin = '1234'
        self.assertEqual(new_phone5.pin,'1234')


    def test_memory(self):
        new_phone6 = Samsung('Galaxy S10','2018','6.4','12','Daniel','Android')
        new_phone6.memory = 64
        self.assertEqual(new_phone6.memory,64)


    def test_id(self):
        new_phone7 = Iphone('XS MAX','2018','6.5','12','IOS')
        new_phone7.apple_id = True
        self.assertEqual(new_phone7.apple_id,True)


    def register(self):
        new_iphone = Iphone('XS MAX','2018','6.5','12','IOS')
        new_iphone.apple_id_username = 'user'
        self.assertEqual(new_iphone.apple_id_username,'user')

    def register_password(self):
        new_iphone1 = Iphone('XS MAX','2018','6.5','12','IOS')
        new_iphone1.apple_id_password = '12345'
        self.assertEqual(new_iphone1.apple_id_password,'12345')

    def register_check_password(self):
        new_iphone2 = Iphone('XS MAX','2018','6.5','12','IOS')
        new_iphone2.apple_id_check_password = '12345'
        self.assertEqual(new_iphone2.apple_id_check_password,'12345')
