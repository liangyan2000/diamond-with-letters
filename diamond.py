n = int (input("Please give me a number between 1 and 26: "))
column = 4*n -3
line = 2*n -1

lists = [['-' for i in range (column)] for i in range (line)]

x = line//2
y = column//2
letter = [chr(96+n-i) for i in range (n)]
z = n-1
lists[x][y] = letter[z]

def four_d(x, y, z):
    if lists [x-1] [y] == '-':
        lists [x-1] [y] = letter [z-1] 
    if lists [x+1] [y] == '-':
        lists [x+1] [y] = letter [z-1]
    if lists [x] [y+2] == '-':
        lists [x] [y+2] = letter [z-1]
    if lists [x] [y-2] == '-':
        lists [x] [y-2] = letter [z-1]

for k in range (n-1):
    for i in range (line):
        for j in range (column):
            if lists[i][j] in letter and lists[i][j] != letter [0]:
                four_d(i, j, letter.index(lists[i][j]))


for i in range (line):
    for j in range (column):
        print(lists[i][j], end='')
    print()
