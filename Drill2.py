def multipleSlits(numSlits,numTargets):
    nodos = numSlits+numTargets+1
    matriz = [[0 for i in range(nodos)]for j in range(nodos)]
    for i in range(numSlits):
        matriz[i+1][0]=1/numSlits
    for i in range(1,numSlits+1):
        for j in range(numSlits+1,nodos):
            valor = input("valor de "+str(i)+" a "+str(j)+" : ")
            if valor!='0':
                matriz[j][i]=int(valor[0])/int(valor[2])
            else:
                matriz[j][i]=0
    for i in range(numSlits+1,nodos):
        matriz[i][i]=1
    return matriz
                   


def main():
    numSlits = int(input("ingrese numero de slits : "))
    numTargets = int(input("write the number of targets: "))
    for i in multipleSlits(numSlits,numTargets):
        print(i)

main()
    
