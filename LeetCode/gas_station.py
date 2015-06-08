
class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        diff = []
        i = 0
        while i < len(gas):
            diff.append(gas[i] - cost[i])
            i += 1

        leftGas, sumCost, start = 0, 0, 0
        i = 0
        while i < len(gas):
            leftGas += diff[i]
            sumCost += diff[i]
            if sumCost < 0:
                start = i + 1
                sumCost = 0
            i += 1

        if leftGas < 0:
                return -1
        return start
