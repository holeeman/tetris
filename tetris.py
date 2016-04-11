def matrix_transposition(my_list):
    
    output = []
    for r in range(len(my_list[0])):
        output.append([])
        for c in range(len(my_list)):
            output[r].append(my_list[c][r])
    return output

def reverse_rows(my_list):
    return my_list[::-1]

def rotate(my_list):
    return reverse_rows(matrix_transposition(my_list))

def board_init(w=10, h=24):
    

a = [[0, 0, 1], [1, 1, 1]]

b = [[1,1,1,1],[0,0,0,0]]

for i in b:
    print i

for i in rotate(b):
    print i
