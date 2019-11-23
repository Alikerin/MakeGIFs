
'''
Make a directory and put the pictures inside
Number the pictures in an ascending order e.g 1, 2, 3, 4 etc.
'''
import os
from PIL import Image

class MakeGIF:
    def __init__(self, image_dir):
        images = os.listdir(image_dir)
        images.sort()
        self.image_names = images
        self.image_dir = image_dir
        self.images = []

    def makegif(self, output_file_name, duration_of_frame, no_of_loops):

        assert (output_file_name[-4:] == '.gif'), 'Expects file extension to be .gif but got {}'.format(output_file_name)

        for name in self.image_names:
            self.images.append(Image.open(os.path.join(self.image_dir, name)))
        self.images[0].save(output_file_name, save_all=True, append_images=self.images[1:], optimize=False, duration=duration_of_frame, loop=no_of_loops)
