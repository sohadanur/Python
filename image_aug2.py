import imgaug as ia
import imgaug.augmenters as iaa
import imageio
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import ipyplot  # Ensure this library is installed for image display

# Read the input image
input_img = imageio.imread(r"C:\Users\sohad\OneDrive\Desktop\Python\BacBon\parrot.jpg")

# Perform image augmentation using imgaug

# Horizontal Flip
hflip = iaa.Fliplr(p=1.0)
input_hf = hflip(image=input_img)

# Vertical Flip
vflip = iaa.Flipud(p=1.0)
input_vf = vflip(image=input_img)

# Display the original and augmented images using matplotlib
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(input_img)
axes[0].set_title('Original')
axes[0].axis('off')

axes[1].imshow(input_hf)
axes[1].set_title('Horizontally Flipped')
axes[1].axis('off')

axes[2].imshow(input_vf)
axes[2].set_title('Vertically Flipped')
axes[2].axis('off')

plt.show()


#Rotation of image
# Rotation of image
input_img2 = imageio.imread(r"C:\Users\sohad\OneDrive\Desktop\Python\BacBon\parrot.jpg")
rot1 = iaa.Affine(rotate=(-50, 20))
input_rot1 = rot1.augment_image(input_img2)

# Display the original and rotated images using matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(input_img2)
axes[0].set_title('Original')
axes[0].axis('off')

axes[1].imshow(input_rot1)
axes[1].set_title('Rotated Image')
axes[1].axis('off')

plt.show()

# Display the original and gausian noise images using matplotlib
# Add Gaussian Noise to the image
noise = iaa.AdditiveGaussianNoise(10, 40)
input_noise = noise.augment_image(input_img)
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
noise=iaa.AdditiveGaussianNoise(10,40)
input_noise=noise.augment_image(input_img)
images_list=[input_img, input_noise]
labels = ['Original', 'Gaussian Noise Image']
ipyplot.plot_images(images_list,labels=labels,img_width=180)

axes[0].imshow(input_img2)
axes[0].set_title('Original')
axes[0].axis('off')

axes[1].imshow(input_noise)
axes[1].set_title('Gaussian Noise Image')
axes[1].axis('off')

plt.show()