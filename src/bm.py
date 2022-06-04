from collections import defaultdict
from typing import DefaultDict


def make_km_table(pattern: str) -> DefaultDict[str, int]:
    """
    Returns a defaultdict for bad rules.
    The key is an alphabet in the pattern and the value is the size to slide.
    The default value is len(pattern)
    """
    m = len(pattern)
    table = defaultdict(lambda: m)
    for i, c in enumerate(pattern):
        table[c] = m - i - 1
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def search(self) -> int:
        """
        Search the first pattern occurrence in text.
        Use Bad Character Heuristic to decide slide size.
        Returns: the index of the first character of matched substring of self.text.
            e.g., When self.text is ANPANMAN and self.pattern is ANM, it returns 3 (ANP[ANM]AN).
        """
        n = len(self.text)
        m = len(self.pattern)
        k = m - 1  # k is the index of the character of the current substring of text being compared with pattern
        while k < n:
            j = m - 1  # l is the index of the character of the pattern that is being compared.
            while 0 <= j:
                if self.text[k] == self.pattern[j]:
                    k -= 1
                    j -= 1
                else:
                    break
            else:
                # match
                return k + 1
            # Align self.text[k] with self.pattern[m].
            # It goes forward by one when it goes backward by k += self.table[self.text[k]].
            k += max(self.table[self.text[k]], m - j)

        return -1
