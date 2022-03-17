# input = [1,2,3,1,1,3]
input = [1,1,1,1]
# input = [1,2,3]
count = 0

print(input)
for index_input, value_input in enumerate(input):
    print([index_input, value_input])
    for index_check, value_check in enumerate(input):
        input_data = list([index_input, value_input])
        check_data = list([index_check, value_check])
        if input_data != check_data:
            if index_input < index_check:
                if value_input == value_check:
                    print(f'{input_data} >>>> {check_data}')
                    count += 1
    print(input)
print(count)

