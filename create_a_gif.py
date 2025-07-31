# import library that we need
import imageio.v3 as iio

# this list contains the location for the different images
filenames = ['chicklet1.png', 'chicklet2.png', 'chicklet3.png', 'chicklet4.png']
# empty list for storing the actual image data
images = []

# uses a for loop to cycle through the images
for filename in filenames:
  images.append(iio.imread(filename))

# uses the imwrite function to create the gif
iio.imwrite('chicklet.gif', images, duration = 500, loop = 0)