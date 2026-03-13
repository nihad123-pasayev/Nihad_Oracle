from db import get_connection
from employee_repostery import EmployeeRepository
from department_statistics import DepartmentStatistics


repo = EmployeeRepository()
stats = DepartmentStatistics()

# Data insert
repo.insert_data(1, "Nihad Əliyev",     1500, 20)
repo.insert_data(2, "Aytən Hüseynova",   400, 30)
repo.insert_data(3, "Tural Məmmədov",    300, 10)
repo.insert_data(4, "Günel Əhmədova",    490, 20)
repo.insert_data(5, "Rəşad Quliyev",    2000, 10)
repo.insert_data(6, "Elvin Abbasov",      1200, 30)
repo.insert_data(7, "Nigar Məmmədova",     850, 20)
repo.insert_data(8, "Kamran Əliyev",      1700, 10)
repo.insert_data(9, "Aysel Həsənova",      450, 30)
repo.insert_data(10, "Orxan Qasımov",     1100, 20)
repo.insert_data(11, "Zaur Kərimov",      2100, 10)
repo.insert_data(12, "Lalə Rəhimova",      380, 30)
repo.insert_data(13, "Murad Əliyev",      1350, 20)
repo.insert_data(14, "Sevinc Hüseynova",  1600, 10)
repo.insert_data(15, "Rauf İsmayılov",     920, 30)

#all employeees
repo.show_all_employees()

# employees who salary <500 with descending order
repo.show_low_salary_descending()

# department_statistics and graph
stats.show_charts()