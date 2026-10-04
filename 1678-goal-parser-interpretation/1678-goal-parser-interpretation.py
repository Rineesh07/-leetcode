class Solution:
    def interpret(self, command: str) -> str:
        command = list(command)
        ans = []
        for i in range(len(command)):
            if command[i] == '(' and command[i+1] == ')':
                ans.append('o')
            else:
                ans.append(command[i])
        # print(ans)
        final = []
        for x in ans:
            if x != '(' and x != ')':
                final.append(x)
        return ''.join(final)