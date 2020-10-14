from class_Phone import Phone,Iphone,Samsung
from  unittest import TestCase

class TestPhone(TestCase):

    def test_battery(self):
        new_phone = Iphone('XS MAX','2018','458','blocking','12')
        new_phone.battery = 0
        self.assertEqual(new_phone.battery,0)

    def test_camera(self):
        new_phone1 = Iphone('XS MAX','2018','458','blocking','12')
        new_phone1.camera = 0
        self.assertEqual(new_phone1.camera,0)

    def test_power(self):
        new_phone2 = Iphone('XS MAX','2018','458','blocking','12')
        new_phone2.power = 0
        self.assertEqual(new_phone2.power,0)

    def test_processor(self):
        new_phone3 = Iphone('XS MAX','2018','458','blocking','12')
        new_phone3.processor = 'A14'
        self.assertEqual(new_phone3.processor,'A14')

    def test_model(self):
        new_phone4 = Iphone('XS MAX','2018','458','blocking','12')
        new_phone4.model = 'XS MAX'
        self.assertEqual(new_phone4.model,'XS MAX')