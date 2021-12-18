def parse_input(input_file, to_int=False, single_value=False):
    with open(input_file) as f:
        measurements = [l.strip() for l in f.readlines()]
        if to_int:
            measurements = [int(m) for m in measurements]
        if single_value:
            return measurements[0]
    return measurements

def data_as_matrix_str(data):
    return '\n'.join(''.join(str(i) for i in l) for l in data)

def pad_data(data, value=0):
    padded = [[value for _ in range(len(data[0])+2)]]
    for row in data:
        padded.append([value] + row + [value])
    return padded + [[0 for _ in range(len(data[0])+2)]]


def unpad_data(data):
    return [[i for i in row[1:-1]] for row in data[1:-1]]
