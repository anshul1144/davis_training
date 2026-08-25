"""Calculate employee payroll from monthly attendance records."""


def read_non_negative_number(message):
	while True:
		try:
			number = float(input(message))
			if number >= 0:
				return number
			print("Enter a value greater than or equal to 0.")
		except ValueError:
			print("Enter a valid number.")


def read_working_days():
	while True:
		try:
			working_days = int(input("Working days in the month: "))
			if working_days > 0:
				return working_days
			print("Working days must be greater than 0.")
		except ValueError:
			print("Enter a valid whole number.")


def read_attendance(working_days):
	while True:
		value = input(
			f"Attendance for {working_days} days (enter present days or P/A record): "
		).strip().upper()
		count = value[:-1] if value.endswith("P") else value
		if count.isdigit():
			present_days = int(count)
			if 0 <= present_days <= working_days:
				return ["P"] * present_days + ["A"] * (working_days - present_days)

		record = value.split()
		if len(record) == working_days and all(day in ("P", "A") for day in record):
			return record
		print(f"Enter a number from 0 to {working_days}, or exactly {working_days} P/A values.")


def calculate_payroll(employee, working_days, overtime_threshold, overtime_rate):
	present_days = employee["attendance"].count("P")
	absent_days = employee["attendance"].count("A")
	attendance_percentage = present_days / working_days * 100
	daily_salary = employee["monthly_salary"] / working_days
	deduction = absent_days * daily_salary
	paid_overtime_hours = max(0, employee["overtime_hours"] - overtime_threshold)
	overtime_pay = paid_overtime_hours * overtime_rate
	net_salary = employee["monthly_salary"] - deduction + overtime_pay

	return {
		"working_days": present_days,
		"absent_days": absent_days,
		"attendance_percentage": attendance_percentage,
		"deduction": deduction,
		"overtime_pay": overtime_pay,
		"net_salary": net_salary,
	}


def add_employee(employees, working_days):
	employee_id = input("Employee ID: ").strip()
	if employee_id in employees:
		print("Employee ID already exists.")
		return

	employees[employee_id] = {
		"name": input("Employee name: ").strip(),
		"monthly_salary": read_non_negative_number("Monthly salary: "),
		"attendance": read_attendance(working_days),
		"overtime_hours": read_non_negative_number("Overtime hours: "),
	}
	print("Employee record saved.")


def display_payroll(employees, working_days, overtime_threshold, overtime_rate):
	if not employees:
		print("No employee records available.")
		return

	low_attendance = []
	for employee_id, employee in employees.items():
		payroll = calculate_payroll(
			employee, working_days, overtime_threshold, overtime_rate
		)
		print(f"\n{employee_id} - {employee['name']}")
		print(f"Working days: {payroll['working_days']}")
		print(f"Absent days: {payroll['absent_days']}")
		print(f"Attendance: {payroll['attendance_percentage']:.2f}%")
		print(f"Overtime pay: {payroll['overtime_pay']:.2f}")
		print(f"Salary deduction: {payroll['deduction']:.2f}")
		print(f"Net salary: {payroll['net_salary']:.2f}")
		if payroll["attendance_percentage"] < 75:
			low_attendance.append(employee["name"])

	print("\nEmployees below 75% attendance:")
	print(", ".join(low_attendance) if low_attendance else "None")


def attendance_payroll():
	employees = {}
	working_days = read_working_days()

	overtime_threshold = read_non_negative_number("Overtime threshold (hours): ")
	overtime_rate = read_non_negative_number("Overtime pay per hour: ")

	while True:
		print("\n1. Add employee  2. Payroll summary  3. Exit")
		choice = input("Choose an option: ").strip()
		if choice == "1":
			add_employee(employees, working_days)
		elif choice == "2":
			display_payroll(employees, working_days, overtime_threshold, overtime_rate)
		elif choice == "3":
			print("Exiting the payroll analyzer.")
			break
		else:
			print("Invalid choice.")


if __name__ == "__main__":
	try:
		attendance_payroll()
	except EOFError:
		print("\nNo input received. Exiting the payroll analyzer.")
