import numpy as np
import cv2

import matplotlib.pyplot as plt
from random import randrange

# stitch two image together
def Stitch(L, wp_image):
    # from warp image split it from the points from Homography and put the image to the position
    wp_image[0:Left.shape[0], 0:L.shape[1]] = Left

    return wp_image

# Use to Draw the Matching points
def Draw_Matching_Points(R, L, d1, d2, k1, k2):

    matche = bf.match(d1, d2)
    matche = sorted(matche, key=lambda x: x.distance)
    # Draw first 10 matches.
    # draw the corresponding Matching points
    img3 = cv2.drawMatches(L, k1, R, k2, matche[:100], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    plt.imshow(img3)
    plt.show()

# Find the Matching points of two image
def Find_Matching_Points(R, L):
    # ibtain the key point and the description
    key_point1, descriptor1 = orb.detectAndCompute(R, None)
    key_point2, descriptor2 = orb.detectAndCompute(L, None)
    Draw_Matching_Points(R, L, descriptor1, descriptor2, key_point1, key_point2)

    return bf.knnMatch(descriptor1, descriptor2, k=2), key_point1, key_point2

# Get the Homography from the matching points, Note that the matching points should be higher than 4
def Get_HomoGraphy(match_points):

    count = 0
    for i in range(len(match_points)):
        if match_points[i][1].distance > match_points[i][0].distance:
            # count how many good matching points
            count = count + 1
            nice_match.append(match_points[i])
    match_points = np.array(nice_match)
    # homography
    if count >= 4:
        src = np.float64([k1[m.queryIdx].pt for m in match_points[:, 0]]).reshape(-1, 1, 2)
        dst = np.float64([k2[m.trainIdx].pt for m in match_points[:, 0]]).reshape(-1, 1, 2)
        H, _ = cv2.findHomography(src, dst, cv2.RANSAC, 1.0)
    return H


if __name__ == '__main__':

    nice_match = []
    # setting
    orb = cv2.ORB_create()
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    # read image
    Right_BGR = cv2.imread("imageB.png")
    Left_BGR = cv2.imread("imageA.png")
    # change to RGB
    Right = cv2.cvtColor(Right_BGR, cv2.COLOR_BGR2RGB)
    Left = cv2.cvtColor(Left_BGR, cv2.COLOR_BGR2RGB)
    # find matching points
    match_points, k1, k2 = Find_Matching_Points(Right, Left)
    # Get homograpghy matrix
    H = Get_HomoGraphy(match_points)
    # Get the warp image
    wp_image = cv2.warpPerspective(Right, H, (Left.shape[1] + Right.shape[1], Left.shape[0]))
    # stitch image
    stitch_image = Stitch(Left, wp_image)

    plt.imshow(stitch_image)
    plt.show()
