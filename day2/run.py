from lib import getStringFileAsArray

data = getStringFileAsArray('input')

depth = 0
horizontal_position = 0
aim = 0

for element in data:
    array = element.split(' ')
    print(array[0])

    if (array[0] == 'forward'):
        horizontal_position += int(array[1])
        depth += (int(array[1]) * aim)
    elif (array[0] == 'up'):
        aim -= int(array[1])
    elif (array[0] == 'down'):
        aim += int(array[1])

print('Horizontal position:', str(horizontal_position))
print('Depth', str(depth))
print (depth * horizontal_position)