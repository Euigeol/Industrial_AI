import cv2
import numpy as np


img = cv2.imread('c:/image/BmW.png', cv2.IMREAD_GRAYSCALE)
connectivity = 8
num_labels, labelmap = cv2.connectedComponents(img, connectivity, cv2.CV_32S)

img = np.hstack((img, labelmap.astype(np.float32)/(num_labels - 1)))
cv2.imshow('Connected components', image)
cv2.waitKey()
cv2.destroyAllWindows()

image = cv2.imread('c:/image/BmW.png', cv2.IMREAD_GRAYSCALE)
otsu_thr, otsu_mask = cv2.threshold(image, -1,1,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

output = cv2.connectedComponentsWithStats(otsu_mask, connectivity, cv2.CV_32S)
num_label, labelmap, stats, centers = output
colored = np.full((image.shape[0], image.shape[1], 3), 0, np.uint8)

for l in range(1, num_labels):
    if stats[l][4] > 200:
        colored[labelmap == l] = (0, 255*l/num_labels, 255*(num_labels-l)/num_labels)
        cv2.circle(colored,
                   (int(centers[l][0]), int(centers[l][1])), 5, (255,0,0), cv2.FILLED)
        
image = cv2.cvtColor(otsu_mask*255, cv2.COLOR_GRAY2BGR)

cv2.imshow('Connected components', np.hstack((image, colored)))
cv2.waitKey()
cv2.destroyWindow()