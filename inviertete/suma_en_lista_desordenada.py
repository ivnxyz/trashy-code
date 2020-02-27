arr = [8, 7, 2, 5, 3, 1]

sum = int(input("Escribe la suma que quieres buscar: "))


def find_sum(n):
    
    result = []
    
    for i in range(0, len(arr)):
    
        first_number = arr[i]
    
        for j in range(i + 1, len(arr)):
            second_number = arr[j]
            
            if first_number + second_number == n:
                
                result.append(((i, j), (first_number, second_number)))

    # Imprimir el mensaje
    
    if len(result) > 0:
        for tupl in result:
            first_index = tupl[0][0]
            second_index = tupl[0][1]
            
            first_number = tupl[1][0]
            second_number = tupl[1][1]
            
            print("Encontré un par en los índices {} y {} ({}, {})".format(first_index, second_index, first_number, second_number))
    else:
        print("No encontré ningún par :(")
        
find_sum(sum)