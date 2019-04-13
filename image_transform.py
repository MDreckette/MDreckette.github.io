from PIL import Image

my_image= Image.open("flower.jpeg")
image_pixels = my_image.load()
width, height= my_image.size
for i in range(0,width):
    for m in range(0,height):
        current_pixel=image_pixels[i,m]
        blue_components=current_pixel[0]
        green_components=current_pixel[1]
        red_components=current_pixel[2]
        gray_value=(int)(0.07*blue_components+0.72*green_components+0.21*red_components)
        new_value =(gray_value, gray_value, gray_value,255)
        if(gray_value <50):
            new_value= (176,138,226)
        elif(gray_value <100):
            new_value= (0,31,59,255)
        elif(gray_value <200):
            new_value= (215,30,1,255)
        image_pixels[i,m]= new_value


my_image.show()
