input = [1,2,3,1,1,3]
# input = [1, 1, 1, 1]
# input = [1,2,3]
count = 0

print(input)
for index_input, value_input in enumerate(input):
    for index_check, value_check in enumerate(input):
        input_data = (index_input, value_input)
        check_data = (index_check, value_check)
        if input_data != check_data:
            if index_input < index_check:
                if value_input == value_check:
                    count += 1

print(count)

count = 0
for i in range(0, len(input)):
    for j in range(i + 1, len(input)):
        if input[i] == input[j]:
            count += 1
print(count)

