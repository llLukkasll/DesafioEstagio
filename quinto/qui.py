# String a ser invertida
string_original = "exemplo"

# Inversão dos caracteres
string_invertida = ""
for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

# Exibição do resultado
print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
