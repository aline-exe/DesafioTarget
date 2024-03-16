def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1): # percorrer a string inversamente
        string_invertida += string[i]
    return string_invertida

def palindromo (string_original):
    if string_original == string_original [::-1]: # se a string original for igual até de trás pra frente, palíndromo
        return True
    else: 
        return False
    

string_original = input("Digite alguma coisa legal: ")
string_invertida = inverter_string(string_original)

if palindromo(string_original):
    print("Legal! Você escreveu um palindromo! :) ") # indicação de palíndromo pois o resultado vai sair igual
else:
    pass
print("Palavra invertida:", string_invertida)

# palíndromos: radar, asa, arara