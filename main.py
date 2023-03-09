import numpy as np
import matplotlib.pyplot as plt
import cv2


def load_image():
    blank_img = np.zeros((600,600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img, text='ABCDE', org=(50,300), fontFace=font, fontScale=5, color=(255,255,255), thickness=25)
    return blank_img

def display_img(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()

img = load_image();
# display_img(img)

""" 'Erosion' attacks the edges between foreground and background"""
kernel = np.ones((5,5), dtype=np.uint8)
result = cv2.erode(img, kernel, iterations=4)
# display_img(result)

""" 'Opening' does a good job of attacking background noise (erosion followed by dilation)"""
# img = load_image()
#
# # make a noise image
# white_noise = np.random.randint(low=0, high=2, size=(600,600))
# white_noise = white_noise * 255
# display_img(white_noise)
#
# # combine our noise with the original image
# noise_img = white_noise + img
# display_img(noise_img)
#
# # eliminate the noise
# opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernel)
# display_img(opening)

""" 'Closing' Remove noise from foreground"""
# img = load_image()
# black_noise = np.random.randint(low=0, high=2, size=(600,600))
# black_noise = black_noise * -255
# display_img(black_noise)
#
# black_noise_img = black_noise + img
# display_img(black_noise)
#
# # brings anything in the img matrix that was below zero, back to zero
# black_noise_img[black_noise_img==-255] = 0
# display_img(black_noise_img)
#
# close = cv2.morphologyEx(black_noise_img, cv2.MORPH_CLOSE, kernel)
# display_img(close)

""" 'Morphological gradient' this is a type of edge detection, attempts to find the space between erosion and dilation """
img = load_image()
display_img(img)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
display_img(gradient)


