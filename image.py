from PIL import Image
import sys, os

if len(sys.argv) < 3:
  print("Usage: ./image.py image.png title")
  sys.exit()

# Setimage title
title = sys.argv[2]

assert os.path.exists(sys.argv[1])
background = Image.open("2600.png")
overlay = Image.open(sys.argv[1])
size = 495,495
overlay.thumbnail(size)
bg_w, bg_h = background.size
o_w, o_h = overlay.size
offset = ((bg_w - o_w) // 2, (bg_h - o_h) // 2)



#background = background.convert("RGBA")
#overlay = overlay.convert("RGBA")

#new_img = Image.blend(background, overlay, 0.5)a
x = 0
y = 0
if True:
  print("%s " % overlay)
  background.paste(overlay, offset, overlay.convert('RGBA'))
  background.save("2600_%s.png" % title, "PNG")
  #loc = raw_input("Change coordinates?[y/n]")
  
  """
  if loc.lower() == "y":
    x = input("Enter X position: ")
    y = input("Enter Y position: ")
  else:
    background.paste(overlay, (x, y), overlay.convert('RGBA'))
    background.save("2600_%s.png" % title, "PNG")
    break
  """

def paste(bg, fg, x=0, y=0):
  bg.paste(fg, (x,y), overlay.convert('RGBA'))
  bg.save("out.png", "PNG")

