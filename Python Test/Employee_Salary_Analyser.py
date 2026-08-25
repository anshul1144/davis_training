"""Analyze employee salaries using department and performance allowances."""


DEPARTMENT_ALLOWANCES = {
	"IT": 0.20,
	"HR": 0.15,
	"Sales": 0.10,
	"Finance": 0.18,
}

PERFORMANCE_ALLOWANCES = {
	"Excellent": 0.20,
	"Good": 0.10,
	"Average": 0.05,
	"Poor": 0.00,
}


def read_number(message):
	while True:
		try:
			number = float(input(message))
			if number >= 0:
				return number
			print("Enter a number greater than or equal to 0.")
		except ValueError:
			print("Enter a valid number.")


def read_choice(message, choices):
	while True:
		choice = input(message).strip().lower()
		for valid_choice in choices:
			if choice == valid_choice.lower():
				return valid_choice
		print("Choose one of:", ", ".join(choices))


def calculate_salary(employee):
	basic = employee["basic_salary"]
	department_amount = basic * DEPARTMENT_ALLOWANCES[employee["department"]]
	performance_amount = basic * PERFORMANCE_ALLOWANCES[employee["rating"]]
	final_salary = basic + department_amount + performance_amount
	return final_salary


def add_employee(employees):
	employee_id = input("Employee ID: ").strip()
	name = input("Employee name: ").strip()
	department = read_choice("Department (IT/HR/Sales/Finance): ", DEPARTMENT_ALLOWANCES)
	basic_salary = read_number("Basic salary: ")
	rating = read_choice("Performance (Excellent/Good/Average/Poor): ", PERFORMANCE_ALLOWANCES)

	employees[employee_id] = {
		"name": name,
		"department": department,
		"basic_salary": basic_salary,
		"rating": rating,
	}
	print("Employee saved.")


def display_employees(employees):
	if not employees:
		print("No employees available.")
		return

	for employee_id, employee in employees.items():
		salary = calculate_salary(employee)
		print(
			f"{employee_id} - {employee['name']} | "
			f"{employee['department']} | Final salary: {salary:.2f}"
		)


def display_analysis(employees):
	if not employees:
		print("No employees available.")
		return

	highest_id = max(employees, key=lambda key: calculate_salary(employees[key]))
	highest_employee = employees[highest_id]
	highest_salary = calculate_salary(highest_employee)
	print(f"Highest salary: {highest_employee['name']} ({highest_salary:.2f})")

	department_salaries = {}
	for employee in employees.values():
		department = employee["department"]
		department_salaries.setdefault(department, []).append(calculate_salary(employee))

	for department, salaries in department_salaries.items():
		print(f"Average salary in {department}: {sum(salaries) / len(salaries):.2f}")


def salary_analyzer():
	employees = {}

	while True:
		print("\n1. Add employee  2. View employees  3. Show analysis  4. Exit")
		choice = input("Choose an option: ").strip()

		if choice == "1":
			add_employee(employees)
		elif choice == "2":
			display_employees(employees)
		elif choice == "3":
			display_analysis(employees)
		elif choice == "4":
			print("Exiting the analyzer.")
			break
		else:
			print("Invalid choice.")


salary_analyzer()
