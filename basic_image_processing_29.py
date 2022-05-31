
####
### This is a tutorial code and notes from https://www.youtube.com/watch?v=mQkcf8kgit8&list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG&index=30

###
from matplotlib import pyplot as plt 
from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.filters import gaussian,sobel 


## images will have unit8 type
im =io.imread("320033569584635.jpg")

##  images will have float64 type 
im_gray =io.imread("320033569584635.jpg", as_gray=True)


## %25 rescaling and image will have float64 , anti-aliasing gaussian smoothing uyguluyor.
im_rescale =rescale(im,1.0/4.0, anti_aliasing=False)


# Output Image will have 200 by 200 size
im_resize =resize(im,(200,200), anti_aliasing=False)

## it will strech image 4 by 3 scale 
img_downscaled=downscale_local_mean(im_gray,(4,3))
plt.imshow(img_downscaled,cmap='gray')


## it will create blur image 
#output image will be same size as input
#cval: value to fill edges
#sigma : Standard deviation for Gaussian kernel.
im_gaussian=gaussian(im_gray,sigma=5,mode="constant",cval=0.0) 

## it will create image with edges intensified
im_sobel=sobel(im_gray)

plt.imshow(im_sobel,cmap='gray')
plt.show()