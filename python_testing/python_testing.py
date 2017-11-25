
def parse(eq = str):
    eq = eq.split('+')
    if len(eq) > 1:
        for i in range(len(eq)):
            eq[i] = parse(str(eq[i]))
        return sum(eq)
    else:
        eq = eq[0].split('-')
        if len(eq) > 1:
            for i in range(len(eq)):
                eq[i] = parse(str(eq[i]))
            return eq[0] - sum(eq[1:])
        else:
            eq = eq[0].split('*')
            if len(eq) > 1:
                prod = 1
                for i in range(len(eq)):
                    eq[i] = parse(str(eq[i]))
                    prod *= float(eq[i])
                return prod
            else:
                eq = eq[0].split('/')
                if len(eq) > 1:
                    quoz = parse(str(eq[0]))
                    for i in range(1, len(eq)):
                        eq[i] = parse(str(eq[i]))
                        quoz /= float(eq[i])
                    return quoz
                else:
                    return float(str(eq[0]))



equation = '20 / 5 - 4 / 2 * 12'
print(parse(equation))
