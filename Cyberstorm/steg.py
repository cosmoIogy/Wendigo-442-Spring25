import sys

SENTINEL = bytearray([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])

def parse_args():
    args = sys.argv[1:]
    config = {
        'store': False,
        'retrieve': False,
        'bit': False,
        'byte': False,
        'offset': 0,
        'interval': 1,
        'wrapper': None,
        'hidden': None
    }

    for arg in args:
        if arg == '-s':
            config['store'] = True
        elif arg == '-r':
            config['retrieve'] = True
        elif arg == '-b':
            config['bit'] = True
        elif arg == '-B':
            config['byte'] = True
        elif arg.startswith('-o'):
            config['offset'] = int(arg[2:])
        elif arg.startswith('-i'):
            config['interval'] = int(arg[2:])
        elif arg.startswith('-w'):
            config['wrapper'] = arg[2:]
        elif arg.startswith('-h'):
            config['hidden'] = arg[2:]

    if not config['wrapper']:
        sys.exit("Error: Wrapper file is required (-w<filename>).")

    if config['store'] and not config['hidden']:
        sys.exit("Error: Hidden file is required for storing (-h<filename>).")

    if not (config['store'] ^ config['retrieve']):
        sys.exit("Error: Must specify either store (-s) or retrieve (-r).")

    if not (config['bit'] ^ config['byte']):
        sys.exit("Error: Must specify bit (-b) or byte (-B) mode.")

    return config

def store_byte_mode(wrapper, hidden, offset, interval):
    for byte in hidden + SENTINEL:
        wrapper[offset] = byte
        offset += interval
    return wrapper

def store_bit_mode(wrapper, hidden, offset, interval):
    data = hidden + SENTINEL
    for byte in data:
        for _ in range(8):
            wrapper[offset] &= 0b11111110
            wrapper[offset] |= (byte & 0b10000000) >> 7
            byte = (byte << 1) & 0xFF
            offset += interval
    return wrapper

def retrieve_byte_mode(wrapper, offset, interval):
    result = bytearray()
    match = bytearray()
    while offset < len(wrapper):
        byte = wrapper[offset]
        offset += interval

        match.append(byte)
        if match == SENTINEL[:len(match)]:
            if match == SENTINEL:
                return result
        else:
            result.extend(match)
            match.clear()
    return result

def retrieve_bit_mode(wrapper, offset, interval):
    result = bytearray()
    match = bytearray()
    while offset + 8 * interval <= len(wrapper):
        byte = 0
        for i in range(8):
            byte |= (wrapper[offset] & 0b1)
            if i < 7:
                byte <<= 1
            offset += interval

        match.append(byte)
        if match == SENTINEL[:len(match)]:
            if match == SENTINEL:
                return result
        else:
            result.extend(match)
            match.clear()
    return result

def main():
    config = parse_args()

    try:
        with open(config['wrapper'], 'rb') as f:
            wrapper = bytearray(f.read())
    except FileNotFoundError:
        sys.exit(f"Error: Wrapper file {config['wrapper']} not found.")

    hidden = bytearray()
    if config['store']:
        try:
            with open(config['hidden'], 'rb') as f:
                hidden = bytearray(f.read())
        except FileNotFoundError:
            sys.exit(f"Error: Hidden file {config['hidden']} not found.")

    if config['store']:
        if config['bit']:
            wrapper = store_bit_mode(wrapper, hidden, config['offset'], config['interval'])
        else:
            wrapper = store_byte_mode(wrapper, hidden, config['offset'], config['interval'])
        sys.stdout.buffer.write(wrapper)

    elif config['retrieve']:
        if config['bit']:
            extracted = retrieve_bit_mode(wrapper, config['offset'], config['interval'])
        else:
            extracted = retrieve_byte_mode(wrapper, config['offset'], config['interval'])
        sys.stdout.buffer.write(extracted)

if __name__ == "__main__":
    main()
