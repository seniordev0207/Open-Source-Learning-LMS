import frappe


def execute():
	assignments = frappe.get_all("Lesson Assignment", fields=["name", "course"])
	for assignment in assignments:
		evaluator = frappe.db.get_value("LMS Course", assignment.course, "evaluator")
		frappe.db.set_value("Lesson Assignment", assignment.name, "evaluator", evaluator)
