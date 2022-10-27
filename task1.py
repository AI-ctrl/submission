import cv2

image = cv2.imread("data/Task_1.jpg")
imgeCopy = image.copy()
refPt = []
cropping = False
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		# print("inittial",refPt)
		cropping = True
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False
		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		# print(refPt)
		cv2.imwrite("task1Results/Task_1_cropped.jpg",imgeCopy[refPt[0][1]:refPt[1][1],refPt[0][0]:refPt[1][0]])
		cv2.imshow("Window", image)
		cv2.imwrite("task1Results/Task_1_insights.jpg",image)
		
# Making Window For The Image
cv2.namedWindow("Window")
cv2.imshow("Window",image)

# Adding Mouse CallBack Event
cv2.setMouseCallback("Window",click_and_crop)
# cv2.imwrite()
cv2.waitKey(0)



