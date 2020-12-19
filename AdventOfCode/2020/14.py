def part1(data):
    rows = parse_data(data)
    mask = None
    ret = {}
    for r in rows:
        if r.startswith('mask'):
            mask = r.split(' = ')[1]
        else:
            parts = r.split(' = ')
            num = bin(int(parts[1]))[2:]
            addr = parts[0][parts[0].find('[') + 1:parts[0].find(']')]
            final = ['0' for i in range(len(mask))]
            j = len(final) - 1
            i = len(num) - 1
            while i >= 0:
                final[j] = num[i]
                j -= 1
                i -= 1
            for i, m in enumerate(mask):
                if m != 'X':
                    final[i] = m
            ret[addr] = int(''.join(final), 2)
    return sum(ret.values())


def part2(data):
    rows = parse_data(data)
    mask = None
    ret = {}
    for r in rows:
        if r.startswith('mask'):
            mask = r.split(' = ')[1]
        else:
            parts = r.split(' = ')
            num = int(parts[1])
            addr = bin(int(parts[0][parts[0].find('[') + 1:parts[0].find(']')]))[2:]
            final = ['0' for i in range(len(mask))]
            j = len(final) - 1
            i = len(addr) - 1
            while i >= 0:
                final[j] = addr[i]
                j -= 1
                i -= 1
            all_addrs = get_all_addrs(final, mask)
            for ad in all_addrs:
                ret[int(ad, 2)] = num
    return sum(ret.values())


def get_all_addrs(final, mask):
    if len(mask) <= 0:
        return ['']
    addrs = get_all_addrs(final[1:], mask[1:])
    new_addrs = []
    for addr in addrs:
        if mask[0] == 'X':
            new_addrs.append('1' + addr)
            new_addrs.append('0' + addr)
        elif mask[0] == '1':
            new_addrs.append('1' + addr)
        else:
            new_addrs.append(final[0] + addr)
    return new_addrs


def parse_data(data):
    rows = data.split('\n')
    return rows
