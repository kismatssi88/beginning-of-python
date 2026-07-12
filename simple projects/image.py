import numpy as np
from PIL import Image

# -----------------------------
# Load Image
# -----------------------------
image = Image.open("input.jpg")
img = np.array(image)

print("Image Shape:", img.shape)

# -----------------------------
# 1. Grayscale
# -----------------------------
gray = img.mean(axis=2).astype(np.uint8)
Image.fromarray(gray).save("gray.jpg")

# -----------------------------
# 2. Negative Image
# -----------------------------
negative = 255 - img
Image.fromarray(negative.astype(np.uint8)).save("negative.jpg")

# -----------------------------
# 3. Brightness Increase
# -----------------------------
bright = np.clip(img + 50, 0, 255)
Image.fromarray(bright.astype(np.uint8)).save("bright.jpg")

# -----------------------------
# 4. Brightness Decrease
# -----------------------------
dark = np.clip(img - 50, 0, 255)
Image.fromarray(dark.astype(np.uint8)).save("dark.jpg")

# -----------------------------
# 5. Contrast Increase
# -----------------------------
contrast = np.clip(img * 1.5, 0, 255)
Image.fromarray(contrast.astype(np.uint8)).save("contrast.jpg")

# -----------------------------
# 6. Horizontal Flip
# -----------------------------
flip_h = img[:, ::-1]
Image.fromarray(flip_h.astype(np.uint8)).save("flip_horizontal.jpg")

# -----------------------------
# 7. Vertical Flip
# -----------------------------
flip_v = img[::-1]
Image.fromarray(flip_v.astype(np.uint8)).save("flip_vertical.jpg")

# -----------------------------
# 8. Rotate 90 Degrees
# -----------------------------
rotate = np.rot90(img)
Image.fromarray(rotate.astype(np.uint8)).save("rotated.jpg")

# -----------------------------
# 9. Crop Center
# -----------------------------
h, w = img.shape[:2]

crop = img[h//4:3*h//4, w//4:3*w//4]
Image.fromarray(crop.astype(np.uint8)).save("crop.jpg")

bw = np.where(gray > 128, 255, 0).astype(np.uint8)
Image.fromarray(bw).save("black_white.jpg")

noise = np.random.randint(-30, 31, img.shape)
noisy = np.clip(img + noise, 0, 255)
Image.fromarray(noisy.astype(np.uint8)).save("noisy.jpg")


red = img.copy()
red[:, :, 1] = 0
red[:, :, 2] = 0
Image.fromarray(red.astype(np.uint8)).save("red.jpg")

green = img.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0
Image.fromarray(green.astype(np.uint8)).save("green.jpg")

blue = img.copy()
blue[:, :, 0] = 0
blue[:, :, 1] = 0
Image.fromarray(blue.astype(np.uint8)).save("blue.jpg")


mirror = np.concatenate((img, img[:, ::-1]), axis=1)
Image.fromarray(mirror.astype(np.uint8)).save("mirror.jpg")

print("\nAll images have been created successfully!")