path = './input.txt'
list_of_reading = []

with open(path) as f:
    for line in f:
        list_of_reading.append(int(line))


number_of_increase = 0
for index, value in enumerate(list_of_reading):
    if index < (len(list_of_reading )- 3 ):
        if( ((value + list_of_reading[index+1] + list_of_reading[index+2]) - (list_of_reading[index+1] + list_of_reading[index+2] + list_of_reading[index+3])) < 0):
            number_of_increase += 1

print(number_of_increase)