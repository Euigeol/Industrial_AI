import cv2
import numpy as np

camera_matrix = np.load('c:/study/11week/pinhole_calib/camera_mat.npy')
dist_coefs  = np.load('c:/study/11week/pinhole_calib/dist_coefs.npy')

img = cv2.imread('c:/study/11week/pinhole_calib/img_00.png')

cv2.imshow('orignal image', img)

ud_img = cv2.undistort(img, camera_matrix, dist_coefs)
cv2.imshow('undistorted image1', ud_img)

opt_cam_mat, valid_roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, img.shape[:2][::-1], 0)
ud_img = cv2.undistort(img, camera_matrix, dist_coefs, None, opt_cam_mat)
cv2.imshow('undistorted image2', ud_img)

cv2.waitKey()
cv2.destroyAllWindows()

