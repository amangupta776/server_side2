import frappe
def execute(filters=None):
    return get_columns(filters), get_data(filters)
def get_columns(filters):
    columns = [
        {
            'fieldname': 'sales_order_name',
            'label': ('Name'),
            'fieldtype': 'Link',
            'options': 'Sales Order'
        },
        {
            'fieldname': 'customer_name',
            'label': ('Customer Name'),
            'fieldtype': 'Link',
            'options': 'Customer'
        },
        {
            'fieldname': 'delivery_date',
            'label': ('Delivery Date'),
            'fieldtype': 'date'
        },{
            'fieldname': 'item_code',
            'label': ('Item Code'),
            'fieldtype': 'Link',
            'options': 'item'
        },{
            'fieldname': 'item_name',
            'label': ('Item Name'),
            'fieldtype': 'data'
        },{
            'fieldname': 'qty',
            'label': ('Quantity'),
            'fieldtype': 'Float'
        },{
            'fieldname': 'sales_invoice_name',
            'label': ('Sales Invoice'),
            'fieldtype': 'Link',
            'options':"Sales Invoice"
        }
    ]
    return columns
def get_data(filters):
    dp = frappe.db.sql("""
        SELECT p.name,customer_name,pa.delivery_date,item_code,item_name,qty FROM `tabSales Order` p JOIN `tabSales Order Item` pa ON pa.parent = p.name
    """, as_dict=True)
    da = frappe.db.sql("""
       SELECT
    p.name AS sales_order_name,
    p.customer_name,
    pa.delivery_date,
    pa.item_code,
    pa.item_name,
    pa.qty,
    si.name AS sales_invoice_name
FROM
    `tabSales Order` p
JOIN
    `tabSales Order Item` pa ON pa.parent = p.name
LEFT JOIN
    `tabSales Invoice` si ON si.customer_name = p.customer_name;
    """, as_dict=True)
    if filters.delivery_date:
        da = frappe.db.sql("""
        SELECT p.name,customer_name,pa.delivery_date,item_code,item_name,qty FROM `tabSales Order` p JOIN `tabSales Order Item` pa ON pa.parent = p.name
                     WHERE pa.delivery_date < %s
    """,(filters.delivery_date), as_dict=True)
    print(dp)
    data = [
        {
            'account': 'Application of Funds (Assets)',
            'currency': 'INR',
            'balance': '15182212.738'
        },
        {
            'account': 'Current Assets - GTPL',
            'currency': 'INR',
            'balance': '17117932.738'
        }
    ]
    return da