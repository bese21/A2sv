if __name__ == '__main__':
    N = int(input())
    list=[]
    for _ in range(N):
        x=input().split()
        if x[0]=="append":
            for i in range(1,len(x)):
                list.append(int(x[i]))
        elif x[0]=="print":
            print(list)
        elif x[0]=="insert":
            list.insert(int(x[1]),int(x[2]))
        elif x[0]=="remove":
            list.remove(int(x[1]))
        elif x[0]=="sort":
            list.sort()
        elif x[0]=="reverse":
            list.reverse()
        else:
            list.pop()
            
        
