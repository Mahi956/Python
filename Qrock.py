print("ROCK , PAPER , SCISSORS")
Player_1 = input("Enter Value1 :")
Player_2 = input("Enter Value2 :")

match Player_1 , Player_2:
    case "rock" , "paper":
        print("Rock Win ")
        
    case "rock" , "scissor":
        print("Rock Win")  
        
    case "paper" , "scissor" :
        print("Scissor Win")
        
    case "paper" , "rock":
        print("Paper Win")       
    
    case "scissor" , "rock":
        print("Rock Win") 
    
    case "scissor", "paper" :
        print("Scissor Win")
        
    case "rock", "rock":
        print("TIE")
        
    case "paper", "paper":
        print("TIE")
    
    case "scissor" ,"scissor":
        print("TIE")
    
    case _:
        print("Invalid Input ")