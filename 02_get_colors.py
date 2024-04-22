def rgb(red=0, green=0, blue=0):
    return f'rgb({red}, {green}, {blue})'

def get_colors():
    dct = {'red': rgb(255, 0, 0),
           'green': rgb(0, 255, 0),
           'blue': rgb(0, 0, 255)}
    return dct


print(rgb(255))
print(get_colors())
