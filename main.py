from utils import *

def main():
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('--image_dir', '-imgdir', type=str)
    parser.add_argument('--output_file_name', '-fn', type=str, required=True)
    parser.add_argument('--duration_of_frame', '-dur', type=int, default=60)
    parser.add_argument('--no_of_loops', '-lps', type=int, default=3)
    parser.add_argument('--event_file', '-evf', type=str)
    parser.add_argument('--video_name', '-vn', type=str)
    parser.add_argument('--type', choices=['1', '2'], help='1 for image_dir and 2 for event_file')
    args = parser.parse_args()

    #convert args to dictionary
    params = vars(args)
    if params['type'] == '1':
        assert params['image_dir'] != None, 'Option 1 requires image_dir argument'
        gif_object = MakeGIF(params['image_dir'])
        gif_object.makegif(params['output_file_name'], params['duration_of_frame'], params['no_of_loops'])

    if params['type'] == '2':
        assert params['event_file'] != None, 'Option 1 requires image_dir argument'
        gif_object = TensorboardMakeGIF(params['event_file'], params['video_name'])
        gif_object.makegif(params['output_file_name'], params['duration_of_frame'], params['no_of_loops'])

if __name__ == '__main__':
    main()
