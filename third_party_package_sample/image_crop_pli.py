from PIL import Image
img= Image.open(r"C:/Users/Suhaib/OneDrive/Pictures/Screenshots/Screenshot (12).png")

width,height=img.size
print(width,height)

left = int(input("enter left pixel \n"))
top = int(input("enter top pixel \n"))
right = int(input("enter right pixel \n"))
bottom = int(input("enter bottom pixel"))

img_crop=img.crop((top,right,))


img_crop.show()
#img.show()