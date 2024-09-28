string_original = input("Digite uma string: ")


# Inverter a string manualmente
"""string_invertida = ""
for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]"""

i = len(string_original) - 1   
string_invertida = ""
while i >= 0:
    string_invertida += string_original[i]
    i -= 1
# Exibir a string invertida
print("String original:", string_original)
print("String invertida:", string_invertida)