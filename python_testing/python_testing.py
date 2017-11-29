
def parse(eq = str, returnString = False):
    eq = processParenthesis(eq)
    if returnString:
        return 'placeholder'
    return eq

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




equation = '20 / (5 - 4) / (2 * (12 + 5))'
print(parse(equation))
