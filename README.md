# Image-Stitching

## Image Stitching

```
a. The first depth of this algorithm is input two images which are supposed to stitch. 

b. Use in-built function knnMatch() to find the matching points

c. Determine which points is good match, if it is a good match, save it to the array

d. Use the good match points to compute the homography. Reason: Using the homography matrix so that we can perspective the image.

e. Use in-built function Warp perseptive to find the warp image. Reason: Makes two image looks like it from the same view.

f. Stitch two images into one, combine two image together.
```




![image](https://user-images.githubusercontent.com/55338365/170853247-45b05cb6-165c-42a0-a9e2-7dcd20b26337.png)


Fig 1. Match points


![image](https://user-images.githubusercontent.com/55338365/170853248-fc56c08e-fbd3-4b31-936a-ae8265395a76.png)


Fig 2. Stitch image
