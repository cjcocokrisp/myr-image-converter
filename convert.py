try:
    from PIL import Image
except:
    print("The python image library is not installed...\nInstall it using pip install pillow")
    exit()

def rgb_to_hex(rgb: list[int, int, int, int] or tuple[int, int, int, int], mode: str):
    if mode == 'RGBA': return '%02x%02x%02x%02x' % rgb
    if mode == 'RGB': return '%02x%02x%02x' % rgb


print('-------------------------------\nMYR Image Converter')
# Get the file name and size of each pixel area 
file_name = input('Provide the file name: ')
pixel_size = int(input('Please input the pixel area for the image (If you do not know just use 1): '))

# Open and load image then create a text file for the output
img = Image.open(file_name)
loaded_img = img.load()
file = open(f'output/{file_name}.txt', 'w')
print('Converting...')

# Calculate the pixels per row (IMAGE WIDTH / PIXEL SIZE)
# The value is subtracted by 1 just to make sure there is no index out of bounds errors later in the program
pixels_per_row = int(img.size[0] / pixel_size) - 1

# Define the variables for the output
file.write('let x = 0;\n')
file.write('let y = 0;\n')
file.write('let transparent = false;\n\n')

# Define the loop header
loop_header = f'while(x < {pixels_per_row + 1})' + '{\n'

# Write the loops for the MYR output
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

# Loop Structure
# while(x <= AMOUNT OF PIXELS PER ROW){
#     if(x == 0 - PIXELS PER ROW AMOUNT){
#         SET THE COLOR
#     } 
#     if(transparent == false){
#         SET THE POSITION, THEN DRAW THE BOX AND INCREMENT
#         setPosition(x, y, 0);
#         box();
#         x++;
#     }
# }

# Tell user that the program is finished and wait for input
print("Conversion Successful! Press enter to exit...")
input("-------------------------------")