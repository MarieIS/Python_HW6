mylist = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
output = [digit
          for each_list in mylist
          for each_list_2 in each_list
          for digit in each_list_2]
print(output)