def arithmetic_arranger(cases, answer = False):
    num1s = []
    num2s = []
    dashes = []
    answers = []
    
    for case in cases:
        num1, operator, num2 = case.split()
        
        # Veryfication
        if len(cases) > 5:
            return 'Error: Too many problems.'
        
        elif operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        elif num1.isdigit() == False or num2.isdigit() == False:
            return "Error: Numbers must only contain digits."

        elif len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits." #But code can handle it

        ####
        
        # Building Arranged Problems 
        maxLength = len(max(case.split(), key=len))

        result = str(int(num1) + int(num2)) if operator == '+' else str(int(num1) - int(num2))

        num1s.append(' ' * (maxLength+2-len(num1)) + num1) 
        num2s.append(operator + ' ' * (maxLength+1-len(num2)) + num2)
        dashes.append('-' * (maxLength+2))
        answers.append(' '*(maxLength+2-len(result)) + result)

    # Rendering Output
    spaces = '    '
    arrangedProblems = spaces.join(num1s) + "\n" + spaces.join(num2s) + "\n" + spaces.join(dashes)

    if answer:
        arrangedProblems += "\n" + spaces.join(answers)

    return arrangedProblems