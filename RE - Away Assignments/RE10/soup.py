def soup(matrix,word):
    for fila in range(len(matrix)):
        for letra in range(len(matrix[fila])):
            if matrix[fila-1][letra-1] == word[0]:
                if checksoup(matrix,fila-1,letra-1,word[1:]):
                    return "{0}{1}".format(chr(ord("A")+fila-1),letra)


def checksoup(matrix,fila,letra,word):
    if word == "":
        return True
    else:
        for r in range(fila-1,fila+2):
            for l in range(letra-1,letra+2):
                if r>=0 and l>=0 and r<len(matrix) and l<len(matrix) and word[0] == matrix[r][l]:
                    matrix[r][l] == ""
                    if checksoup(matrix,r,l,word[1:]):
                        return checksoup(matrix,r,l,word[1:])
                    else:
                        continue


#print(soup((('X', 'A', 'B', 'N', 'T', 'O'),
#('Y', 'T', 'N', 'R', 'I', 'T'),
#('U', 'P', 'O', 'M', 'D', 'S'),
#('I', 'O', 'H', 'U', 'O', 'O'),
#('R', 'T', 'E', 'L', 'Q', 'X'),
#('I', 'W', 'J', 'K', 'P', 'Z')), 'PORTO'))