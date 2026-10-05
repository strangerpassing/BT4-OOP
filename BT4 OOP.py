# Họ và tên: Nguyễn Trung Hiếu
# Mã số sinh viên: 202418898
class Employee:
    def __init__(self, employeeid, fullName, department="Unassigned"):
        if not employeeid or not fullName or not department:
            raise ValueError("Error: No blank ids or names or departments allowed!")
        
        self.employeeid = employeeid
        self.fullName = fullName
        self.department = department
        self.monthlybonus = 0

    def check(self):
        if self.monthlybonus<0:
            raise ValueError("Error: Monthly bonus cannot be negative!")
    def showID(self):
         return self.employeeid
    
    def showfullName(self):
         return self.fullName

    def showdepartment(self):
         return self.department

    def showmonthlybonus(self):
         return self.monthlybonus
    
    def addBonus(self, amount):
        if amount>0:
            self.monthlybonus += amount
            print(f"employee {self.employeeid} got an increase of money bonus to {self.monthlybonus}")

    def addBonuswithreason(self, amount, reason):
        if amount>0 and not not reason:
            self.monthlybonus += amount
            print(f"employee {self.employeeid} got an increase of money bonus to {self.monthlybonus} due to {reason}")

    def addBonuswithreasonVersion2(self, rate, referenceAmount, reason):
        if rate>0 and not rate>0.5 and referenceAmount>0 and not not reason:
            self.monthlybonus += rate*referenceAmount
            print(f"employee {self.employeeid} got an increase of money bonus to {self.monthlybonus} due to {reason}")

    def changemonthlybonus(self, newval):
        if newval<0:
            raise ValueError("Error: monthly bonus cannot be negative!")
        else:
            self.monthlybonus = newval

    def changeDepartment(self, newdep):
        if not newdep:
            raise ValueError("Error: New department cannot be blank!")
        else:
            self.department = newdep

    def calculateGrossPay(self):
        return self.monthlybonus

    def getEmployeeType(self):
        return "Employee"

    def displayPayrollInfo(self):
        print(f"the monthly bonus is {self.monthlybonus}")
        print(f"the department is {self.department}")

class SalariedEmployee(Employee):
    def __init__(self, id, fullName, monthlySalary,  responsibilityAllowance, department = "Unassigned"):
        if not id or not fullName or not department:
            raise ValueError("Error: No blank ids or names or departments allowed!")
        if monthlySalary<0 or responsibilityAllowance<0:
            raise ValueError("Error: monthly salary and resposibility allowance cannot be negative!")
        
        self.employeeid = id
        self.fullName = fullName
        self.department = department
        self.monthlybonus = 0
        self.monthlySalary = monthlySalary
        self.responsibilityAllowance = responsibilityAllowance

    def showmonthlysalary(self):
        return self.monthlySalary

    def showresposibilityallowance(self):
        return self.responsibilityAllowance

    def changemonthlysalary(self, newval):
        if newval<0:
            raise ValueError("Error: monthly salary cannot be negative!")
        else:    
            self.monthlySalary = newval

    def changeresposibilityallowance(self, newval):
        if newval<0:
            raise ValueError("Error: responsibility allowance cannot be negative!")
        else:
            self.responsibilityAllowance = newval
    
    def calculateGrossPay(self):
        return self.monthlySalary * self.responsibilityAllowance + self.monthlybonus

    def getEmployeeType(self):
        return "Salaried Employee"

    def displayPayrollInfo(self):
        print(self.employeeid)
        print(self.fullName)
        print(self.getEmployeeType())
        print(f"department: {self.showdepartment()}")
        print(f"Monthly salary:{self.monthlySalary}")
        print(f"Responsibility allowance:{self.responsibilityAllowance}")
        print(f"Monthly bonus:{self.showmonthlybonus()}")
        print(f"Total gross pay is:{self.calculateGrossPay()}")

class HourlyEmployee(Employee):
    def __init__(self, id, fullName, hourlyRate, workedHours, department = "Unassigned"):
        if not id or not fullName or not department:
            raise ValueError("Error: No blank ids or names or departments allowed!")
        if hourlyRate<0 or workedHours<0 or workedHours>250:
            raise ValueError("Error: hourly salary and worked hours cannot be negative and worked hours cannot be larger than 250!")

        self.employeeid = id
        self.fullName = fullName
        self.department = department
        self.monthlybonus = 0
        self.hourlyRate = hourlyRate
        self.workedHours = workedHours

    def showhourlyrate(self):
        return self.hourlyRate

    def showworkedhours(self):
        return self.workedHours

    def changehourlyrate(self, newval):
        if newval<0:
            raise ValueError("Error: hourly rate cannot be negative!")
        else:
            self.hourlyRate = newval

    def changeworkedhours(self, newval):
        if newval<0 or newval>250:
            raise ValueError("Error: unsuitable value for worked hours")
        else:
            self.workedHours = newval

    def calculateGrossPay(self):
        if self.workedHours<160:
            return self.workedHours*self.hourlyRate + self.monthlybonus
        else:
            return self.hourlyRate*(160 + 1.5*(self.workedHours-160)) + self.monthlybonus
    
    def getEmployeeType(self):
        return "Hourly Employee"

    def displayPayrollInfo(self):
        print(self.employeeid)
        print(self.fullName)
        print(self.getEmployeeType())
        print(f"department: {self.showdepartment()}")
        print(f"hourly rate is: {self.hourlyRate}")
        print(f"worked hours: {self.workedHours}")
        print(f"monthly bonus: {self.showmonthlybonus()}")
        print(f"total gross pay is: {self.calculateGrossPay()}")
        

class SalesEmployee(Employee):
    def __init__(self, id, fullName, baseSalary, salesRevenue, commissionRate, department = "Unassigned"):
        if not id or not fullName or not department:
            raise ValueError("Error: No blank ids or names or departments allowed!")
        if baseSalary<0 or salesRevenue<0 or commissionRate<=0 or commissionRate>=0.3:
            raise ValueError("Error: Unsuitable base salary, sales revenue or commission rate(commission rate must be >0 and <0.3)")

        self.employeeid = id
        self.fullName = fullName
        self.baseSalary = baseSalary
        self.salesRevenue = salesRevenue
        self.commissionRate = commissionRate
        self.department = department
        self.monthlybonus = 0

    def showbasesalary(self):
        print(self.baseSalary)

    def changebasesalary(self, newval):
        if newval<0:
            raise ValueError("Error: new base salary cant be negative!")
        else:
            self.baseSalary = newval

    def showsalesrevenue(self):
        print(self.salesRevenue)

    def changesalesrevenue(self, newrev):
        if newrev<0:
            raise ValueError("Error: revenue cant be negative!")
        else:
            self.salesRevenue = newrev

    def showcommissionrate(self):
        print(self.commissionRate)

    def changecommissionrate(self, newval):
        if newval<=0 or newval>=0.3:
            raise ValueError("Error: commission rate should be in (0,0.3)!")
        else:
            self.commissionRate = newval

    def calculateGrossPay(self):
        return self.baseSalary + self.salesRevenue * self.commissionRate + self.monthlybonus

    def getEmployeeType(self):
        return "Sales Employee"
    
    def displayPayrollInfo(self):
        print(self.employeeid)
        print(self.fullName)
        print(self.getEmployeeType())
        print(f"department: {self.showdepartment()}")
        print(f"the base salary is {self.baseSalary}")
        print(f"the sales revenue is {self.salesRevenue}")
        print(f"the commission rate is {self.commissionRate}")
        print(f"monthly bonus: {self.monthlybonus}")
        print(f"the total gross pay is {self.calculateGrossPay()}")

class Payroll:
    def __init__(self, period):
        self.period = period
        self.employee_list = []

    def addEmployee(self, employee):
        for i in self.employee_list:
            if i.employeeid == employee.employeeid:
                print("Error: The list cannot contain 2 same employees!")
                return None
        self.employee_list.append(employee)

    def findEmployee(self, employeeId):
        for i in self.employee_list:
            if i.employeeid == employeeId:
                print(f"Yes, you found them. Here is information of your employee:")
                print(f"{i.displayPayrollInfo()}")
                return
        print("Sorry, no employee found")

    def calculateTotalPayroll(self):
        total = 0
        for i in self.employee_list:
            total = total + i.calculateGrossPay()
        return total

    def calculateTotalPayrollbydepartment(self, department):
        total = 0
        for i in self.employee_list:
            if i.department == department:
                total = total + i.calculateGrossPay()
            else:
                continue
        return total

    def findHighestPaidEmployee(self):
        if len(self.employee_list) == 0:
            return None
        elif len(self.employee_list) == 1:
            return self.employee_list[0]
        else:
            result = self.employee_list[0]
            for i in range(1,len(self.employee_list),1):
                if self.employee_list[i].calculateGrossPay() > result.calculateGrossPay():
                    result = self.employee_list[i]
        return result

    def displayPayroll(self):
        for i in self.employeelist:
            i.displayPayrollInfo()
            print("\n")

T1 = SalariedEmployee("Sa1", "Josh Mats", 32000, 100, "D1")
P1 = Payroll("2022-01")
P1.addEmployee(T1)
T2 = HourlyEmployee("H1", "Amy Rose", 440, 242, "D1")
T3 = SalesEmployee("F1", "Miles Prower", 25000, 1500000, 0.12)
P1.addEmployee(T2)
P1.addEmployee(T3)
T1.addBonus(6000)
T4 = SalesEmployee("F2", "Ivo Robotnik", 27500, 1750000, 0.125, "Information and Technology")
P1.addEmployee(T4)
print(P1.calculateTotalPayroll())
T5 = SalariedEmployee("F3", "Brian Dunes", 31000, 3250, "")