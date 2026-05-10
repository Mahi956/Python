Digit1 = float( input("enter your input_1 : "))
Operator = input("enter operator (+ , - , / , * , ** , // , % ) : ")
Digit2 = float( input("enter your input_2 : "))

if Operator == "+" :
    print("result : ",  Digit1 + Digit2)
    
elif Operator == "-" : 
    print("result : " ,  Digit1 - Digit2)
    
elif Operator == "*" :
    print("result : " ,  Digit1 * Digit2)
    
elif Operator == "**" :
    print("result : " , Digit1 ** Digit2)
    
elif Operator == "/" :
    if Digit1 != 0:
     print("result : " ,Digit1 / Digit2 )
    
    else:
        print("result : Error (dividion by zero)")  
        
elif Operator == "//" :
    if Digit1 != 0:
     print("result : " , Digit1 // Digit2 ) 
     
    else:
        print("result : Error (dividion by zero)")
        
else:
    print("INVALID OPERATOR")