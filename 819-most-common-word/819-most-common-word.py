import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        words = [word for word in re.sub('[^a-z]', ' ', paragraph.lower()).split() if word not in banned]
        count = Counter(words)
        answer = count.most_common(1)[0][0]
        
        return answer