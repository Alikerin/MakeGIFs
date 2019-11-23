from utils import MakeGIF

def main():
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('--image_dir', '-imgdir', type=str, required=True)
    parser.add_argument('--output_file_name', '-fn', type=str, required=True)
    parser.add_argument('--duration_of_frame', '-dur', type=int, default=60)
    parser.add_argument('--no_of_loops', '-lps', type=int, default=3)

    args = parser.parse_args()

    #convert args to dictionary
    params = vars(args)

    gif_object = MakeGIF(params['image_dir'])

    gif_object.makegif(params['output_file_name'], params['duration_of_frame'], params['no_of_loops'])

if __name__ == '__main__':
    main()
