
# Mohammad Zafari
# mhdzafari80@gmail.com

count = 0
count2 = 0

def hanoi(n, start, mid, final):
    global count
    global count2
    count += 1
    if n == 1:
        print(f"Move Disk number {n}: {start} to {final}")
        count2 += 1 
    else:
        hanoi(n-1,start,final,mid)
        print(f"Move Disk number {n}: {start} to {final}")
        hanoi(n-1, mid, start, final)
N = int(input('Enter the number of Disk:'))
hanoi(N,'A','B','C')
print(f"THE NUMBER OF MOVES : {count}"'\n')
