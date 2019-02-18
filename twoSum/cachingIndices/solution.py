class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        places = {}
        for i, n in enumerate(nums):
            try:
                if places[n] is None:
                    places[n] = i
                else:
                    old = places[n]
                    places[n] = []
                    places[n].append(old)
                    places[n].append(i)
            except KeyError:
                places[n] = i

            try:
                if places[target-n] is not None:
                    if type(places[target-n]) is type(int()):
                        if places[target-n] != places[n]:
                            return (places[target-n], places[n])
                        else:
                            continue
                    elif type(places[target-n]) is type(list()):
                        return (places[target-n][0], places[target-n][1])
                    else:
                        return 'extra'
                else:
                    places[target-n] = None

            except KeyError:
                places[target-n] = None
