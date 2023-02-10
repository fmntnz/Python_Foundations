my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': "un Objeto que vuela en el aire y lleva personas o cosas",
  'name': 'Freddy',
  'last_name': 'Montañez',
  'age': 87
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))

print('avion' in my_dict)
print('otroqueno' in my_dict)