from .views import *
from django.urls import path

urlpatterns = [
    path("", index, name="index"),

    # home page path
    path("ShowHome", showHome, name = "Show_Home"),
    path("AdminForm", adminForm, name = "Admin_Form"),
    path("ShowAdmin", showAdmin, name = "Show_Admin"),
    path("ShowContactDetails", showContactDetails, name = "Show_Contact_Details"),

    path("Department", department, name = "Department_Form"),
    path("UpdateDepartment/<int:id>",  updateDepartment,  name = "Update_Department"),
    path("DeleteDepartment/<int:id>",  deleteDepartment,  name = "Delete_Department"),
    path("ShowDepartment",  showDepartment,  name = "Show_Department_Details"),

    path("Doctor",  doctor, name = "Doctor_Form"),
    path("UpdateDoctor/<int:id>",  updateDoctor,  name = "Update_Doctor"),
    path("DeleteDoctor/<int:id>",  deleteDoctor,  name = "Delete_Doctor"),
    path("ShowDoctor",  showDoctor,  name = "Show_Doctor_Details"),

    path("Patient",  patient, name = "Patient_Form"),
    path("UpdatePatient/<int:id>",  updatePatient,  name = "Update_Patient"),
    path("DeletePatient/<int:id>",  deletePatient,  name = "Delete_Patient"),
    path("ShowPatient",  showPatient, name = "Show_Patient_Details"),

    path("Room", room, name = "Room_Form"),
    path("UpdateRoom/<int:id>", updateRoom, name="Update_Room"),
    path("DeleteRoom/<int:id>", deleteRoom, name="Delete_Room"),
    path("ShowRoom", showRoom, name = "Show_Room_Details"),

    path("Checkout", checkout, name = "Checkout_Form"),
    path("UpdateCheckout/<int:id>", updateCheckout, name="Update_Checkout"),
    path("DeleteCheckout/<int:id>", deleteCheckout, name="Delete_Checkout"),
    path("ShowCheckout", showCheckout, name = "Show_Checkout_Details"),
    path("PaymentProcess", paymentProcess, name = "Payment_Process"),
    path("PaymentDone", payPalDone, name = "Payment_Done"),
    path("PaymentCancelled", payPalCancelled, name = "Payment_Cancelled"),

    path("MedicalStore", medicalStore, name = "Medical_Store_Form"),
    path("UpdateMedicalStore/<int:id>", updateMedicalStore, name="Update_MedicalStore"),
    path("DeleteMedicalStore/<int:id>", deleteMedicalStore, name="Delete_MedicalStore"),
    path("ShowMedicalStore", showMedicalStore, name = "Show_Medical_Store_Details"),
    path('OrderMedicine', orderMedicine,name='Order_Medicine'),
    path('ShowOrderMedicine', showOrderMedicine, name='Show_Order_Medicine'),
    path("OrderPaymentProcess", orderPaymentProcess, name="Order_Payment_Process"),
    path("OrderPaymentDone", orderPaymentDone, name="Order_Payment_Done"),
    path("OrderPaymentCancelled", orderPaymentCancelled, name="Order_Payment_Cancelled"),

    path("Staff", staff, name = "Staff_Form"),
    path("UpdateStaff/<int:id>", updateStaff, name="Update_Staff"),
    path("DeleteStaff/<int:id>", deleteStaff, name="Delete_Staff"),
    path("ShowStaff", showStaff, name = "Show_Staff_Details"),

    path("Visitor", visitor, name = "Visitor_Form"),
    path("UpdateVisitor/<int:id>", updateVisitor, name="Update_Visitor"),
    path("DeleteVisitor/<int:id>", deleteVisitor, name="Delete_Visitor"),
    path("ShowVisitor", showVisitor, name = "Show_Visitor_Details"),
]
