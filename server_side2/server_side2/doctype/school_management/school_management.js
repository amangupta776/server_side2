// Copyright (c) 2024, Aman and contributors
// For license information, please see license.txt

frappe.ui.form.on("School Management", {
    refresh: function(frm) {
        frm.add_custom_button('Add Data', () => {
            const dialogBox = new frappe.ui.Dialog({
                title: "Enter Student Data",
                fields: [
                    {
                        label: "Student Name",
                        fieldname: "student_name",
                        fieldtype: "Data"      
                    },
                    {
                        label: "Student Roll Number",
                        fieldname: "student_roll_number",
                        fieldtype: "Data"   
                    },
                    {
                        label: "Class",
                        fieldname: "class",
                        fieldtype: "Data"   
                    },
                    {
                        label: "Percentage",
                        fieldname: "percentage",
                        fieldtype: "Data"   
                    }
                ],
                primary_action_label: "Add",
                primary_action(val) {
                    frm.add_child("student_data",val);
                    frm.save()
                    frm.refresh_field('student_data');
                    dialogBox.hide();
                }
            });
            dialogBox.show();
        });
    }
});
