# Employee Class
class Employee:
    
    def __init__(self, StaffID, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):
        self.StaffID = int(StaffID)
        self.LastName = str(LastName)
        self.FirstName = str(FirstName)
        self.RegHours = int(RegHours)
        self.HourlyRate = int(HourlyRate)
        self.OTMultiple = float(OTMultiple) 
        self.TaxCredit = int(TaxCredit)
        self.StandardBand = int(StandardBand)
    
    def computePayment(self, HoursWorked, Date):
        payment = dict()
        payment['Name']= self.FirstName + " " + self.LastName
        payment['Date'] = Date
        payment['Regular Hours Worked'] = min(HoursWorked, self.RegHours)
        payment['Overtime Hours Worked'] = max(0, HoursWorked - self.RegHours)
        payment['Regular Rate'] = self.HourlyRate
        payment['Overtime Rate'] = self.HourlyRate * self.OTMultiple
        payment['Regular Pay'] = self.HourlyRate * payment['Regular Hours Worked']
        payment['Overtime Pay'] = max(payment['Overtime Rate'] * payment ['Overtime Hours Worked'], 0)
        payment['Gross Pay'] = payment['Regular Pay'] + payment['Overtime Pay']
        payment['Standard Rate Pay'] = self.StandardBand
        payment['Higher Rate Pay'] = max(payment['Gross Pay'] - self.StandardBand, 0)
        payment['Standard Tax'] = round(payment['Standard Rate Pay'] * 0.2 ,2)
        payment['Higher Tax'] = round(payment['Higher Rate Pay'] * 0.4, 2)
        payment['Total Tax'] = payment['Standard Tax'] + payment['Higher Tax']
        payment['Tax Credit'] = self.TaxCredit
        payment['Net Deductions'] = payment['Higher Tax'] + payment['Tax Credit']
        payment['Net Pay'] = max(0, payment['Gross Pay'] - payment['Net Deductions'])
        return payment


# To open Employees.txt file
with open('/Users/keanemoya/Desktop/Programming_CA/Employee.txt') as employeeFile:
    employees = []
    for line in employeeFile:
        details = tuple(line.split(' '))
        employees.append(Employee( * details))

# To open Hours.txt file
with open('/Users/keanemoya/Desktop/Programming_CA/Hours.txt') as hours:
    for line in hours:
        line = line.split(" ")
        StaffID = eval(line[0])
        for employee in employees:
            if employee.StaffID == StaffID:
                print(employee.computePayment(eval(line[2]), line[1]))
                break


# Reference for unittest: https://docs.python.org/3/library/unittest.html

import unittest

#TEST1 - Net pay cannot exceed gross pay 
class TestMethods(unittest.TestCase):
#TEST1 - Net Pay cannot exceed Gross Pay
    def testNetLessEqualGross(self):
        e=Employee(12345, "Green", "Joe", 37, 16, 1.5, 70, 700)
        pi=employee.computePayment(1,'31/10/2021')
        self.assertLessEqual(pi['Net Pay'],pi['Gross Pay'])

#TEST2 - Overtime pay or overtime hours cannot be negative
    def testOvertimePayorOvertimeHours(self):
        e=Employee(12345, "Green", "Joe", 37, 16, 1.5, 70, 700)
        pi=employee.computePayment(1,'31/10/2021')
        self.assertGreaterEqual(pi['Overtime Pay'], 0) or self.assertGreaterEqual(pi['Overtime Hours Worked'],0)

#TEST3 - Regular Hours Worked cannot exceed hours worked
    def testRegHoursWorkedCannotExceedOTHrs (self):
        e=Employee(12345, "Green", "Joe", 37, 16, 1.5, 70, 700)
        pi=employee.computePayment(1,'31/10/2021')
        self.assertLessEqual(pi['Regular Hours Worked'],pi['Regular Hours Worked'])

#TEST4 - Higher Tax cannot be negative
    def testHigherTaxCannotBeNegative(self):
        e=Employee(12345, "Green", "Joe", 37, 16, 1.5, 70, 700)
        pi=employee.computePayment(1,'31/10/2021')
        self.assertGreaterEqual(pi['Higher Tax'],0)

#TEST5 - Net Pay cannot be negative
    def testNetPayCannotBeNegative(self):
        e=Employee(12345, "Green", "Joe", 37, 16, 1.5, 70, 700)
        pi=employee.computePayment(1,'31/10/2021')
        self.assertGreaterEqual(pi['Net Pay'],0)

if __name__ == '__main__':
    unittest.main()


