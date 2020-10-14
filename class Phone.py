class Phone:
    def __init__(self,model,make,year,screen,push,camera,system):
        self.make = make
        self.model = model
        self.year = year
        self.screen = screen
        self.push = push
        self.camera = camera
        self.battery = 100


    def description(self):
        return f'Производство : {self.make} Модель : {self.model} Год выпуска : {self.year}  Экран : {self.screen} дюймов , Камера : {self.camera}'


class Iphone(Phone):

    def __init__(self,model,year,screen,push,camera,make ='Apple',system='IOS'):
        super().__init__(make,model,year,screen,push,camera,system)
        self.processor = 'A14'
        self.power = 3000
        self.touch_id = True
        self.face_id = True
        self.siri = True
        self.memory = 256

    def broke(self):
        if self.power == 0:
            print('Change your battery!')
        elif self.camera == 0:
            print('Your phone has broken!')




    def low_battery(self,battery):
        self.battery = battery
        if self.battery == 0:
            print('Recharge')


phone = Iphone('XS MAX','2018','458','blocking','12')
print(phone.low_battery())



class Samsung(Phone):
    def __init__(self,model,year,screen,push,camera,make='Samsung',system='Android'):
        super().__init__(model,year,screen,push,camera,system)
        self.processor = 'Cortex-A73'
        self.power = 4000
        self.touch_id = True
        self.face_id = True
        self.siri = False
        self.memory = 64







