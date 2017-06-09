from itertools import permutations

queinput = "1 3 7 6 8 3"
ansinput = "250"
gamesplit = queinput.split()
gameperm = list(map("".join, permutations(gamesplit)))
symbols = ['*','/','+','-','*','/','+','-','*','/','+','-','*','/','+','-','*','/','+','-']
symperm = list(map("".join, permutations(symbols)))
answer = []
for x in symperm:
    for n in gameperm:
        function = "("+"("+"("+"("+"("+n[0] + x[0] + n[1]+")" + x[1] + n[2]+")" + x[2] + n[3]+")" + x[3] + n[4]+")" + x[4] + n[5]+")"
        if eval(function) == int(ansinput):
            ans = (n[0] + x[0] + n[1] + x[1] + n[2] + x[2] + n[3] + x[3] + n[4] + x[4] + n[5])
            print ans


print answer

