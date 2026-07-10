def is_balanced(text):
    # TODO: implement bracket balance check
    pila = []
    
    parejas = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for caracter in text:
        
        if caracter in parejas.values(): 
            pila.append(caracter)
            
        elif caracter in parejas:  
            if not pila:
                return False
            
            ultimo_abierto = pila.pop()
            
            if ultimo_abierto != parejas[caracter]:
                return False
                
    return len(pila) == 0


argument = input() if __name__ == "__main__" else ""
print(is_balanced(argument))
