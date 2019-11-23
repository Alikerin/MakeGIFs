
'''
Make a directory and put the pictures inside
Number the pictures in an ascending order e.g 1, 2, 3, 4 etc.
'''
import os
from PIL import Image
import tensorflow as tf

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

class TensorboardMakeGIF:
    def __init__(self, event_file, video_name):
        self.event_file = event_file
        self.video_name = video_name

        self.events = [value.tag for event in tf.compat.v1.train.summary_iterator(self.event_file) for value in event.summary.value]

        assert self.video_name in self.events, '{} not in Event file'.format(self.video_name)


    def makegif(self, output_file_name, duration_of_frame, no_of_loops):
        assert (output_file_name[-4:] == '.gif'), 'Expects file extension to be .gif but got {}'.format(output_file_name)
        self.x = 0
        for event in tf.compat.v1.train.summary_iterator(self.event_file):
            for value in event.summary.value:
                if value.tag == self.video_name:
                    self.x = value
        self.image_string = self.x.image.encoded_image_string
        self.image = tf.image.decode_gif(self.image_string)
        self.image = self.image.numpy()

        self.image_list = [Image.fromarray(self.image[i]) for i in range(self.image.shape[0])]

        self.image_list[0].save(output_file_name, save_all=True, append_images=self.image_list[1:], optimize=False, duration=duration_of_frame, loop=no_of_loops)
