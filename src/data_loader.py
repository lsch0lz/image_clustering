import os


def get_images(path):
    image_path = []
    with os.scandir(path) as files:
        for file in files:
            if file.name.endswith(".jpg"):
                image_path.append(os.path.join(path, file.name))
            elif file.name.endswith(".jpeg"):
                image_path.append(os.path.join(path, file.name))
            elif file.name.endswith(".png"):
                image_path.append(os.path.join(path, file.name))

    return image_path
