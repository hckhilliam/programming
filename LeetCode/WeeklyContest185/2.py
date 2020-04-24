from typing import List
from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        items = set()
        table = defaultdict(dict)

        for o in orders:
            items.add(o[2])
            table[int(o[1])][o[2]] = table[int(o[1])].get(o[2], 0) + 1

        litems = sorted(items)
        out = [['Table'] + litems]
        for key in sorted(table.keys()):
            out.append([str(key)] + [str(table[key].get(v, 0)) for v in litems])
        return out


print(Solution().displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
print(Solution().displayTable([["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]))
print(Solution().displayTable([["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]))
