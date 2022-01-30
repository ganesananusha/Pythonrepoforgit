# def fibonacci(n):
#     sequence = [0,1]
#
#
#     for i in range(2,n+1):
#         next_num = sequence[-1] + sequence[-2]
#         sequence.append(next_num)
#     return sequence
# # fibonacci(5)
# sequence = fibonacci(10)
# print(sequence)
#
# lambda a,b,c:a+2
array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:")
print(array_nums)
odd_ctr = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
even_ctr = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
print("\nNumber of even numbers in the above array: ", even_ctr)
print("\nNumber of odd numbers in the above array: ", odd_ctr)