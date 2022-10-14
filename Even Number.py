def odd(num):
    return num % 2 != 0
def even(num):
    return num % 2 == 0

print("filter Even Number from the list !! ")
num_list = [2,7,9,3,4,5,8]
print(f"Mixed list : {num_list}")

even_list = filter(even, num_list)
even_list = list(even_list)
print(f"even list : {even_list}")

odd_list = filter(odd,num_list)
odd_list = list(odd_list)
print(f"odd list : {odd_list}")