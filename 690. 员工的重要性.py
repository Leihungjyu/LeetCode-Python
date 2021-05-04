"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        table = {employee.id: employee for employee in employees}
        return table[id].importance if table[id].subordinates == [] else table[id].importance + sum(self.getImportance(employees, i) for i in table[id].subordinates)
