import matplotlib.pyplot as plt
import utm


loc1 = utm.from_latlon(22.548133, 72.850833)
loc2 = utm.from_latlon(22.433067, 72.991698)

home = utm.from_latlon(22.507484, 72.950398)
boat = utm.from_latlon(22.486708, 72.929456)
cbot = utm.from_latlon(22.476398, 72.910745)

from PIL import Image

image = Image.open('crop.png')
width,height = image.size
print(width,height)

scale_x = width/abs(loc1[0]-loc2[0])
scale_y = height/abs(loc1[1]-loc2[1])
print(scale_x,scale_y)

map_plot = plt.imread('crop.png')
bounding_box = (0,width,0,height)

latitude = [(loc1[0]-home[0])*scale_x+width,(loc1[0]-boat[0])*scale_x+width,(loc1[0]-cbot[0])*scale_x+width]
longitude = [(loc2[1]-home[1])*scale_y+height,(loc2[1]-boat[1])*scale_y+height,(loc2[1]-cbot[1])*scale_y+height]

fig, ax = plt.subplots(figsize=(15,10))
ax.scatter(latitude[0],longitude[0],color='green',s=200)
ax.scatter(latitude[1],longitude[1],color='blue',s=200)
ax.scatter(latitude[2],longitude[2],color='red',s=200)
ax.imshow(map_plot,extent=bounding_box)
plt.show()