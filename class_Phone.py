class Phone:
    def __init__(self,model,make,year,screen,camera,system):
        self.make = make
        self.model = model
        self.year = year
        self.screen = screen
        self.system = system
        self.camera = camera
        self.size = 10
        self.iscase = False


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


    def buy_phone(self, cash, price):
        self.cash = cash
        self.price = price
        if self.cash >= self.price:
            print('Вы можете позволить себе этот телефон')
        else:
            print("У вас не хватает денег")


    def wear(self,case):
        if self.size == case:
            self.iscase = True
            print(True)
        else:
            print(False)


class Iphone(Phone):

    def __init__(self,model,year,screen,camera,make ='Apple',system='IOS'):
        super().__init__(self,model,year,screen,camera,system)
        self.apple_id = True
        self.apple_id_username = ''
        self.apple_id_password = ''
        self.apple_id_check_password = ''
        self.processor = 'A12'
        self.power = 3000
        self.touch_id = True
        self.face_id = True
        self.siri = True
        self.memory = 256
        self.sim = 1
        self.pin = '1234'
        self.case = 20
        self.weight = 200


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


    def temperature(self,temp):
        self.battery = 100
        self.temp = temp
        if self.temp <= 5:
            self.battery == 0
            print('Переохлаждение телефона. Включите позже!')


    def broken_glass(self,glass):
        self.glass = glass
        if self.glass == 'Broken':
            print('Change this glass')


    def registration(self,username,password,check_password):
        if password == check_password:
            self.apple_id_username = username
            self.apple_id_password = password
            self.apple_id_check_password = check_password
            return f'Регистрация прошла успешно'
        else:
            print('Повторите попытку')


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
        self.size = 23
        self.weight = 175


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
        return f'Осталось {self.memory} gb памяти'


    def death(self):
        if self.camera == 0 and self.battery == 0 and self.screen == 0 and self.touch_id == 0 and self.face_id == 0:
            print('Ваш телефон ремонту не подлежит')
        else:
            print("Обратитесь к специалисту!")

    def take_photo(self):
        if self.camera > 0:
            print('Take a picture')
        else:
            print('Камера не работает')


    def take_video(self):
        if self.camera > 0:
            print('Take a video')
        else:
            print('Камера не работает')


phone2 = Samsung('Galaxy S10','2018','6.4','12','Daniel','Android')
