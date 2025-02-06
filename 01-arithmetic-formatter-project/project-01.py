import re

def arithmetic_arranger(problems, solve = False):
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    if len(problems) > 5:
            return "Error: Too many problems"
    for problem in problems:
        if(re.search("[^\s0-9,+-]", problem)):
            if(re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        first_number = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_number = problem.split(" ")[2]

        if(len(first_number) >= 5 or len(second_number) >= 5):
             return "Error: Numbers cannot be more than four digits."
        
        result = ""
        if(operator == "+"):
             result = str(int(first_number) + int(second_number))
        elif(operator == "-"):
             result = str(int(first_number) - int(second_number))
        length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(length)
        bottom = operator + str(second_number).rjust(length - 1)
        line = ""
        res = str(result).rjust(length)
        for s in range(length):
             line += "-"
        if problem != problems[-1]:
             first += top + "     "
             second += bottom + "     "
             lines += line + "     "
             sumx += res + "     "
        else:
             first += top
             second += bottom
             lines += line
             sumx += res
       
    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    return string
    

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(arithmetic_arranger(["1 + 2", "1 - 9380"], True))
    #    operands = problem.split()
     #   if len(operands) != 3:
      #      return "Error: Operator must be '+' or '-'." 

 #       try:
  #          operand1, operator, operand2 = operands
   #         int(operand1)
    #        int(operand2)
     #   except ValueError:
      #      return "Error: Numbers must only contain digits."

       # if operator not in ['+', '-']:
        #    return "Error: Operator must be '+' or '-'."

       # if len(operand1) > 4 or len(operand2) > 4:
       #     return "Error: Numbers cannot be more than four digits."

    #return arranged_problems

#print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')