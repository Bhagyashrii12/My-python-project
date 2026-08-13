from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return []

        words.discard(beginWord)

        queue = deque([[beginWord]])
        result = []
        found = False

        while queue and not found:
            used = set()

            for _ in range(len(queue)):
                path = queue.popleft()
                word = path[-1]

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i + 1:]

                        if newWord in words:
                            newPath = path + [newWord]

                            if newWord == endWord:
                                result.append(newPath)
                                found = True
                            else:
                                queue.append(newPath)

                            used.add(newWord)

            words -= used

        return result
