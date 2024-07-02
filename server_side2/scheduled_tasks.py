import frappe
def my_background_task():
    # This Function is Running in Background and Increasing value of items by +1 
    doc = frappe.get_doc('Total Item')
    doc.items=int(doc.items)+1
    doc.save()
    frappe.db.commit()
    return doc.items
