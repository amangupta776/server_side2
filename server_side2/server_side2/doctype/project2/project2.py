# Copyright (c) 2024, Aman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Project2(Document):
	def before_save(self):
		try:
			recipients = ["amanhyoer@gmail.com"]
			subject = f"New {self.doctype} Created"
			message = f"A new {self.doctype} has been created with the following details:\n\n"
			message += f"Title: {self.title}\n"
			message += f"Description: {self.description}\n"
			
			task_data = "\nTasks:\n"
			for task in self.get('task'):
				task_data += f"- {task.task_name}, {task.hours} hours\n"
			
			message += task_data
			
			frappe.sendmail(
				recipients=recipients,
				subject=subject,
				message=message,
				delayed=False
			)

		except Exception as e:
			frappe.throw("Error Occured While Sending Email",e)
