# Define dictionary for seven segment display digits
seven_segment_dict = {
    "0": "1111110",
    "1": "0100100",
    "2": "1011011",
    "3": "1101101",
    "4": "0101111",
    "5": "1101010",
    "6": "1111010",
    "7": "0100101",
    "8": "1111111",
    "9": "1101111"
}

# Define dictionary for mirror images
mirror_image_dict = {
    "S": seven_segment_dict,
    "L": {k: v[::-1] for k, v in seven_segment_dict.items()},
    "R": {k: v[::-1] for k, v in seven_segment_dict.items()},
    "U": {k: v.translate(str.maketrans("01", "10")) for k, v in seven_segment_dict.items()},
    "D": {k: v.translate(str.maketrans("01", "10")) for k, v in seven_segment_dict.items()},
}


def main():
    digits = input()  # String of digits
    side = input()  # String of mirror positions

    output = ""
    for digit, mirror_position in zip(digits, side):
        if mirror_position in "SL":
            output += mirror_image_dict[mirror_position][digit]
        else:
            output += seven_segment_dict[digit]

    print(output)


if __name__ == "__main__":
    main()
