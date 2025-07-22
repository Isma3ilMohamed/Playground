class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        mapping = {}
        final = {}

        def abbreviate(x, keep=0):
            return (x[:keep+1] + str(len(x)-2-keep) + x[-1], keep)

        for x in words:
            abbreviation = abbreviate(x)
            mapping[abbreviation[0]] = mapping.get(abbreviation[0], []) + [(x,abbreviation[1])]
            final[x] = abbreviation[0]
        
        bad = []
        while True:
            delete = []
            for k,v in mapping.items():
                if len(v) > 1:
                    bad.extend([(k, x) for x in v])
                    delete.append(k)

            for x in delete:
                del mapping[x]

            if not bad:
                break
            else:
                while bad:
                    x = bad.pop()
                    abbreviation = abbreviate(x[1][0], x[1][1]+1)
                    final[x[1][0]] = abbreviation[0]
                    mapping[abbreviation[0]] = mapping.get(abbreviation[0], []) + [(x[1][0], abbreviation[1])]

        return [k if len(k)<=len(v) else v for k,v in final.items()]
