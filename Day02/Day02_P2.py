def calculate_minimum_set_power(draws):
    max_counts = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        for color, count in draw.items():
            if count > max_counts[color]:
                max_counts[color] = count
    return max_counts['red'] * max_counts['green'] * max_counts['blue']

def process_games_for_power(lines):
    total_power_sum = 0

    for line in lines:
        line = line.strip()
        parts = line.split(': ')
        draws_data = parts[1].split('; ')
        draws = []

        for draw_data in draws_data:
            draw_counts = {'red': 0, 'green': 0, 'blue': 0}
            for color_data in draw_data.split(', '):
                count, color = color_data.split(' ')
                draw_counts[color.strip()] += int(count)
            draws.append(draw_counts)

        total_power_sum += calculate_minimum_set_power(draws)

    return total_power_sum

# Read the file and process the games

with open("Advent_Code_2023/Day02/game_data.txt", 'r') as file:
    lines = file.readlines()

sum_of_powers = process_games_for_power(lines)
print(f"Sum of the power of the minimum sets of cubes: {sum_of_powers}")
