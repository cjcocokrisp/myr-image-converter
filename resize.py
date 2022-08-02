try:
    from PIL import Image
except:
    print("The python image library is not installed...\nInstall it using pip install pillow")
    exit()

# Get the file name and the resize percentage
print('-------------------------------\nImage Resize')
file_name = input('Provide the file name: ')
resize_percentage = 0.01 * int(input('By what percent would you like to resize your image?\nAbove 100 is an increase, below 100 is a decrease\n'))

# Resize the image
print('Resizing...')
img = Image.open(file_name)
new_img = img.resize((int(img.size[0] * resize_percentage), int(img.size[1] * resize_percentage)))
new_img.save(file_name)

print("Resize Successful! Press enter to exit...")
input("-------------------------------")