# pillow

# Original image size: %sx%s
# Resize image to: %sx%s
# thumbnail.jpg


from PIL import Image, ImageFilter

im = Image.open("WechatIMG11.jpeg")
x, y = im.size
print("Original image size: %sx%s" % (x, y))
im.thumbnail((x // 2, y // 2))
print("Resize image to: %sx%s" % (x / 2, y / 2))
im.save("change1.jpg", "jpeg")


im = Image.open("WechatIMG11.jpeg")
im2 = im.filter(ImageFilter.BLUR)
im2.save("change2.jpg", "jpeg")
