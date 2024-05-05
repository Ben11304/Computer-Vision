import cv2
import numpy as np
import skfuzzy as fuzz

def fuzzy_C(image,n_classes):
    # Flatten the image array and normalize
    data = image.flatten()
    data_norm = data / 255.0  # Normalize to [0, 1]

    # Reshape data for clustering
    data_reshaped = data_norm.reshape((1, -1))

    # Specify the number of clusters
    clusters = n_classes

    # Apply Fuzzy C-means
    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
        data_reshaped, clusters, 2, error=0.005, maxiter=1000, init=None)

    # Find the cluster membership for each pixel

    # Map back to image shape
    segmented_image = cluster_membership.reshape(image.shape)

    # Convert the segmented image into uint8 (for displaying)
    segmented_image = np.uint8(255 * segmented_image / clusters)
    return segmented_image

def AdaptThresh_image
frame_gray= cv2.adaptiveThreshold(
    blur,                # source image
    255,                       # max value to use with the THRESH_BINARY
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, # adaptive method, Gaussian weighting
    cv2.THRESH_BINARY,         # threshold type
    bl_sz,                        # block size: size of a pixel neighborhood used to calculate threshold value
    const                       # constant subtracted from the mean or weighted sum
    )