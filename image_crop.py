import imgaug as ia
import imgaug.augmenters as iaa
import imageio
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import ipyplot  # Ensure this library is installed for image display
import imageio.v2 as imageio

# Read the input image
input_img = imageio.imread(r"C:\Users\sohad\OneDrive\Desktop\Python\BacBon\parrot.jpg")
crop1 = iaa.Crop(percent=(0, 0.5)) 
input_crop1 = crop1.augment_image(input_img)

# Display the original and cropped images using matplotlib
fig, axes = plt.subplots(1, 2, figsize=(15, 10)) 
# the first no. is used to crop vertically
#the second no. is used to crop horizontally

axes[0].imshow(input_img)
axes[0].set_title('Original')
axes[0].axis('off')

axes[1].imshow(input_crop1)
axes[1].set_title('Cropped Image')
axes[1].axis('off')

plt.show()