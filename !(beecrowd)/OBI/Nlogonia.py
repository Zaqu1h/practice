alfabeto = "abcdefghijklmnopqrstuvxz"

vogais = "aeiou"

palavra = input()
cifrado = []
pos = 0

for letra in palavra:
    
    cifrado.append(letra)
    
    if letra not in vogais:
        pos = alfabeto.index(letra)
        
        if pos == len(alfabeto) - 1:
            cifrado.append('uz')
            continue
        
        for i in range(len(alfabeto) - 1):
            
            if (pos - (i + 1)) >= 0:
                esq = alfabeto[pos - (i + 1)]
                
            if (pos + (i + 1)) <= len(alfabeto) - 1:
                dir = alfabeto[pos + (i + 1)]  
            
            if esq in vogais and dir in vogais:
                vogalProx = esq
                break
            
            if dir in vogais:
                vogalProx = dir
                break
            
            if esq in vogais:
                vogalProx = esq
                break
        
        cifrado.append(vogalProx)
            
        for i in range(len(alfabeto) - 1):
            
            consProx = alfabeto[pos + (i + 1)]
            if consProx not in vogais:
                cifrado.append(consProx)
                break

print(''.join(cifrado))
