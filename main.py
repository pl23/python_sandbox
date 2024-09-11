import csv

game_map = {}

def read_chunk(game_map, path, cords = None):
    """Reads a chunk of a tile map from a CSV file.

    Args:
        map (dict): The map dictionary to store the chunk.
        path (str or tuple): The path to the CSV file or a tuple containing the base path and file extension.
        cords (tuple, optional): The coordinates of the chunk. Defaults to None.

    Returns:
        dict: The updated map dictionary.
    """
    if isinstance(path, str):
        file_path = path
    else:
        file_path = f"{path[0]}{cords[0]},{cords[1]}{path[1]}"
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        chunk = [row for row in reader]
    game_map[f"{cords[0]},{cords[1]}"] = chunk
    return game_map

def write_chunk(game_map, chunk, path, cords = None):
    """Writes a chunk of a tile map to a CSV file.

    Args:
        map (dict): The map dictionary.
        chunk (list): The chunk of tiles to write.
        path (str or tuple): The path to the CSV file or a tuple containing the base path and file extension.
        cords (tuple, optional): The coordinates of the chunk. Defaults to None.

    Returns:
        dict: The updated map dictionary.
    """
    if isinstance(path, str):
        file_path = path
    else:
        file_path = f"{path[0]}{cords[0]},{cords[1]}{path[1]}"
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(chunk)
    game_map[f"{cords[0]},{cords[1]}"] = file_path
    return game_map

