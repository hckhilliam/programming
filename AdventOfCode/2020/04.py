
def part1(data):
    rows = parse_data(data)
    valid = 0
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for r in rows:
        v = True
        for k in keys:
            if k not in r:
                v = False
                break
        if v:
            valid += 1
    return valid


def part2(data):
    rows = parse_data(data)
    valid = 0
    for r in rows:
        try:
            if 'byr' not in r or not (1920 <= int(r['byr']) <= 2002):
                continue
            if 'iyr' not in r or not (2010 <= int(r['iyr']) <= 2020):
                continue
            if 'eyr' not in r or not (2020 <= int(r['eyr']) <= 2030):
                continue
            if 'hgt' not in r:
                continue
            else:
                t = r['hgt'][-2:]
                h = int(r['hgt'][:-2])
                if t == 'cm' and not (150 <= h <= 193):
                    continue
                elif t == 'in' and not (59 <= h <= 76):
                    continue
                elif t != 'in' and t != 'cm':
                    continue
            if 'hcl' not in r:
                continue
            elif r['hcl'][0] != '#' or len(r['hcl']) != 7:
                continue
            else:
                v = True
                for ch in r['hcl'][1:]:
                    if not (ch.isdigit() or 'a' <= ch <= 'f'):
                        v = False
                        break
                if not v:
                    continue
            if 'ecl' not in r or r['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                continue
            if 'pid' not in r or len(r['pid']) != 9:
                continue
            else:
                v = True
                for ch in r['pid']:
                    if not ch.isdigit():
                        v = False
                        break
                if not v:
                    continue
            valid += 1
        except Exception:
            pass
    return valid


def parse_data(data):
    rows = data.split('\n')
    parts = []
    res = []
    for r in rows:
        if r == '':
            vals = {}
            for p in parts:
                pp = p.split(' ')
                for ppp in pp:
                    pppp = ppp.split(':')
                    vals[pppp[0]] = pppp[1]
            res.append(vals)
            parts = []
        else:
            parts.append(r)
    vals = {}
    for p in parts:
        pp = p.split(' ')
        for ppp in pp:
            pppp = ppp.split(':')
            vals[pppp[0]] = pppp[1]
    res.append(vals)
    return res
