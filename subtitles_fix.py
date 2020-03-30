import sys
import argparse

ARROW = " --> "

"""
Example of time:
00:00:12,028 --> 00:00:13,774

"""

def valid_time(s):
    if len(s.split(":")) != 2:
        msg = "Not a valid time: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)
    return s.split(":")

def parse_argumnets():
    """
    :return: arguments
    """
    parser = argparse.ArgumentParser(
        description='fix subtitle offset')
    parser.add_argument('subtitles_file', type=str, help="Path to file")
    parser.add_argument("-n", "--new_file", dest="new_file", type=str, default=None,
                        help="new file to create, if not, overide subtitle file")
    
    parser.add_argument("-t", "--time",  help="Time to add - format MM:SS", 
                    required=True, type=valid_time)
    return parser.parse_args()

def is_line_time(line):
    return ARROW in line

def modify_time_line(line, time):
    # Break line
    line_back = []

    part_line = line.split(ARROW);
    for time_format in part_line:
        time_particales = time_format.split(":")
        time_particales[1] = str(int(time_particales[1]) + int(time[1]))
        line_back.append(":".join(time_particales))
        # TODO: add seconds
    # Sort line back
    return ARROW.join(line_back)

def main():
    args = parse_argumnets()
    new_file = ""
    with open(args.subtitles_file, "r") as subtitle_f:
        for l in subtitle_f.readlines():
            if is_line_time(l):
                new_file = new_file + modify_time_line(l, args.time)
            else:
                new_file = new_file + l

    result_file = args.new_file if args.new_file else args.subtitles_file
    with open(result_file, "w") as new_sub:
        new_sub.write(new_file)

if __name__ == "__main__":
    main()