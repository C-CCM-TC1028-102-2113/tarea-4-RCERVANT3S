def main():
    #escribe tu código abajo de esta línea
    pass

num1 = int(input())

for conta in range(1,num1+1,1):
    print(conta,end="-")
    if conta % 2 == 0:
       print("%") 
    else:     print("#") 

if __name__=='__main__':   
    main()
