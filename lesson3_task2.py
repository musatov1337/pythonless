def my_func(**kwargs):
    return kwargs


print(my_func(name=(input("Введите ваше имя: ")).title(), secondname=(input("Введите вашу фамилию: ")).title(),
              year=input("Введите год рождения: "), city=(input("Введите город проживания: ")).title(),
              email=input("Email: "), phone=input("Введите ваш телефон: ")))


# Для себя
def my_func():
    my_dict = {"Имя": input("Введите ваше имя: "), "Фамилия": input("Введите вашу фамилию: "),
               "Год рождения": input("Введите год рождения: "),
               "Город проживания": input("Введите город проживания: "),
               "Почта": input("Email: "),
               "Телефон": input("Введите ваш телефон")}
    return my_dict


print(my_func())
