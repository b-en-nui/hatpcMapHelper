import math

FILEPATH = 'levelData/tutorial1.txt'
CHUNK_DIM = 16
BLOCK_DIM = 21

# CHUNKS = [
#     {
#         'data': [],
#         'height': CHUNK_DIM,
#         'width': CHUNK_DIM,
#         'x': 0,
#         'y': 0
#     }
# ]

def map_coord_to_chunk_coord(x, y):
    chunk_x = 0
    chunk_y = 0
    while x >= CHUNK_DIM:
        x -= CHUNK_DIM
        chunk_x += CHUNK_DIM
    while y >= CHUNK_DIM:
        y -= CHUNK_DIM
        chunk_y += CHUNK_DIM
    return chunk_x, chunk_y, x, y


def map_coord_to_block_index(x, y):
    while x >= BLOCK_DIM:
        x -= BLOCK_DIM
    while y >= BLOCK_DIM:
        y -= BLOCK_DIM
    return 1 + (BLOCK_DIM * y) + x


def generate_chunk_key(x, y):
    return '%s_%s' % (str(x), str(y))


def process_map():

    map_height = 0
    map_width = 0

    created_chunks = {}

    with open(FILEPATH, 'r') as file:
        for line in file:
            for i in range(len(line)):
                chunk_x, chunk_y, x, y = map_coord_to_chunk_coord(i, map_height)
                chunk_key = generate_chunk_key(chunk_x, chunk_y)
                if chunk_key not in created_chunks:
                    created_chunks[chunk_key] = {
                        'data': [0] * (CHUNK_DIM * CHUNK_DIM),
                        'height': CHUNK_DIM,
                        'width': CHUNK_DIM,
                        'x': chunk_x,
                        'y': chunk_y
                    }
                if line[i] == ' ':
                    created_chunks[chunk_key]['data'][CHUNK_DIM * y + x] = 0
                elif line[i] == 'x':
                    created_chunks[chunk_key]['data'][CHUNK_DIM*y + x] = map_coord_to_block_index(i, map_height)
                else:
                    created_chunks[chunk_key]['data'][CHUNK_DIM * y + x] = 0

            row_len = len(line)
            if row_len > map_width:
                map_width = row_len
            map_height += 1

    chunks_wide = math.ceil(map_width / CHUNK_DIM)
    chunks_tall = math.ceil(map_height / CHUNK_DIM)

    data_json = list(created_chunks.values())

    print('Map height: %s, Map width: %s' % (map_height, map_width))
    print('Chunk dimensions: %s x %s' % (chunks_wide, chunks_tall))
    print(data_json)

    for chunk in data_json:
        print('<chunk x="%s" y="%s" width="%s" height="%s">%s</chunk>' % (chunk['x'], chunk['y'], chunk['width'], chunk['height'], ','.join(map(str, chunk['data']))))


if __name__ == '__main__':
    process_map()


# chunks = [
#     {
#      "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
#                 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
#                 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
#                 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
#                 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
#                 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121],
#      "height":16,
#      "width":16,
#      "x":0,
#      "y":0
#     }
# ]