#1
def max_num(a,b,c):
    return max([a,b,c])

print (max_num(1,2,3))
print(max_num(70,50,1))
print(max_num(80,15,2))

#2
def mult_list(lst):
    if len(lst) == 0:
        return 0
    
    prod = lst[0]

    if len(lst) > 1:
        for i in lst [1:]:
            prod = prod * i
    
    return prod

print(mult_list([5,6,7]))
print(mult_list([]))
print(mult_list([20]))

#3
def rev_string(my_str):
    return my_str[::-1]

print(rev_string("cats"))
print(rev_string("blueberry"))
print(rev_string("mt everest"))

#4
def num_within(x,y,z):
    return x in range(y,z+1)

print(num_within(5,4,6))
print(num_within(7,1,7))
print(num_within(12,27,6))

#5 
def pascal(n):
    triangle = []

    for i in range(n):
        row = [1]  # First element of each row is always 1

        if i > 0:
            previous_row = triangle[i - 1]
            for j in range(len(previous_row) - 1):
                row.append(previous_row[j] + previous_row[j + 1])

            row.append(1)  # Last element of each row is always 1

        triangle.append(row)

    # Print the triangle
    for row in triangle:
        print(" ".join(str(num) for num in row))

pascal(5)