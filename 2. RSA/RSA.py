def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


def get_keys(*, first_simple: int, second_simple: int) -> list:
    n = first_simple * second_simple
    phi = (first_simple - 1) * (second_simple - 1)
    e = 257
    while nod(e, phi) != 1:
        e += 1
    for k in range(1, phi):
        d = (k * phi + 1) / e
        if int(d) == d:
            return [e, int(d), n]


def get_data_binary(filename: str) -> bytes:
    with open(filename, 'rb') as file:
        arr = file.read()
    return arr


def get_data_int(filename: str) -> list:
    with open(filename, 'rb') as file:
        elem = file.read(4)
        data = []
        while elem:
            data.append(int.from_bytes(elem, 'big'))
            elem = file.read(4)
        return data


def encode_rsa(*, file_to_encode: str, file_encoded: str, e: int, n: int) -> None:
    data = get_data_binary(file_to_encode)
    dct = {}
    with open(file_encoded, 'wb') as f:
        for b in data:
            if b not in dct:
                elem = pow(b, e, n)
                dct[b] = elem
            else:
                elem = dct[b]
            f.write(elem.to_bytes(4, 'big'))
    print('successful encode')


def decode_rsa(*, file_to_decode: str, file_decoded: str, d: int, n: int) -> None:
    data = get_data_int(file_to_decode)
    dct = {}
    with open(file_decoded, 'wb') as f:
        for b in data:
            if b not in dct:
                elem = pow(b, d, n)
                dct[b] = elem
            else:
                elem = dct[b]
            f.write(elem.to_bytes(1, 'big'))
    print('successful decode')

# prime nums: 809, 811
# open key: 2003, 656099
# secret key: 1307, 656099


if __name__ == '__main__':
    open_key, secret_key, key = get_keys(first_simple=7681, second_simple=9349)
    encode_rsa(file_to_encode='input-files/ТПП.pdf', file_encoded='output-files/temp.txt', e=open_key, n=key)
    decode_rsa(file_to_decode='output-files/temp.txt', file_decoded='output-files/new.pdf', d=secret_key, n=key)
