from PIL import Image

def rgb_to_hex(rgb, mode):
    if mode == 'RGBA': return '%02x%02x%02x%02x' % rgb
    if mode == 'RGB': return '%02x%02x%02x' % rgb

print('-------------------------------\nMYR Image Converter')
file_name = input('Provide the file name: ')
pixel_size = int(input('Please input the pixel area for the image: '))

img = Image.open(file_name)
loaded_img = img.load()
file = open(f'output/{file_name}.txt', 'w')
print('Converting...')
    
pixels_per_row = int(img.size[0] / pixel_size) - 1

file.write('let x = 0;\n')
file.write('let y = 0;\n')
file.write('let transparent = false;\n\n')

loop_header = f'while(x < {pixels_per_row + 1})' + '{\n'
y = img.size[1] - 1
while y > 0:
    file.write(loop_header)
    x = 0
    i = 0
    for i in range(pixels_per_row + 1):
        if img.mode == 'RGBA':
            if loaded_img[x, y][3] == 0:
                file.write(f'   if(x == {i})' + '{\n       transparent = true;\n    }\n')
            else:
                file.write(f'   if(x == {i})' + '{\n       setColor("#' + str(rgb_to_hex(loaded_img[x, y], img.mode)[0:6]) + '");\n    }\n')
        else:
            file.write(f'   if(x == {i})' + '{\n       setColor("#' + str(rgb_to_hex(loaded_img[x, y], img.mode)[0:6]) + '");\n    }\n')
        x += pixel_size
    file.write('    if(transparent == false){\n     setPosition(x, y, 0);\n     box();\n    }\n    transparent = false;\n    x++;\n}\n\n')
    file.write('x = 0;\ny++;\n\n')
    y -= pixel_size

print("Conversion Successful!\n-------------------------------")