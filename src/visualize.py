import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def view_cluster(clusters):
    plt.figure(figsize=(25, 25))
    files = clusters[cluster]

    if len(files) > 30:
        files = files[:29]

    for index, file in enumerate(files):
        plt.subplot(10, 10, index=1)
        img = Image.open(file)
        img = np.array(img)

        plt.imshow(img)
        plt.axis("off")
