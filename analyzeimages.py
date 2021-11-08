##########################
# run getimages.py first!#
##########################

import os

import colorthief as ct
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
import seaborn as sns

genre_ids = [  # should be same as the one in getimages.py!
    4,  # fighting
    5,  # shooter
    8,  # platformer
    10,  # racing
    12,  # RPG
    36  # MOBA
]

directory = 'images'


def generateColorList(genre_id):
    for file in os.scandir(directory + "/" + str(genre_id)):
        if (file.path.endswith(".jpg") or file.path.endswith(".png")) and file.is_file():
            image = ct.ColorThief(file.path)
            palette = image.get_color()
            colours_list.append(palette)
            print(genre, os.path.basename(file.path), palette)


def getNameFromGenreID(genre_id):
    if genre_id == 4:
        output = "fighting game"
    elif genre_id == 5:
        output = "shooter game"
    elif genre_id == 8:
        output = "platforming"
    elif genre_id == 10:
        output = "racing game"
    elif genre_id == 12:
        output = "role playing game"
    elif genre_id == 36:
        output = "MOBA"
    return output


#  main
for genre in genre_ids:
    #  for plotting
    xlist = []
    ylist = []
    zlist = []
    clist = []
    colours_list = []

    ax = plt.axes(projection='3d')
    generateColorList(genre)

    for i in range(0, len(colours_list)):
        x = colours_list[i][0]
        xlist.append(x)
        y = colours_list[i][1]
        ylist.append(y)
        z = colours_list[i][2]
        zlist.append(z)
        c = (x / 255, y / 255, z / 255)
        clist.append(c)

    ax.scatter(xlist, ylist, zlist, c=clist, s=100, edgecolors='none')
    plt.title("Most dominant colours in the " + getNameFromGenreID(genre) + " genre.")
    plt.show()
    # extra condensation
    #plot all colours in 2D
    sns.palplot(colours_list, size=1)
    plt.show()
    # make new image of all the average cols
    im = Image.new('RGB', (len(colours_list), 1))
    im.putdata(colours_list)
    im.save("temp.png")
    # condense further to 6 values and saturate
    ctim = ct.ColorThief("temp.png")
    pal = ctim.get_palette(color_count=6)
    im2 = Image.new('RGB', (6, 1))
    im2.putdata(pal)
    im2.save("temp2.png")
    conv = ImageEnhance.Color(im2)
    im3 = conv.enhance(10)
    palette = im3.getdata()
    sns.palplot(palette)
    plt.show()
    os.remove("temp.png")
    os.remove("temp2.png")
