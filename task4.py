#Задание 4.
# Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
# speed, color, name, is_police (булево).
# А также публичные методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс публичный метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
# """
class Car:
     is_police = False 
     speed = 0    
  
     def __init__(self, name, color):
            self.name = name
            self.color = color
  
     def show_self(self):
         print(f"Машина {self.name}, цвет {self.color}")
  
     def show_speed(self):            
           print (f"Скорость равна {self.speed}")
  
     def go(self, speed):
           self.speed = speed
           #print (f"Едем со скоростью {speed}") 
  
     def stop(self):
           self.speed = 0
           print(f"Остановка")           
  
     def turn(self, direction):
           if direction == 1 :
              print ("Повернули налево ")
           else :
              print ("Повернули направо")      


class TownCar(Car):

     def show_speed(self):
         super().show_speed()         
         if self.speed > 60:
             print("Cкорость превышает разрешенную в городе!")
         else:
             print("Скорость в допустимых пределах")    


class WorkCar(Car):

     def show_speed(self):
         super().show_speed()         
         if self.speed > 40:
             print("Cкорость превышает разрешенную!")
         else:
             print("Скорость в допустимых пределах")  

             
class PoliceCar(Car):

     is_police = True   

     def show_self(self):
         super().show_self()
         print("Полицейский автомобиль")       

                        
car1 = Car("BMV","зеленый")
car1.show_self()
car1.go(35)
car1.show_speed()
car1.stop()  
car1.color = "светло-зеленый"
print(car1.color)
car2 = TownCar("Toyota", "белый")
car2.show_self()
car2.color = "серый"
car2.show_self()
car2.show_speed()
car2.go(35)
car2.show_speed()
car2.go(65)
car2.show_speed()
car2.speed = 100
car2.show_speed()
car2.turn(1)
car3 = WorkCar("КАМАЗ", "красный")
car3.show_self()
car3.go(70)
print(car3.speed)
car3.show_speed()
car4 = PoliceCar("Lada", "синий") 
car4.show_self()
car4.color = "белый"
car4.show_self()
car4.show_speed()
car4.go(78)
car4.show_speed()
car4.turn(3)      
car4.stop()              
                     