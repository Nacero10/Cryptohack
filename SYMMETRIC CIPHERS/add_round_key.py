
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    return [[s[i][j] ^ k[i][j] for j in range(4)] for i in range(4)]


print(add_round_key(state, round_key))


matrix=[[99, 114, 121, 112], [116, 111, 123, 114], [48, 117, 110, 100], [107, 51, 121, 125]]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return [matrix[i][j] for i in range(4) for j in range(4)]




print(''.join(chr(i) for i in matrix2bytes(matrix)))



