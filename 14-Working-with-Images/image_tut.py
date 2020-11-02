from PIL import Image

comp = Image.open('example.jpg')
print(comp.size)
half = 1993/2
x,y,w,h = (half - 110 ),850,(half+145),1257
print(x,y,w,h)
comp.crop((x,y,w,h)).show()
print(comp.crop((x,y,w,h)).size)
#comp.show()