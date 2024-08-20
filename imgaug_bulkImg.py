import cv2
import numpy as np
import os
     
# Specify the folder with the images to be augmented
folder_path = "C:/Users/sohad/OneDrive/Desktop/Python/BacBon"
save_path = "C:/Users/sohad/OneDrive/Desktop/Python/BacBon"

# Perform augmentation for each image in the folder
for filename in os.listdir(r"C:\Users\sohad\OneDrive\Desktop\Python\BacBon"):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load image
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)
        
        # Apply augmentation techniques to create new images
        flipped_img = cv2.flip(img, 1)
        rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        gaussian_blur_img = cv2.GaussianBlur(img, (5,5), 0)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
        color_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
        
        # Save new images
        new_filename_1 = "flipped_" + filename
        new_filename_2 = "rotated_" + filename
        new_filename_3 = "blurred_" + filename
        new_filename_4 = "grayed_" + filename
        new_filename_5 = "colored_" + filename

        
        new_img_path_1 = os.path.join(save_path, new_filename_1)
        new_img_path_2 = os.path.join(save_path, new_filename_2)
        new_img_path_3 = os.path.join(save_path, new_filename_3)
        new_img_path_4 = os.path.join(save_path, new_filename_4)
        new_img_path_5 = os.path.join(save_path, new_filename_5)
        
        cv2.imwrite(new_img_path_1, flipped_img)
        cv2.imwrite(new_img_path_2, rotated_img)
        cv2.imwrite(new_img_path_3, gaussian_blur_img)
        cv2.imwrite(new_img_path_4, gray_img)
        cv2.imwrite(new_img_path_5, color_img)
     
