from PIL import Image

red = Image.open('red_color.jpg')
red.putalpha(128)
#red.show()
blue = Image.open('blue_color.png')
blue = blue.convert("RGB")
blue.save('blue_color_im.jpg')
blue.putalpha(128)
#blue.show()

blue.paste(red,box=((0,0)),mask=red)
print(type(blue.paste(red,box=((0,0)),mask=red)))
blue.show()
