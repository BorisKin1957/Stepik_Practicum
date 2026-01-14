'''Игрок наш учился в школе с глубоким изучением английского языка. Поэтому
down c up путает. ))'''

x, y, d = input().split()

match d:
    case 'down':
        new_x, new_y = int(x), int(y) + 1
    case 'right':
        new_x, new_y = int(x) + 1, int(y)
    case 'left':
        new_x, new_y = int(x) - 1, int(y)
    case 'up':
        new_x, new_y = int(x), int(y) - 1


print(f'x: {new_x}, y: {new_y}, direction: {d}')