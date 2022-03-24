


input = [1,2,3,1,1,3]
# input = [1,1,1,1]
# input = [1,2,3]
count = 0


for index_input, value_input in enumerate(input):
    for index_check, value_check in enumerate(input):
        input_data = list([index_input, value_input])
        check_data = list([index_check, value_check])
        if input_data == check_data:
            pass
        elif value_input == value_check:
            print(f'{input_data} >>>> {check_data}')
            count += 1
    input.pop(0)
print(count)

