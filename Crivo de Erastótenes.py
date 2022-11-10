import math 

 
 
 

def resolveocrivo(valor): 

    maior = math.sqrt(valor) 

    maior = math.floor(maior) 

    conjuntoOriginal = set(range(2, valor + 1)) 

    conjuntoParaRetirar = set() 

    for x in conjuntoOriginal: 

        for y in conjuntoOriginal: 

            if maior >= x != y and y % x == 0: 

                conjuntoParaRetirar.add(y) 

    print(conjuntoOriginal.difference(conjuntoParaRetirar)) 

 
 
 

if __name__ == '__main__': 

    valor = input("Digite um número maior que 2:") 

    try: 

        valor = int(valor) 

        if valor == 2: 

            print(2) 

        elif valor < 2: 

            print("Digite um valor maior que 2:") 

        else:     

            resolveocrivo(valor) 

    except: 

        print("Tente novamente") 

 

 