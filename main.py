class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        total_cost = 0
        current_gas = 0
        start_index = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]
            
            # If current gas is negative, reset the start index
            if current_gas < 0:
                start_index = i + 1  # Move to the next station
                current_gas = 0  # Reset current gas

        # If total gas is greater than or equal to total cost, we can complete the circuit
        return start_index if total_gas >= total_cost else -1

# Example usage
solution = Solution()
print(solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # Output: 3
print(solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]))              # Output: -1
