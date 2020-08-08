class Solution(object):
    def reconstructQueue(self, people):
        heightList, heightDict = [], {}
        for person in people:
            if person[0] not in heightDict:
                heightList.append(person[0])
                heightDict[person[0]] = [person]
            else:
                heightDict[person[0]].append(person)

        sorted_height = sorted(heightList, reverse=True)
        ret = []
        for h in sorted_height:
            sameHeight = heightDict[h]
            sorted_sameHeight = sorted(sameHeight, key=lambda x: x[1])
            for i in range(0, len(sorted_sameHeight)):
                ret.insert(sorted_sameHeight[i][1], sorted_sameHeight[i])
        return ret
