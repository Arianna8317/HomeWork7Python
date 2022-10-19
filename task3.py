# Задание 3.
# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
# __str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
# """
class Worker:
    
    def __init__(self, name, surname, position, wages, bonus):
              self.name = name
              self.surname = surname
              self.position = position
              self._income = { "wages" : wages,
                               "bonus" : bonus }


class Position(Worker):

    def get_full_name(self):
        return f"Работник : {self.name} {self.surname}" 

    def get_total_income (self):
        return self._income['wages'] + self._income['bonus']      

    def __str__(self):
        return f"Имя: {self.name} Фамилия: {self.surname} Должность: {self.position} Зарплата : {self._income['wages'] + self._income['bonus']}"             


man = Position("Сергей", "Колесник", "электрик", 78, 5)  
print(man.get_full_name())
print(f"Зарплата {man.get_total_income()}") 
print(man)           
woman = Position("Наталья", "Петрова", "бухгалтер", 150, 15)  
print(woman.get_full_name())
print(f"Зарплата {woman.get_total_income()}") 
print(woman)           