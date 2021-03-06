import Drill1
import matplotlib.pyplot as plt
def multipleSlits(numSlits,numTargets):
    nodos = numSlits+numTargets+1
    matriz = [[0 for i in range(nodos)]for j in range(nodos)]
    for i in range(numSlits):
        matriz[i+1][0]=1/numSlits
    for i in range(1,numSlits+1):
        for j in range(numSlits+1,nodos):
            valor = input("valor de "+str(i)+" a "+str(j)+" : ")
            if valor!='0':
                matriz[j][i]=round(int(valor[0])/int(valor[2]),2)
            else:
                matriz[j][i]=0
    for i in range(numSlits+1,nodos):
        matriz[i][i]=1
    return matriz
                   


def main():
    click = int(input("Ingrese el numero de clicks : "))
    numSlits = int(input("ingrese numero de slits : "))
    numTargets = int(input("write the number of targets: "))
    Istate = [0 for i in range(numSlits+numTargets+1)]
    Istate[0]=1
    matriz = multipleSlits(numSlits,numTargets)
    final = Drill1.marble(matriz,Istate,click)
    print("La matriz resultante es :")
    for i in matriz:
        print(i)
    print()
    print("El vector resultante es : ")
    print(final)
    plt.bar([i for i in range(len(final))],final)
    plt.show()

if __name__=='__main__':
    main()


