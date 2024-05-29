#Я думаю много воды написал но попытался использовать все методы надеюсь получилось правильно
# Словарчик года рождения
my_dict = {"Misha": 2002, "Sasha": 1987, "Andrey": 2003}

print(my_dict)
print(my_dict["Misha"])
print(my_dict.get("coconut"))
my_dict["Kazjemyaka"] = 1111
print(my_dict["Kazjemyaka"])
my_dict.update({"Гриня": 2004,
                "Якто?": 1955})
print(my_dict)
Black_list = my_dict.pop("Kazjemyaka")
print(Black_list)
print(my_dict)


#Множество
my_set = {1, 2, 4, 2, 4, 5, 1, 5, 4, 2, 2, "Misha"}

print(my_set)
my_set.update({"Little", "lolipop"})
print(my_set)
my_set.remove('Misha')
print(my_set)