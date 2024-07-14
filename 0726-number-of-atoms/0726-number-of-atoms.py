from collections import defaultdict

class Solution(object):
    def countOfAtoms(self, formula):
        def parse_formula(formula):
            stack = [defaultdict(int)]
            i, n = 0, len(formula)

            while i < n:
                if formula[i] == '(':
                    stack.append(defaultdict(int))
                    i += 1
                elif formula[i] == ')':
                    top = stack.pop()
                    i += 1
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiplier = int(formula[i_start:i] or 1)
                    for name, count in top.items():
                        stack[-1][name] += count * multiplier
                else:
                    i_start = i
                    i += 1
                    while i < n and formula[i].islower():
                        i += 1
                    name = formula[i_start:i]
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    count = int(formula[i_start:i] or 1)
                    stack[-1][name] += count

            return stack[0]

        def format_result(counts):
            result = []
            for name in sorted(counts.keys()):
                result.append(name)
                if counts[name] > 1:
                    result.append(str(counts[name]))
            return ''.join(result)

        counts = parse_formula(formula)
        return format_result(counts)