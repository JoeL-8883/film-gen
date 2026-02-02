import os
import argparase

def get_urls(num_urls=0, startpoint=0):
    """
    Extract a specified number of images from a list of image URLs.
    """

    dir = "urls/all.txt"

    with open(dir, "r") as f:
        if num_urls == 0:
            with open(f"urls/url_{num_urls}.txt", "w") as f_out:
                for line in f:
                    f_out.write(line + "\n")
        else:
            if startpoint > 0:
                output_filename = f"urls/url_{startpoint}_{num_urls + startpoint}.txt"
            else:
                output_filename = f"urls/url_{num_urls}.txt"
            with open(output_filename, "w") as f_out:
                # Skip the first lines
                for _ in range(startpoint):
                    f.readline()
                
                for _ in range(num_urls):
                    url = f.readline().strip()
                    f_out.write(url + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_urls", type=int, default=500, help="The number of urls to be written to a subset txt file")
    parser.add_argument("startpoint", default=0, help="The startpoint of the all.txt file, use if you are downloading the data in chunks.")
    args = parser.parse_args()
    get_urls(args.num_urls, args.startpoint)
