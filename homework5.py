immutable_var = "я", 2, 3, 4, "пакетик"

print(immutable_var)
print(immutable_var[0])
print(immutable_var[-1])

#immutable_var[0] = 200
#изменять картеж нельзя так как картеж является неизменным списком, из него можно что то взять но не заменить или положить

mutable_list = [1, 2, 3]

mutable_list[1] = 4
mutable_list.append('я не умею')
mutable_list.extend(['программировать', 'da' ])
mutable_list.remove(1)

print(mutable_list)