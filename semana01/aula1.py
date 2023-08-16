#matriz
matriz = [[1,2,3],[4,5,6],[7,8,9]]
for line in range(len(matriz)):
    for column in range(len(matriz[line])):
        print(matriz[line][column], end=" ")
    print(end="\n")
###########

def scale(matriz,scale_value):
    result = []
    for line in range(len(matriz)):
        result.append([])
        for column in range(len(matriz[line])):
            result[line].append(matriz[line][column] * scale_value)
           
    return result
    
    
    
    
def main():
    matriz = [[5,32,5],[3,76,43],[20,27,83]]
    result = scale(matriz,5)
    print(result)

main()
