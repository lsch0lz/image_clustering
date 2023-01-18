import os

FLOWERS = []


def get_images(path):
    with os.scandir(path) as files:
        for file in files:
            if file.name.endswith(".jpg"):
                FLOWERS.append(os.path.join(path, file.name))
            elif file.name.endswith(".jpeg"):
                FLOWERS.append(os.path.join(path, file.name))
            elif file.name.endswith(".png"):
                FLOWERS.append(os.path.join(path, file.name))
    return FLOWERS
