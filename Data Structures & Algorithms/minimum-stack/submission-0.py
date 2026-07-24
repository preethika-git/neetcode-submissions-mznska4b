class MinStack:

    def __init__(self):
        self.stk = []
        self.m_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.m_stk:
            self.m_stk.append(val)
        else:
            cur = min(val, self.m_stk[-1])
            self.m_stk.append(cur)

    def pop(self) -> None:
        self.stk.pop()
        self.m_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.m_stk[-1]
        
