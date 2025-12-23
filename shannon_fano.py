from collections import Counter

def shannon_fano_encoding(data):
    freq = Counter(data)
    items = sorted(freq.items(), key=lambda x: -x[1])
    codes = {}

    def recurse(symbols, prefix=''):
        if len(symbols) == 1:
            codes[symbols[0][0]] = prefix or '0'
            return
        total = sum(f[1] for f in symbols)
        split = 0
        acc = 0
        for i in range(len(symbols)):
            acc += symbols[i][1]
            if acc >= total / 2:
                split = i + 1
                break
        recurse(symbols[:split], prefix + '0')
        recurse(symbols[split:], prefix + '1')

    recurse(items)
    return codes

def encode_message(message, codes):
    return ''.join(codes[c] for c in message)

def decode_message(bitstring, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    temp = ''
    result = ''
    for b in bitstring:
        temp += b
        if temp in reverse_codes:
            result += reverse_codes[temp]
            temp = ''
    return result
