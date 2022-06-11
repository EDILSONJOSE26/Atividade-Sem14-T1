def soma_temperatura(tupla_com_as_temperaturas):
    temperatura1 = tupla_com_as_temperaturas[0]
    temperatura2 = tupla_com_as_temperaturas[2]
    if tupla_com_as_temperaturas[1] != tupla_com_as_temperaturas[3]:
        if tupla_com_as_temperaturas[3] == 'C':
            
            temperatura1 = (tupla_com_as_temperaturas[0] - 32) * (5/9), 'C'
        else:
            
            temperatura1 = (tupla_com_as_temperaturas[0] * (9/5))  + 32, 'F'
        soma_temp = round(temperatura1[0] + temperatura2,4) , temperatura1[1]
    else:
        soma_temp = round(temperatura1 + temperatura2, 4), tupla_com_as_temperaturas[1] 
    return soma_temp
    
def main():
    
    temperatura01 = float(input())
    escala01 = input().strip().upper()[0]
    temperatura02 = float(input())
    escala02 = input().strip().upper()[0]
    temperaturas = (temperatura01, escala01, temperatura02, escala02)

    
    soma_temp = soma_temperatura(temperaturas)

    
    print(f"({soma_temp[0]}, '{soma_temp[1]}')")
    
    
if __name__ == '__main__':
    main()
