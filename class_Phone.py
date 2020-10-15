class Phone:
    def __init__(self,model,make,year,screen,camera,system):
        self.make = make
        self.model = model
        self.year = year
        self.screen = screen
        self.system = system
        self.camera = camera



    def description(self):
        return f'Производство : {self.make} Модель : {self.model} Год выпуска : {self.year}  Экран : {self.screen} дюймов , Камера : {self.camera}'


    def broke(self):
        self.battery = 100
        if self.battery == 0:
            print('Change your battery!')
        elif self.camera == 0:
            print('Your phone has broken!')



    def low_battery(self,battery):
        self.battery = battery
        if self.battery <= 20:
            print('Recharge')

    def battery_description(self):
         print(f'У вашего телефона {self.battery} % зарядки')



class Iphone(Phone):

    def __init__(self,model,year,screen,camera,make ='Apple',system='IOS'):
        super().__init__(self,model,year,screen,camera,system)

        self.processor = 'A14'
        self.power = 3000
        self.touch_id = True
        self.face_id = True
        self.siri = True
        self.memory = 256
        self.sim = 1
        self.pin = '1234'


    def description(self):
        print(f'{self.model} {self.year} {self.screen} {self.camera} ')


    def unblocking_iphone(self):
        if self.touch_id == False or self.face_id == False:
            print('Блокировка не работает')
        elif self.pin != '1234':
            print('Блокировка не работает')
        else:
            print("Телефон разблокирован")


    def video_play(self,min):
        self.battery = 100
        result = min // 5
        self.battery -= result
        return f'У вас осталось : {self.battery} %'




phone1 = Iphone('XS MAX','2018','6.5','12','IOS')



class Samsung(Phone):
    def __init__(self,model,year,screen,push,camera,owner,make='Samsung',system='Android'):
        super().__init__(model,year,screen,push,camera,system)
        self.processor = 'Cortex-A73'
        self.touch_id = True
        self.face_id = True
        self.siri = False
        self.memory = 64
        self.owner = owner


    def video_play(self,min):
        self.battery = 100
        result = min // 3
        self.battery -= result
        return f'У вас осталось : {self.battery} %'


    def internet_using(self,cash):
        self.cash = cash
        if self.cash > 0:
            print('Интернет работает')
        else:
            print('У вас недостаточно средств на балансе')

    def user(self,new_owner):
        self.owner = new_owner
        print(self.owner)

    def change_memory(self,product):
        if product == 'instagram':
            self.memory -= 3
        elif product == 'video':
            self.memory -= 0.8
        elif product == 'music':
            self.memory -= 0.5
        elif product == 'film':
            self.memory -= 4
        elif product == 'games':
            self.memory -= 5
        elif product == 'online_book':
            self.memory -= 1
        return f'Память : {self.memory}'


phone2 = Samsung('Galaxy S10','2018','6.4','12','Erjan','Android')
print(phone2.change_memory('film'))
