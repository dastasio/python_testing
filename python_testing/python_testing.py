
def parse(eq = str, returnString = False):
    eq = processParenthesis(eq)

    result = processOperations(eq)
    if returnString:
        return str(result)
    else:
        return result

def extractParenthesis(eq):
    startPos = -1
    endPos = -1
    openCount = 0
    parInfo = []
    for i in range(len(eq)):
        if eq[i] == '(':
            if openCount == 0:
                startPos = i
            openCount += 1
        if eq[i] == ')':
            openCount -= 1
            if openCount < 0:
                return 'ERROR'
            elif openCount == 0:
                endPos = i
                parInfo.append([startPos, endPos])
    return parInfo

def processParenthesis(eq):
    positions = extractParenthesis(eq)
    if len(positions) == 0:
        return eq
    elif positions == 'ERROR':
        raise SystemExit

    originalEquation = eq
    for elem in positions:
        eq = eq.replace(originalEquation[elem[0] : (elem[1] + 1)], 
                   parse(originalEquation[(elem[0] + 1) : elem[1]], True), 
                   1)
    return eq

def processOperations(eq):
    eq = eq.split('+')
    if len(eq) > 1:
        return solveAdditions(eq)
    else:
        eq = eq[0].split('-')
        if len(eq) > 1:
            return solveSubtraction(eq)
        else:
            eq = eq[0].split('*')
            if len(eq) > 1:
                return solveMultiplication(eq)
            else:
                eq = eq[0].split('/')
                if len(eq) > 1:
                    return solveDivision(eq)
                else:
                    return float(str(eq[0]))


def solveAdditions(eq):
    for i in range(len(eq)):
        eq[i] = processOperations(str(eq[i]))
    return sum(eq)

def solveSubtraction(eq):
    for i in range(len(eq)):
        eq[i] = processOperations(str(eq[i]))
    return eq[0] - sum(eq[1:])

def solveMultiplication(eq):
    prod = 1
    for i in range(len(eq)):
        eq[i] = processOperations(str(eq[i]))
        prod *= float(eq[i])
    return prod

def solveDivision(eq):
    quoz = processOperations(str(eq[0]))
    for i in range(1, len(eq)):
        eq[i] = processOperations(str(eq[i]))
        quoz /= float(eq[i])
    return quoz


equation = '20 / (5 - 4) / (2 * (12 + 5))'
print(parse(equation))
