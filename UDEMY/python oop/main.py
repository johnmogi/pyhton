from employees import Manager,Mechanic,Attendant, Cook
from reporting import AccountingReport,StaffingReport, ScheduleReport
from shift import MorningShift, EveningShift, NightShift

employees = [
Manager("Vera","Johnes", 2000, MorningShift()),
Cook("John","Mogi", 4000, MorningShift()),
Attendant("Mouse", "Cotoure", 1500, EveningShift()),
Mechanic("Neo","Angel", 1000, NightShift()),
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees)
]
for r in reports:
    r.print_report()
    print()

# accounting_report = AccountingReport(employees)
# accounting_report.print_accounting_report()
#
# staff_report = StaffingReport(employees)
# staff_report.print_staff_report()

# e = Employee("Vera", 2000)

# print(f'Employee name: {e.name}, Salary: {e.salary}')
