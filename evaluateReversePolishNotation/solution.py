import collections


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        q = collections.deque()
        operators = set(["+", "-", "*", "/"])

        for i in range(len(tokens)):
            if tokens[i] in operators:
                second_operand = q.pop()
                fist_operand = q.pop()

                if tokens[i] == "+":
                    q.append(fist_operand + second_operand)
                elif tokens[i] == "-":
                    q.append(fist_operand - second_operand)
                elif tokens[i] == "*":
                    q.append(fist_operand * second_operand)
                elif tokens[i] == "/":
                    q.append(int(fist_operand / second_operand))
                else:
                    raise ValueError("invalid operator")
            else:
                q.append(int(tokens[i]))

        return q.pop()
