import sys
ARROW = " --> "

"""
Example of time:
00:00:12,028 --> 00:00:13,774

"""
def is_line_time(line):
    return ARROW in line

def mod_time_line(line, diff_min, dif_sec):
    # Break line
    line_back = []

    part_line = line.split(ARROW);
    for time_format in part_line:
        time_particales = time_format.split(":")
        time_particales[1] = str(int(time_particales[1])+ diff_min)
        line_back.append(":".join(time_particales))
    # Sort line back
    return ARROW.join(line_back)

def fix_all():
    new_file = ""
    with open(sys.argv[1], "r") as subtitle_f:
        for l in subtitle_f.readlines():
            if is_line_time(l):
                new_file = new_file + mod_time_line(l, 22,23)
            else:
                new_file = new_file + l

    with open(sys.argv[2], "w") as new_sub:
        new_sub.write(new_file)


fix_all()
