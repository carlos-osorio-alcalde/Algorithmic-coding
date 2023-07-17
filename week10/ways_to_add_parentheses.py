class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }

        for i in range(len(expression)):
            if expression[i] in operations:
                left_computations = self.diffWaysToCompute(expression[:i])
                right_computations = self.diffWaysToCompute(expression[i + 1:])

                for left in left_computations:
                    for right in right_computations:
                        results.append(operations[expression[i]](left, right))

        return [int(expression)] if expression.isdigit() else results