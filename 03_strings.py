### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print( my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado" # tabulación y escapado
print(my_scape_string)

my_scape_string = "\\tEste es un String \\n escapado" # \\ el primero anula tanto la tab y escapado
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35

print("Mi nombre es %s %s y mi edad es %s".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %s" %(name, surname, age))


print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[1:6]
print(language_slice)

language_slice = language[-2]
print(language_slice) 

language_slice = language[0:6:2] # 0 hasta 6 de 2 en 2
print(language_slice) 

# Reverse

reversed_language =language[::-1]
print(reversed_language)

# Funciones
language2 = "python"
language3 = "PRogramacIon"
pago = "2000000"
print(language2.capitalize())
print(language2.upper())
print(language3.count("o"))
print(pago.isnumeric())
print(language3.lower())
print(language3.lower().isupper())
print(language2.startswith("py"))
