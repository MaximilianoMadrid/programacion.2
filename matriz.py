#matriz_sencilla=[
    #[1,2,3],
    #[4,5,6]
#]
#for elemento in matriz_sencilla:
    #print(elemento)
matriz_sencilla=[
        [1,2,3],
        [4,5,6]
    ]
print("1) imprimir por posicion")
for elemento in matriz_sencilla:
        print=(elemento)
        print("2)imprimir un elemento por posicion")
        print(matriz_sencilla[1][0])
        print("3)imprimir todos los elementos")
        for fila in matriz_sencilla:
            for elemento in fila:
                print(elemento, end="")
                print()