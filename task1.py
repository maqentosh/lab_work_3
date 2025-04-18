# Задание 1
class Student: #создаём свой собственный тип — класс Студент
    """
 Класс представляющий студента
    """
    def __init__(self, name, student_id):
        self.name = name  # имя студента
        self.student_id = student_id  # айдмшник студента
        self.grades = []  # список оценок

    def add_grade(self, grade): #Функция которая добавляет оценку в список grades
        if 0 <= grade <= 10: #проверка на то что число от 0 до 10
            self.grades.append(grade) #добавляем оценку в список
        else:
            print("Оценка должна быть от 0 до 10")

    def get_average(self): #получаем среднюю оценку
        if self.grades: #проверка на то что число не 0
            return sum(self.grades) / len(self.grades) #считаем
        return 0

    def display_info(self): #функция печатает инфу про студика
        print(f"Студент: {self.name} (ID: {self.student_id})")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average():.2f}")
    # Магические методы
    def __str__(self): #возвращает строку, которую нужно показать
        return f"{self.name} (ID: {self.student_id})"

    def __eq__(self, other): #это способ сравнивать студентов
        return self.student_id == other.student_id

    def __len__(self): #oн вернёт сколько у студента оценок
        return len(self.grades)


# Задание 2
class Person:
    """
    класс для людей. Содержит имя и возраст
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person): #это значит что все что будет в классе персон будет и в классе тичер
    
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        """добавляет студента в список"""
        self.students.append(student)

    def remove_student(self, student_id):
        """удаляет студента по айдишнику"""
        self.students = [s for s in self.students if s.student_id != student_id]

    def list_students(self):
        """выводит список студентов"""
        print(f"Преподаватель: {self.name}, предмет: {self.subject}")
        for student in self.students:
            student.display_info()


# Задание 3
from abc  import ABC, abstractmethod  #для создания абстрактных классов
import math  #библиотека для математических функций
#abc (Abstract Base Classes) говорит чтобы все наследники обязаны реализовать этот метод
class Shape(ABC):
    #у фигуры должны быть методы area() и perimeter().
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape): #создаём новый класс Rectangle, который наследуется от Shape
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape): #тоже самое здесь наследование от shape
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

def print_shape_info(shape):
    """функция которая показывае как работает полиморфизм"""
    print("Площадь:", shape.area())
    print("Периметр:", shape.perimeter())


# Задание 4
class BankAccount:
    
    def __init__(self):
        self._balance = 0  #защищённый атрибут баланса
        self._transactions = [] # защищённый список операций

    def deposit(self, amount):
        """метод для пополнения счёта"""
        self._balance += amount
        self._transactions.append(f"Пополнение: +{amount}")

    def withdraw(self, amount):
        """метод для снятия денег со счёта"""
        if amount <= self._balance:
            self._balance -= amount
            self._transactions.append(f"Снятие: -{amount}")
        else:
            print("Недостаточно средств")

    @property
    def balance(self):
        """просмотр баланса."""
        return self._balance

    def show_transactions(self):
        """вывод всех операций по счёту"""
        print("История операций:")
        for t in self._transactions:
            print(t)


# Задание 6
class Temperature:
    
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if -273.15 <= value <= 1000:
            self._celsius = value
        else:
            print("Недопустимая температура")

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32


# Задание 7
class Assistant(Student, Teacher):
    
    def __init__(self, name, student_id, age, subject):
        Student.__init__(self, name, student_id)
        Teacher.__init__(self, name, age, subject)

    def help_student(self):
        print(f"Ассистент {self.name} помогает студентам по предмету {self.subject}")


#Примеры
if __name__ == "__main__":
    #Работа со студентом
    s1 = Student("БАКУ", 101)
    s1.add_grade(9)
    s1.add_grade(10)
    s1.display_info()

    #Работа с преподавателем
    t1 = Teacher("БАРБАРА МАВРИЛИНКИНА", 40, "Математика")
    t1.add_student(s1)
    t1.list_students()

    #полиморфизм
    r = Rectangle(5, 10)
    print_shape_info(r)

    #Банковский счёт
    acc = BankAccount()
    acc.deposit(500)
    acc.withdraw(200)
    acc.show_transactions()
    print("Баланс:", acc.balance)

    #Работа с температурой
    temp = Temperature(25)
    print("Температура в F:", temp.fahrenheit)

    #Ассистент
    a1 = Assistant("Максилиан", 202, 25, "Физика")
    a1.help_student()
