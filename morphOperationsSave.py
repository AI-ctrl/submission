import cv2


image = cv2.imread("data/morphSample.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("gray", gray)

invert = cv2.bitwise_not(gray)

#erosion
# eroded = cv2.erode(invert, None, iterations=4)
# cv2.imshow("Eroded {} times".format(4), eroded)
# cv2.waitKey(0)


# # dilation
# dilated = cv2.dilate(invert, None, iterations=4)
# cv2.imshow("dilated {} times".format(4), dilated)
# cv2.waitKey(0)



#opening erosoin followed by dilation

opened = cv2.morphologyEx(invert, cv2.MORPH_OPEN, None)
cv2.imwrite("morphResults/opened.jpg", opened)
# cv2.waitKey(0)



#closing dilation followed by erosion

closed = cv2.morphologyEx(invert, cv2.MORPH_CLOSE, None)
cv2.imwrite("morphResults/closed.jpg", closed)
# cv2.waitKey(0)


# morph gradient
gradient = cv2.morphologyEx(invert, cv2.MORPH_GRADIENT, None)
cv2.imwrite("morphResults/gradient.jpg", gradient)
# cv2.waitKey(0)


#top hat
tophat = cv2.morphologyEx(invert, cv2.MORPH_TOPHAT, (9,9))
cv2.imwrite("morphResults/tophat.jpg", tophat)
# cv2.waitKey(0)



# black hat
blackhat = cv2.morphologyEx(invert, cv2.MORPH_BLACKHAT, (9,9))
cv2.imwrite("morphResults/blackhat.jpg", blackhat)
# cv2.waitKey(0)
