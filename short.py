import sys
import textwrap
import uuid
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

print("Enter/Paste your Kavithai. Ctrl-D ( windows ) to save it.")

contents = []
LINE = ""
QUOTES = ""
filename = str(uuid.uuid4())

while True:
    try:
        LINE = input()
    except (SyntaxError, ValueError):
        print("Empty Input or Wrong Input Value")
    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)
    except EOFError:
        break
    contents.append(LINE)

IMG = Image.open("images/quotes.png")
TEXT = "\n".join(contents)
SPACING = 30

wrapper = textwrap.TextWrapper(width=34)
word_list = wrapper.wrap(text=TEXT)

if word_list:
    for ii in word_list[:-1]:
        QUOTES = QUOTES + ii + "\n"
    QUOTES += word_list[-1]

    I1 = ImageDraw.Draw(IMG)
    COLOR = "rgb(0, 0, 0)"

    myFont = ImageFont.truetype("font/baloo.ttf", 36)

    I1.text((195, 480), QUOTES, spacing=SPACING, font=myFont, fill=COLOR)
    I1.text((442, 1000), "#tamilsms", fill = COLOR, font=myFont)

    IMG.save(filename + ".png")
    print("image Generated : " + filename + ".png")
else:
    print("Empty Kavithai Data")
