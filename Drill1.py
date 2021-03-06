def marble(M,Istate,clicks):
    FinalState=Istate
    for i in range(clicks):
        FinalState = multiplicacion(M,FinalState)
    return FinalState


def multiplicacion(M,state):
    NextState = [0 for i in range(len(state))]
    for i in range(len(state)):
        for j in range(len(state)):
            NextState[i]+=M[i][j]*state[j]
    return NextState

def main():
    M = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]
    Istate = [6,2,1,5,3,10]
    clicks = int(input("please enter number of clicks"))
    print(marble(M,Istate,clicks))

if __name__ == "__main__":
    main()
