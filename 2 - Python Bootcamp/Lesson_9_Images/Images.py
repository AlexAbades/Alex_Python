from PIL import Image

mac = Image.open(r"C:\Users\Alex Abades\Documents\Python\Udemy\Python\Complete-Python-3-Bootcamp-master\14-Working"
                 r"-with-Images\example.jpg")
print(type(mac))
mac  #.show()
print('\n')
# To see the size:
print("The size of the image is: ", mac.size)

# CROPPING IMAGES (getting a subsection of the original image)
# Using the method .crop, it ask for a four item tupple, the box, Which it's the left, upper, right, lowe corner pixel.
# Getting the full image
mac.crop((0, 0, 1993, 1257))#.show()
# Getting half of the image
mac.crop((0, 0, 996.5, 1257))#.show()
# Getting tha macintosh
computer = mac.crop((875, 820, 1150, 1257))#.show()

pencils = Image.open(r"C:\Users\Alex Abades\Documents\Python\Udemy\Python\Complete-Python-3-Bootcamp-master\14"
                     r"-Working-with-Images\pencils.jpg")
pencils  #.show()
print('The size is: ', pencils.size)

x = 0
y = 0
h = 1950 / 3
w = 1300 / 10

pencils.crop((x, y, h, w))  #.show()

# Copy and paste images inside images
mac.paste(im=computer, box= (0,0))
mac  #.show()

mac.paste(im=computer, box = (793, 0))
mac  #.show()

# The paste method it's permanently affecting to the variable, but it's not permanently affecting the image itself,
# it's just happening in memory


mac.resize((3000, 500))  #.show()
mac.rotate(90)  #.show()

# RGBA --> Red, Blue, Green, Alpha (transparency)

blue = Image.open(r"C:\Users\Alex Abades\Documents\Python\Udemy\Python\Complete-Python-3-Bootcamp-master\14-Working"
                  r"-with-Images\blue_color.png")
red = Image.open(r"C:\Users\Alex Abades\Documents\Python\Udemy\Python\Complete-Python-3-Bootcamp-master\14-Working"
                 r"-with-Images\red_color.jpg")

blue  #.show()
red  #.show()


red.putalpha(127)
red #.show()

red.putalpha(255)
blue.paste(im=red, box= (0,0), mask=red)
blue  #.show()

blue.save("purple.png")
purple = Image.open("purple.png")
purple  #.show()

matrix = Image.open(r"C:\Users\Alex Abades\Documents\Python\Udemy\Python\Complete-Python-3-Bootcamp-master\14-Working"
                    r"-with-Images\word_matrix.png")
mask = Image.open(r"C:\Users\Alex Abades\Documents\Python\Udemy\Python\Complete-Python-3-Bootcamp-master\14-Working"
                  r"-with-Images\mask.png")

print("The matrix size is: ", matrix.size)

re_mask = mask.resize(matrix.size).convert("L")
print("The resize mask size is: ", re_mask.size)

re_mask.paste(im=matrix, box=(0,0), mask=re_mask)
re_mask.show()