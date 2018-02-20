def sumarDigito(numero):
    if numero<10:
        return numero
    else:
        return sumarDigito(int(numero/10))+(numero%10)

def potencia(numero, numerito):
    if numerito==0:
        return 1
    else:
        return potencia(numero,numerito-1)*numero

def producto(numero, numerito):
    if numerito==1:
        return numero
    else:
        return producto(numero,numerito-1)+numero

def maxDigito(numero):
    if numero<100:
        if numero%10 <= numero/10:
            return numero/10
        else:
            return numero%10
    else:
        if maxDigito(numero/10)<=numero%10:
            return numero%10
        else:
            return maxDigito(numero/10)

def longitud(numero):
    if numero<10:
        return 1
    else:
        return longitud(numero/10)+1
        

def palindromo(numero):
    if numero<10:
        return True
    elif numero<100:
        return int(numero/10) == numero%10
    else:
        return palindromo(int((numero-(int(numero/(10**(longitud(numero)-1)))*(10**(longitud(numero)-1))))/10)) and int(numero/(10**(longitud(numero)-1))) == numero%10

def invertido(numero):
    if numero<10:
        return numero
    elif numero<100:
        return int(numero/10) + (numero%10)*10
    else:
        return invertido(int((numero-(int(numero/(10**(longitud(numero)-1)))*(10**(longitud(numero)-1))))/10)) *10 + int(numero/(10**(longitud(numero)-1))) + ((numero%10)*(10**(longitud(numero)-1)))

def division(numero, numerito ):
    if numerito>numero :
        return 0
    elif numero==numerito :
        return 1
    else :
        return division(numero-numerito, numerito)+1

def fibonnacci(numero):
    if numero <=1 :
        return 1
    else :
        return fibonnacci(numero-1) + fibonnacci(numero-2)
    
    
        
                          
