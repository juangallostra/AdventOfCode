def parse_input(input_file, to_int=False, single_value=False):
    with open(input_file) as f:
        measurements = [l.strip() for l in f.readlines()]
        if to_int:
            measurements = [int(m) for m in measurements]
        if single_value:
            return measurements[0]
    return measurements
