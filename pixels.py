from PIL import Image
from urllib.request import urlopen

img = Image.open(urlopen('https://i.scdn.co/image/557a6058e3de72bf37ffcd2c12dd5932276df344'))

px = img.load()
width, height = img.size

pixelList = []

def main():
    get_vertical_pixelList()
    get_horizontal_pixelList()
    #print(pixelList)

def get_vertical_pixelList():
    for i in range(int(width/20)):
        pixel_location = i*width/20
        pixel_top = px[i*width/20,20]
        pixel_bottom = px[i*width/20,height-20]
        pixelList.append(pixel_top)
        pixelList.append(pixel_bottom)
        # break when bigger than image
        if (pixel_location == width-(width/20)):
            break


def get_horizontal_pixelList():
    for i in range(int(height/20)):
        pixel_location = i*height/20
        pixel_right = px[width-20,i*height/20]
        pixel_left = px[20, i*height/20]
        pixelList.append(pixel_right)
        pixelList.append(pixel_left)

        # break when bigger than image
        if (pixel_location == height-(height/20)):
            break

main()
