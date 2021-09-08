
def main():
    #escribe tu código abajo de esta línea
    pass

def fibo(num):
    if num <2:
        return num
    else:
        return  fibo(num-1) + fibo(num-2)


num = int(input("Enter a number: "))

res = fibo(num)
print(res)

if __name__=='__main__':
    main()
