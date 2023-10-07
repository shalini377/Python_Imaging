from PIL import Image, ImageFilter

before= Image.open("demo.png")
after= before.filter(ImageFilter.BoxBlur(10))
after.save("out_blur.png")
