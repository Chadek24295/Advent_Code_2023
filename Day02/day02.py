def is_game_possible(draws, max_cubes):
    for draw in draws:
        for color, count in draw.items():
            if count > max_cubes[color]:
                return False
    return True

def process_games(lines):
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    possible_games_sum = 0

    for line in lines:
        line = line.strip()  # Remove any trailing newline or whitespace
        parts = line.split(': ')
        game_id = int(parts[0].split(' ')[1])
        draws_data = parts[1].split('; ')
        draws = []

        for draw_data in draws_data:
            draw_counts = {'red': 0, 'green': 0, 'blue': 0}
            for color_data in draw_data.split(', '):
                count, color = color_data.split(' ')
                draw_counts[color.strip()] += int(count)  # Strip potential whitespace in color name
            draws.append(draw_counts)

        if is_game_possible(draws, max_cubes):
            possible_games_sum += game_id

    return possible_games_sum

# Read the file and process the game
with open("Advent_Code_2023/game_data.txt", 'r') as file:
    lines = file.readlines()

sum_of_possible_game_ids = process_games(lines)
print(f"Sum of IDs of possible games: {sum_of_possible_game_ids}")
