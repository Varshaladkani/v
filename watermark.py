#Import required Image library
# from PIL import Image, ImageDraw, ImageFont
#
# #Create an Image Object from an Image
# im = Image.open('/home/varsha/Downloads/index.jpeg')
# width, height = im.size

# draw = ImageDraw.Draw(im)
# text = "sample watermark"
#
# font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
# textwidth, textheight = draw.textsize(text, font)
#
# # calculate the x,y coordinates of the text
# margin = 10
# x = width - textwidth - margin
# y = height - textheight - margin

# # draw watermark in the bottom right corner
# draw.text((x, y), text, font=font)
# im.show()
#
# #Save watermarked image
# im.save('images/watermark.jpg')

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# img = Image.new('RGB', (600, 400), color = 'red')
#
# img.save('pil_red.png')

font = ImageFont.truetype(r'/home/varsha/Downloads/OpenSans-Light.ttf', 24)

img = Image.new('RGB', (600, 400), color = 'red')

draw = ImageDraw.Draw(img)
draw.text((300, 200),"Hello World !",(0,0,0),font=font)

img.save('pil_red.png')