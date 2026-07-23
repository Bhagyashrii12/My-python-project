class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0

        while i < len(words):
            line = []
            length = 0

            while i < len(words) and length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1

            spaces = maxWidth - length

            # Last line or one word
            if i == len(words) or len(line) == 1:
                s = " ".join(line)
                s += " " * (maxWidth - len(s))
                res.append(s)
            else:
                gap = spaces // (len(line) - 1)
                extra = spaces % (len(line) - 1)

                s = ""
                for j in range(len(line) - 1):
                    s += line[j]
                    s += " " * (gap + (1 if j < extra else 0))
                s += line[-1]

                res.append(s)

        return res
