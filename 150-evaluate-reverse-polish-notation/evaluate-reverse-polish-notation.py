
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                a = s.pop()
                b = s.pop()

                if i == "+":
                    s.append(b + a)
                elif i == "-":
                    s.append(b - a)
                elif i == "*":
                    s.append(b * a)
                elif i == "/":
                    s.append(int(b / a))
            else:
                s.append(int(i))

        return s[-1]
