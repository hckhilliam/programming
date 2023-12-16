def to_array(rows):
    return [list(r) for r in rows]

def p_rows(rows):
    for r in rows:
        print(''.join(r))
    print()
