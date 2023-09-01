from stack_array import Stack
#NOTE: ASK IF I CAN USE reverse() FOR LAST PART

# You should not change this Exception class!
class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str: str) -> float:
    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation.
    Raises an PostfixFormatException if the input is not well-formed"""
    if input_str.strip() == "":
        raise PostfixFormatException("Insufficient operands")
    
    stack = Stack(30)
    input_list = input_str.split()

    for element in input_list:
        try:
            stack.push(int(element))
        except:

            try:
                stack.push(float(element))
            except:

                if element == "+":
                    try:
                        num1 = stack.pop()
                        num2 = stack.pop()
                    except:
                        raise PostfixFormatException("Insufficient operands")

                    stack.push(num2 + num1)

                elif element == "-":
                    try:
                        num1 = stack.pop()
                        num2 = stack.pop()
                    except:
                        raise PostfixFormatException("Insufficient operands")

                    stack.push(num2 - num1)

                elif element == "*":
                    try:
                        num1 = stack.pop()
                        num2 = stack.pop()
                    except:
                        raise PostfixFormatException("Insufficient operands")

                    stack.push(num2 * num1)

                elif element == "/":
                    try:
                        num1 = stack.pop()
                        num2 = stack.pop()
                    except:
                        raise PostfixFormatException("Insufficient operands")

                    if num1 == 0:
                        raise ValueError()

                    stack.push(num2 / num1)

                elif element == "**":
                    try:
                        num1 = stack.pop()
                        num2 = stack.pop()
                    except:
                        raise PostfixFormatException("Insufficient operands")

                    stack.push(num2 ** num1)

                elif element == "<<":
                    try:
                        num1 = stack.pop()
                        num2 = stack.pop()
                    except:
                        raise PostfixFormatException("Insufficient operands")

                    if type(num1) == float or type(num2) == float:
                        raise PostfixFormatException("Illegal bit shift operand")

                    stack.push(num2 << num1)

                elif element == ">>":
                    try:
                        num1 = stack.pop()
                        num2 = stack.pop()
                    except:
                        raise PostfixFormatException("Insufficient operands")

                    if type(num1) == float or type(num2) == float:
                        raise PostfixFormatException("Illegal bit shift operand")

                    stack.push(num2 >> num1)

                else:
                    raise PostfixFormatException("Invalid token")

    if stack.num_items != 1:
        raise PostfixFormatException("Too many operands")

    return stack.peek()

def infix_to_postfix(input_str: str) -> str:
    """Converts an infix expression to an equivalent postfix expression"""
    """Input argument:  a string containing an infix expression where tokens are
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """
    infix_list = input_str.split()
    postfix = []
    stack = Stack(30)

    for element in infix_list:
        if element == "(":
            stack.push(element)
        
        elif element == ")":
            while stack.peek() != "(":
                postfix.append(stack.pop())
            stack.pop()

        elif element in ["-", "+", "/", "*", "**", "<<", ">>"]:
            try:
                while check_precedence(element, stack.peek()):
                    postfix.append(stack.pop())

                stack.push(element)
            except:
                stack.push(element)

        else:
            postfix.append(element)

    while not(stack.is_empty()):
        postfix.append(stack.pop())

    return " ".join(postfix)

def check_precedence(o1: str, o2: str) -> bool:
    """Checks whether ecountered operator has higher precedence than operator at
        the top of stack, taking into accountassociativity"""
    """Input arguments: two strings containing operators.
        Returns True if o2 should be appended to postfix expression and False otherwise"""
    prec_dict = {"-" : (0, "l"),
                 "+" : (0, "l"),
                 "/" : (1, "l"),
                 "*" : (1, "l"),
                 "**" : (2, "r"),
                 "<<" : (3, "l"),
                 ">>" : (3, "l")
                }

    o1_prec = prec_dict[o1][0]
    o1_asso = prec_dict[o1][1]
    o2_prec = prec_dict[o2][0]

    return ((o1_prec <= o2_prec) and (o1_asso == "l")) or ((o1_prec < o2_prec) and (o1_asso == "r"))

def prefix_to_postfix(input_str: str) -> str:
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    prefix_list = input_str.split()
    prefix_list.reverse()           #NOTE: ASK ABOUT MEEEEEEEE
    stack = Stack(30)

    for element in prefix_list:
        if element in ["-", "+", "/", "*", "**", "<<", ">>"]:
            o1 = stack.pop()
            o2 = stack.pop()
            stack.push(o1 + " " + o2 + " " + element)

        else:
            stack.push(element)

    return stack.pop()
