import re

class Person:
    def __init__(self, fio, age, passport, weight):
    self.__fio = fio  # устанавливаем имя
    self.__age = age  # устанавливаем возраст
    self.__passport = passport  # устанавливаем паспорт
    self.__weight = weight  # устанавливаем вес

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 14 < age < 150 and int(age):
            self.__age = age
        else:
            print("Возраст должен быть целым числом от 14 до 150")
                                                                                                                            @property                                                 
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        pattern = r"([А-ЯЁ][а-яё]+[\-\s]?){1,}"
        if re.match(pattern, fio) is not None:
            self.__fio = fio
        else: 
            print("Недопустимое имя")
    @property                            
    def passport(self):                                                                                                         return self.__passport
                                                                                                                            @passport.setter                                                                                                        def passport(self, passport):
        pattern = r"\d{4}\s\d{6}"                                                                                               if re.match(pattern, passport) is not None:                                                                                   self.__passport = passport                           
        else:                                                                                                                         print("Неверный формат паспорта")                                                                             @property                                                                                                               def weight(self):
        return self.__weight                                                                                                                                                                                                                        @weight.setter                                                                                                          def weight(self, weight):
        if weight >= 25:                                                                                                               self.__weight = weight                                                                                           else:                                                                   
            print("Вес должен быть вещественным числом от 25 и выше")                                                                                                                                                                                                                                                                                                       def display_info(self)                             
            print(f"Имя: {self.__fio}\tВозраст: {self.__age} \tПаспорт: {self.__passport}\tВес: {self.__weight}")
