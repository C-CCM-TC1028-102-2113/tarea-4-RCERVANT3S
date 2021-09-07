
def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea
    pass

num = int(input("Enter triangle height: "))
val = 2*num - 2
 
for i in range(0, num):
     
       
        for a in range(0, val):
            print(end=" ")
     
        
        val = val - 2
     
       
        for a in range(0, i+1):
         
           
            print("* ", end="")
     
       
        print("\r")




if __name__ == '__main__':
    main()
