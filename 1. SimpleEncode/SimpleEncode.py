import random


def generate_key(size: int) -> None:
    arr = [num for num in range(size)]
    with open('key.txt', 'wb') as key:
        for _ in range(size):
            elem = random.choice(arr)
            key.write(elem.to_bytes(1, 'big'))  # key.write(str(elem) + ' ') 'w'
            arr.remove(elem)


def get_key(filename: str) -> list:
    with open(filename, 'rb') as key:
        ans = [int(elem) for elem in key.read()]  # key.read().split() 'r'
    return ans


def get_reverse_key(original: list, size: int) -> list:
    rev = [0] * size
    for key, value in enumerate(original):
        rev[value] = key
    return rev


def get_data(filename: str) -> bytes:
    with open(filename, 'rb') as file:
        arr = file.read()
    return arr


def show_freq(arr: bytes) -> list:
    count = len(arr)
    frequencies = [0] * 256
    for b in arr:
        frequencies[b] += 1
    print(f'file size in bytes: {count}')
    for index, freq in enumerate(frequencies):
        if freq != 0:
            print(f'byte {index}: found {freq} times')
    return frequencies


def encode_simple(*, file_to_encode: str, file_encoded: str) -> None:
    b_arr = get_data(file_to_encode)
    show_freq(b_arr)
    k = get_key('key.txt')
    coded = bytearray()
    for b in b_arr:
        coded.append(k[b])
    with open(file_encoded, 'wb') as e:
        e.write(coded)
    print('successful encode')


def decode_simple(*, file_to_decode: str, file_decoded: str) -> None:
    b_arr = get_data(file_to_decode)
    k = get_key('key.txt')
    reverse_key = get_reverse_key(k, 256)
    decoded = bytearray()
    for b in b_arr:
        decoded.append(reverse_key[b])
    with open(file_decoded, 'wb') as e:
        e.write(decoded)
    print('successful decode')


if __name__ == '__main__':
    # generate_key(256)
    encode_simple(file_to_encode='input-files/file.txt', file_encoded='output-files/temp.txt')
    decode_simple(file_to_decode='output-files/temp.txt', file_decoded='output-files/newfile.txt')
