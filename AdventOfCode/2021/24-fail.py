from collections import defaultdict, deque
import functools
import math
import re
import pdb


DEBUG_LINES = {}
CURR_STATE = (0, 109)

OPERATOR_MAP = {
    'add': '+',
    'mul': '*',
    'div': '/',
    'mod': '%',
    'eql': '=='
}
DIGS = {f'a{i}' for i in range(14)}


class Solver(object):
    def __init__(self, rows, ai):
        self.ai = ai
        self.rows = rows
        self.extra_id = 1
        self.extra_variables = ['']
        self.curr_dig = 0
        self.debug_state = 0
        self.operator_mapping = {
            '+': self.simplify_add,
            '*': self.simplify_mult,
            '/': self.simplify_div,
            '%': self.simplify_mod,
            '==': self.simplify_eql,
            '!=': self.simplify_nql
        }
        self.variables = {
            'w': Solver.Expr(left=f'a{ai}', mapping=self.operator_mapping),
            'x': Solver.Expr(left='0', mapping=self.operator_mapping),
            'y': Solver.Expr(left='0', mapping=self.operator_mapping),
            'z': Solver.Expr(left=f'b{ai}', mapping=self.operator_mapping)
        }

    def solve(self):
        for i, r in enumerate(self.rows):
            self.debug_state = i
            instruction = r.split(' ')
            cmd = instruction[0]
            p = instruction[1]
            v1 = self.variables[instruction[1]]
            v2 = None
            if len(instruction) == 3:
                v2 = instruction[2]
                if v2 in self.variables:
                    v2 = self.variables[v2].deepcopy()
            if cmd == 'inp':
                self.variables[p] = Solver.Expr(
                    left=f'a{self.curr_dig}',
                    mapping=self.operator_mapping
                )
                self.curr_dig += 1
            else:
                self.variables[p] = Solver.Expr(
                    left=v1, right=v2, operator=OPERATOR_MAP[cmd],
                    mapping=self.operator_mapping
                )
            self.add_debug()()
            self.variables[p] = self.variables[p].simplify()
            self.add_debug()()
        print(self.ai)
        for k, v in self.variables.items():
            print(k)
            print(v)
        print(self.extra_variables)
        print()

    def simplify_add(self, expr):
        if expr.left == '0' and expr.right:
            expr.left = expr.right
            expr.right = None
            expr.operator = None
        elif expr.right == '0':
            expr.right = None
            expr.operator = None
        return expr

    def simplify_mult(self, expr):
        if expr.left == '0' or expr.right == '0':
            expr.left = '0'
            expr.right = None
            expr.operator = None
        elif expr.left == '1' and expr.right:
            expr.left = expr.right
            expr.right = None
            expr.operator = None
        elif expr.right == '1':
            expr.right = None
            expr.operator = None
        return expr
        # elif (
        #     (isinstance(expr.left, Solver.Expr) and expr.left.operator in {'==', '!='}) or
        #     (isinstance(expr.right, Solver.Expr) and expr.right.operator in {'==', '!='})
        # ):
        #     self.extra_variables.append(str(expr))
        #     expr.left = f'b{self.extra_id}'
        #     self.extra_id += 1
        #     expr.right = None
        #     expr.operator = None

    def simplify_div(self, expr):
        if expr.right == '1':
            expr.right = None
            expr.operator = None
        elif expr.left == '0':
            expr.right = None
            expr.operator = None
        # elif isinstance(expr.left, Solver.Expr):
        #     # Remove all multiplications of the mod value
        #     div_value = eval_expr(expr.right)
        #     if div_value:
        #         expr.left = self.reduce_all_mults_div(expr.left, div_value)
        return expr

    def reduce_all_mults_div(self, expr, div_value):
        if not isinstance(expr, Solver.Expr):
            return Solver.Expr(left=expr, right=str(div_value), operator='/', mapping=self.operator_mapping).simplify()

        if expr.operator == '*':
            left = eval_expr(expr.left)
            right = eval_expr(expr.right)
            reduced = None
            if left == div_value:
                reduced = expr.right
            elif right == div_value:
                reduced = expr.left
            if reduced:
                expr.left = reduced
                expr.right = None
                expr.operator = None
                return expr

        if expr.operator not in {None, '/', '==', '%'}:
            expr.left = self.reduce_all_mults_div(expr.left, div_value)
            expr.right = self.reduce_all_mults_div(expr.right, div_value)
            return expr.simplify()
        else:
            return Solver.Expr(left=expr, right=str(div_value), operator='/', mapping=self.operator_mapping)

    def simplify_mod(self, expr):
        if expr.left == '0':
            expr.left = '0'
            expr.right = None
            expr.operator = None
            return expr

        # Remove all multiplications of the mod value
        mod_value = eval_expr(expr.right)
        if mod_value:
            expr.left = self.reduce_all_mults(expr.left, mod_value)

        # Check if the var will actually be greater than the mod number
        vs, vb = get_variables(expr, self.extra_id)
        if len(vs) > 4 or vb:
            return expr

        values = {v: 9 for v in vs}
        j = -1
        while values[vs[0]] != 0:
            a_v1 = eval(get_expr(expr.left, values))
            a_v2 = eval(get_expr(expr.right, values))
            if a_v1 >= a_v2:
                return expr

            values[vs[j]] -= 1
            while j != -len(vs) and values[vs[j]] == 0:
                values[vs[j]] = 9
                j -= 1
                values[vs[j]] -= 1
            j = -1

        # Number will never be greater than mod number, so can reduce it.
        expr.right = None
        expr.operator = None
        return expr

    def reduce_all_mults(self, expr, mod_value):
        # add_debug()()
        if not isinstance(expr, Solver.Expr):
            return expr

        if expr.operator == '*':
            left = eval_expr(expr.left)
            right = eval_expr(expr.right)
            if left == mod_value or right == mod_value:
                expr.left = '0'
                expr.right = None
                expr.operator = None
        elif expr.operator not in {None, '/', '==', '%'}:
            expr.left = self.reduce_all_mults(expr.left, mod_value)
            expr.right = self.reduce_all_mults(expr.right, mod_value)
            return expr.simplify()
        return expr

    def simplify_eql(self, expr):
        vs, vb = get_variables(expr, self.extra_id)
        if not vs and not vb:
            expr.left = str(eval(str(expr)))
            expr.right = None
            expr.operator = None
            return expr

        if expr.right == '0' and expr.left.operator == '==':
            expr.right = expr.left.right
            expr.left = expr.left.left
            expr.operator = '!='
            return expr

        # Check if the var will ever differ in equality.
        if len(vs) > 4 or vb:
            return expr
        values = {v: 1 for v in vs}
        base_comp = int(
            eval(get_expr(expr.left, values)) == eval(get_expr(expr.right, values))
        )
        j = -1
        values[vs[j]] += 1
        while values[vs[0]] != 10:
            res = int(
                eval(get_expr(expr.left, values)) == eval(get_expr(expr.right, values))
            )
            if res != base_comp:
                return expr

            values[vs[j]] += 1
            while j != -len(vs) and values[vs[j]] == 10:
                values[vs[j]] = 1
                j -= 1
                values[vs[j]] += 1
            j = -1

        # Number will never be different, so can reduce it
        expr.left = str(base_comp)
        expr.right = None
        expr.operator = None
        return expr


    def simplify_nql(self, expr):
        vs, vb = get_variables(expr, self.extra_id)
        if not vs and not vb:
            expr.left = str(eval(str(expr)))
            expr.right = None
            expr.operator = None
            return expr

        # if expr.right == '0' and expr.left.operator == '==':
        #     expr.left = expr.left.left
        #     expr.right = expr.left.right
        #     expr.operator = '!='

        # Check if the var will ever differ in equality.
        if len(vs) > 4 or vb:
            return expr
        values = {v: 1 for v in vs}
        base_comp = int(
            eval(get_expr(expr.left, values)) != eval(get_expr(expr.right, values))
        )
        j = -1
        values[vs[j]] += 1
        while values[vs[0]] != 10:
            res = int(
                eval(get_expr(expr.left, values)) != eval(get_expr(expr.right, values))
            )
            if res != base_comp:
                return expr

            values[vs[j]] += 1
            while j != -len(vs) and values[vs[j]] == 10:
                values[vs[j]] = 1
                j -= 1
                values[vs[j]] += 1
            j = -1

        # Number will never be different, so can reduce it
        expr.left = str(base_comp)
        expr.right = None
        expr.operator = None
        return expr

    def add_debug(self):
        if self.debug_state in DEBUG_LINES:
            return pdb.set_trace
        return lambda: None

    class Expr(object):
        def __init__(self, left=None, right=None, operator=None, mapping=None):
            self.left = left
            self.right = right
            self.operator = operator
            self.mapping = mapping

        def __str__(self):
            if not self.operator:
                return str(self.left)
            if self.operator == '==' or self.operator == '/' or self.operator == '!=':
                return f'int({self.left} {self.operator} {self.right})'
            return f'({self.left} {self.operator} {self.right})'

        def __repr__(self):
            return str(self)

        def simplify(self):
            if isinstance(self.left, Solver.Expr) and self.left.is_value():
                self.left = self.left.left
            if isinstance(self.right, Solver.Expr) and self.right.is_value():
                self.right = self.right.left

            v = eval_expr(self)
            if v:
                self.left = str(v)
                self.right = None
                self.operator = None
                return self

            if self.operator:
                return self.mapping[self.operator](self)

            return self

        def is_value(self):
            return not self.operator

        def deepcopy(self):
            e = Solver.Expr(
                operator=self.operator, mapping=self.mapping
            )
            if isinstance(self.left, Solver.Expr):
                e.left = self.left.deepcopy()
            else:
                e.left = self.left
            if isinstance(self.right, Solver.Expr):
                e.right = self.right.deepcopy()
            else:
                e.right = self.right
            return e

    def BExpr(object):
        def __init__(self, value, expr):
            self.value = value
            self.expr = expr


def get_variables(expr, extra_id):
    vs = []
    vb = []
    b_ids = {f'b{i}' for i in range(14)}
    expr_str = str(expr)
    for d in DIGS:
        if d in expr_str:
            vs.append(d)
    for d in b_ids:
        if d in expr_str:
            vb.append(d)
    return vs, vb


def get_expr(expr, values):
    str_expr = str(expr)
    for k, v in values.items():
        str_expr = str_expr.replace(k, str(v))
    return str_expr


def eval_expr(expr):
    try:
        return eval(str(expr))
    except NameError:
        return None


def part1(data):
    rows = parse_data(data)
    start = 1
    programs = []
    while start < 252:
        programs.append((start, start + 17))
        start += 18

    for i, p in enumerate(programs):
        solver = Solver(rows[p[0]:p[1]], ai=i)
        solver.solve()


def parse_data(data):
    rows = data.split('\n')
    return rows


def part2(data):
    return None

    def simplify_mod1(v1, v2, digs):
        if v1 == '0':
            return '0'

        # Check if the var will actually be greater than the mod number
        vs = get_variables1(v1, v2, digs)
        if len(vs) > 4:
            return f'({v1} % {v2})'

        values = {v: 9 for v in vs}
        j = -1
        while values[vs[0]] != 0:
            a_v1 = eval(get_expr1(v1, values))
            a_v2 = eval(get_expr1(v2, values))
            if a_v1 >= a_v2:
                return f'({v1} % {v2})'

            values[vs[j]] -= 1
            while j != -len(vs) and values[vs[j]] == 0:
                values[vs[j]] = 9
                j -= 1
                values[vs[j]] -= 1
            j = -1
        return v1


    def simplify_equality1(v1, v2, digs):
        vs = get_variables1(v1, v2, digs)
        if not vs:
            return str(int(eval(v1) == eval(v2)))
        if len(vs) > 4:
            return f'int({v1} == {v2})'

        values = {v: 1 for v in vs}
        base_comp = int(eval(get_expr1(v1, values)) == eval(get_expr1(v2, values)))
        j = -1
        values[vs[j]] += 1
        while values[vs[0]] != 10:
            res = int(eval(get_expr1(v1, values)) == eval(get_expr1(v2, values)))
            if res != base_comp:
                return f'int({v1} == {v2})'

            values[vs[j]] += 1
            while j != -len(vs) and values[vs[j]] == 10:
                values[vs[j]] = 1
                j -= 1
                values[vs[j]] += 1
            j = -1
        return str(base_comp)


    def get_variables1(v1, v2, digs):
        vs = []
        for d in digs:
            if d in v1 or d in v2:
                vs.append(d)
        return vs


    def get_expr1(expr, values):
        for k, v in values.items():
            expr = expr.replace(k, str(v))
        return expr


    rows = parse_data(data)
    variables = {
        'w': '0',
        'x': '0',
        'y': '0',
        'z': '0'
    }
    curr_dig = 0
    digs = {f'a{i}' for i in range(14)}

    for i in rows[:CURR_STATE]:
        instruction = i.split(' ')
        cmd = instruction[0]
        p = instruction[1]
        v1 = variables[instruction[1]]
        v2 = instruction[2] if len(instruction) == 3 else None
        if v2 in variables:
            v2 = variables[v2]
        if cmd == 'inp':
            variables[p] = f'a{curr_dig}'
            curr_dig += 1
        elif cmd == 'add':
            if v1 == '0':
                variables[p] = v2
            elif v2 != '0':
                variables[p] = f'({v1} + {v2})'
        elif cmd == 'mul':
            if v2 == '0' or v1 == '0':
                variables[p] = '0'
            elif v1 == '1':
                variables[p] = v2
            elif v2 != '1':
                variables[p] = f'({v1} * {v2})'
        elif cmd == 'div':
            if v2 != '1':
                variables[p] = f'int({v1} / {v2})'
        elif cmd == 'mod':
            variables[p] = simplify_mod1(v1, v2, digs)
        elif cmd == 'eql':
            variables[p] = simplify_equality1(v1, v2, digs)
        try:
            variables[p] = str(eval(variables[p]))
        except NameError:
            pass
    for k, v in variables.items():
        print(k)
        print(v)


def determine_expr(expr):
    valid_b = []
    for b in range(0, 100):
        for a in range(1, 10):
            ne = eval(expr.replace('b12', str(b)).replace('a12', str(a)))
            if 7 <= ne < 15:
                valid_b.append(b)
                break
    return valid_b


def find_a(expr, b):
    for a in range(1, 10):
        ne = eval(expr.replace('b12', str(b)).replace('a12', str(a)))
        if 7 <= ne < 15:
            return a
    return None


# 13
# 7 <= b12 < 15

# 12
# 0 <= b11 <= 25 or
# 182 <= b11 < 390

# 11
# 14 <= b10 <= 22 or
#
