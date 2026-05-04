class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        dq = deque()  # deque va contenir les indices des candidats max
                    # toujours triés : le max de la fenêtre est en dq[0]

        for i in range(len(nums)):
            # 1️⃣ Retirer les indices qui sont hors de la fenêtre
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # 2️⃣ Retirer de la deque tous les éléments plus petits que nums[i]
            # Ils ne pourront jamais être maximum tant que nums[i] est là
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3️⃣ Ajouter l'index courant dans la deque
            dq.append(i)

            # 4️⃣ Ajouter le max de la fenêtre au résultat
            # On commence à remplir res uniquement quand la première fenêtre est complète
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res