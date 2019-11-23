# MakeGIFs
This repository contains Python code for making GIF from a Tensorboard event file or a directory containing images in a numerical order such as 1.png, 2.png, 3.png etc.

To make a GIF from image directory run main.py with the required arguments

#### python main.py --image_dir directory_containing_numbered_images --output_file_name output_filename.gif --type 1

To make a GIF from Tensorboard event file run main.py with the required arguments

#### python main.py --event_file path_to_event_file --video_name name_of_logged_video --output_file_name output_filename.gif --type 2

optional arguments:
--duration_of_frame: duration of each frame in the GIF
--no_of_loops: number of times the GIF should loop
