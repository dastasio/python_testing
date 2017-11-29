import math

variables = {'x' : 0,
             'P' : math.pi}

def parse(equation = str, returnString = False, x = variables['x']):
    # removing all whitespaces
    equation = equation.replace(' ', '')
    equation = replaceVariables(equation, x)

    equation = processParenthesis(equation)
    result = processOperations(equation)
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
        trigTest = originalEquation[(elem[0] - 3) : elem[0]]
        if 'sin' in trigTest:
            eq = eq.replace(originalEquation[(elem[0] - 3) : (elem[1] + 1)], 
                   str(math.sin(math.radians(parse(originalEquation[(elem[0] + 1) : elem[1]])))), 
                   1)
        elif 'cos' in trigTest:
            eq = eq.replace(originalEquation[(elem[0] - 3) : (elem[1] + 1)], 
                   str(math.cos(math.radians(parse(originalEquation[(elem[0] + 1) : elem[1]])))), 
                   1)
        elif 'tan' in trigTest:
            eq = eq.replace(originalEquation[(elem[0] - 3) : (elem[1] + 1)], 
                   str(math.tan(math.radians(parse(originalEquation[(elem[0] + 1) : elem[1]])))), 
                   1)
        else:
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

def replaceVariables(eq = str, x = variables['x']):
    for v in variables.keys():
        eq = eq.replace(v, str(variables[v]))
    return eq


equation = '2 * P + 5 + sin(30) * (5 - 3)'
print(parse(equation))
