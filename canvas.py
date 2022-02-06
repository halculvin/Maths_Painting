import numpy as np
from PIL import Image


class Canvas:
    """
    Object where all shapes are going to be drawn
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3D numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path):
        """
        Converts the current array into an image file
        :param image_path: Image path
        :return: an Image
        """
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)