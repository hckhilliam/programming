import re


def part1(data):
    rows = parse_data(data)
    unparsed_rules = {}
    rules = {}

    i = 0
    while rows[i] != '':
        parts = rows[i].split(' ')
        ruleNum = int(parts[0][:-1])
        unparsed_rules[ruleNum] = parts[1:]
        i += 1

    build_rule(0, rules, unparsed_rules)

    i += 1
    rule = '^{}$'.format(rules[0])
    num_matches = 0
    while i < len(rows):
        if bool(re.search(rule, rows[i])):
            num_matches += 1
        i += 1

    return num_matches


def build_rule(ruleNum, rules, unparsed_rules, part=1):
    if part == 2:
        if ruleNum == 8:
            return '({}+)'.format(build_rule(42, rules, unparsed_rules, part))
        elif ruleNum == 11:
            # Sad, regex doesn't support something like this.
            forty_two = build_rule(42, rules, unparsed_rules, part)
            thirty_one = build_rule(31, rules, unparsed_rules, part)
            # Guessing it will be used up to 5 times.
            # Absolutely disgusting.
            return '(({}{})|({}{}{}{})|({}{}{}{}{}{})|({}{}{}{}{}{}{}{})|({}{}{}{}{}{}{}{}{}{}))'.format(
                forty_two, thirty_one,
                forty_two, forty_two, thirty_one, thirty_one,
                forty_two, forty_two, forty_two,
                thirty_one, thirty_one, thirty_one,
                forty_two, forty_two, forty_two, forty_two,
                thirty_one, thirty_one, thirty_one, thirty_one,
                forty_two, forty_two, forty_two, forty_two, forty_two,
                thirty_one, thirty_one, thirty_one, thirty_one, thirty_one
            )

    if ruleNum in rules:
        return rules[ruleNum]

    parts = unparsed_rules[ruleNum]

    # Messy, but reduces the amount of parentheses significantly.
    if len(parts) == 1 and parts[0].startswith('"'):
        rules[ruleNum] = parts[0][1:-1]
        return rules[ruleNum]

    rule = ''
    currRule = ''
    for p in parts:
        # Num.
        if p.isnumeric():
            num = int(p)
            currRule += build_rule(num, rules, unparsed_rules, part)
        # Pipe.
        else:
            rule = '({}){}'.format(currRule, p)
            currRule = ''
    rule += '({})'.format(currRule)

    rules[ruleNum] = '({})'.format(rule)
    return rules[ruleNum]


def part2(data):
    rows = parse_data(data)
    unparsed_rules = {}
    rules = {}

    i = 0
    while rows[i] != '':
        parts = rows[i].split(' ')
        ruleNum = int(parts[0][:-1])
        unparsed_rules[ruleNum] = parts[1:]
        i += 1

    build_rule(0, rules, unparsed_rules, part=2)

    i += 1
    rule = '^{}$'.format(rules[0])
    num_matches = 0
    while i < len(rows):
        if bool(re.search(rule, rows[i])):
            num_matches += 1
        i += 1

    return num_matches


def parse_data(data):
    rows = data.split('\n')
    return rows
