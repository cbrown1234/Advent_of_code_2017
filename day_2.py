

with open('day_2_ss.txt') as ss:
    ss_str = ss.read()

def parse_ss(str_ss, to_int=True):
    rows = str_ss.splitlines()
    rows_cols = []
    for i, row in enumerate(rows):
        row_col = row.split('\t')
        if to_int:
            row_col = [int(col) for col in row_col]
        rows_cols.append(row_col)
    return rows_cols

parsed_ss = parse_ss(ss_str)

def ck_sum(parsed_ss):
    ck_sum = 0
    for row in parsed_ss:
        ck_sum += (max(row)-min(row))
    return ck_sum

print(ck_sum(parsed_ss))

def if_div_answer(n,m):
    "If n is divisible by m, return n/m else 0"
    if n % m == 0:
        return n//m
    return 0

def div_sum(parsed_ss):
    div_sum = 0
    for row in parsed_ss:
        for i, n in enumerate(row):
            for j, m in enumerate(row):
                if i!=j:
                    div_sum += if_div_answer(n,m)
    return div_sum

print(div_sum(parsed_ss))

