def main():
  #escribe tu código abajo de esta línea
    pass
promedio = 0
contador = 0

a = float(input())
if a >= 0:
    promedio = promedio + a
    contador = contador +  1

while a >= 0: 
    a = float(input())
    if a >= 0:
        promedio = promedio + a
        contador = contador +  1
    else: 
        promedio1 = promedio / contador 

print(promedio1)

if __name__ == '__main__':
    main()
