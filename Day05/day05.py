# First, let's read the uploaded input file and parse the data
file_path = 'Java/advent_code_2023/Advent_Code_2023/Day05/input.txt'

def map_value(value, mapping):
    """
    Map a single value from the source to the destination using the provided mapping.
    If the value is not in the mapping, it maps to itself.
    """
    for dest_start, src_start, length in mapping:
        if src_start <= value < src_start + length:
            return dest_start + (value - src_start)
    return value


def find_lowest_location(seeds, maps):
    """
    Find the lowest location number that corresponds to any of the initial seed numbers.
    """
    lowest_location = float('inf')

    for seed in seeds:
        value = seed
        for map in maps:
            value = map_value(value, map)

        lowest_location = min(lowest_location, value)

    return lowest_location



def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extracting the initial seed numbers
    seeds = list(map(int, lines[0].strip().split(": ")[1].split()))

    # Parsing the maps
    maps = []
    current_map = []
    for line in lines[1:]:
        if 'map:' in line:
            if current_map:
                maps.append(current_map)
                current_map = []
        else:
            parts = line.strip().split()
            if parts:
                current_map.append(tuple(map(int, parts)))
    
    maps.append(current_map)  # Adding the last map

    return seeds, maps

# Parse the input file
seeds, maps = parse_input(file_path)

# Find the lowest location number using the previously defined functions
lowest_location = find_lowest_location(seeds, maps)
print(lowest_location)

