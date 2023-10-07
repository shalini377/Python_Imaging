# FIND_EDGES argument, which in turns runs a edge detection kernel on top of the image. The output of the above function results in an image with high intensity changes (edges) in shades of white, and rest of the image in black color.
from PIL import Image, ImageFilter

before=Image.open("demo.png")
after=before.filter(ImageFilter.FIND_EDGES)
after.save("out_edges.png")