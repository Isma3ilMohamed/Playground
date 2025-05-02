class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        q = deque()
        n = len(dom)
        for i, d in enumerate(dom):
            if d != ".":
                q.append((i, d))
        while q:
            i, d = q.popleft()
            if d == "L":
                if i > 0 and dom[i-1] == ".":
                    q.append((i-1, "L"))
                    dom[i-1] = "L"

            else: # d== "R"
                if i+1 < n and dom[i+1] == ".":
                    if i+2 < n and dom[i+2] == "L":
                        q.popleft() #cancel out
                    else:
                        q.append((i+1, "R"))
                        dom[i+1] = "R"
        return "".join(dom)

