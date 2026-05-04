class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        count_t = Counter(t)
        required = len(count_t)  # nombre de lettres distinctes à satisfaire

        # 2️⃣ Fenêtre glissante
        window = Counter()
        left = 0
        formed = 0  # nombre de lettres satisfaites
        min_len = float('inf')
        res = (0, 0)  # indices du résultat

        # 3️⃣ Parcours avec right
        for right in range(len(s)):
            char = s[right]
            
            # ajouter le caractère dans la fenêtre
            if char in count_t:
                window[char] += 1
                # vérifier si on a exactement ce qu'il faut pour ce caractère
                if window[char] == count_t[char]:
                    formed += 1

            # 4️⃣ Rétrécir la fenêtre si elle est valide
            while formed == required:
                # mettre à jour le résultat si la fenêtre est plus petite
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = (left, right)

                # enlever le caractère à gauche
                char_left = s[left]
                if char_left in count_t:
                    window[char_left] -= 1
                    if window[char_left] < count_t[char_left]:
                        formed -= 1

                left += 1  # déplacer le left

        # 5️⃣ Retourner la sous-chaîne minimale
        start, end = res
        if min_len == float('inf'):
            return ""
        else:
            return s[start:end+1]