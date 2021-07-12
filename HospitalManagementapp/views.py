from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

from .forms import *
from .models import *


# Create your views here.
def index(request):
	return HttpResponse("hello World!!!")


@login_required
def department(request):
	if request.method == "POST":
		dept_form_vdf= DepartmentForm(request.POST)
		if dept_form_vdf.is_valid():
			# dept= Department()
			# dept.name= dept_form_vdf.cleaned_data['name']
			# dept.head= dept_form_vdf.cleaned_data['head']
			# dept.save()
			dept_form_vdf.save()

			dept_vdf= DepartmentForm()
			return render(request, 'AddDepartment.html',{"vdf": dept_vdf,'success':"Department Data is saved"})
		else:
			return render(request, 'AddDepartment.html',{"vdf": dept_form_vdf,'success':"Department Data is not "
			                                                                          "saved"})
	dept_vdf= DepartmentForm()
	return render(request, 'AddDepartment.html', {"vdf": dept_vdf })

def updateDepartment(request,id):
	dept_data= Department.objects.get(pk= id)
	if request.method == "POST":
		dept_form_vdf= DepartmentForm(request.POST)
		if dept_form_vdf.is_valid():
			new_dept= Department()
			new_dept.name= dept_form_vdf.cleaned_data['name']
			new_dept.head= dept_form_vdf.cleaned_data['head']
			new_dept.id= dept_data.id
			new_dept.save()

			return redirect("Show_Department_Details")
		else:
			return render(request, 'AddDepartment.html', {"vdf": dept_form_vdf, 'success': "Department Data is not "
			                                                                               "saved"})
	dept_vdf= DepartmentForm( instance= dept_data)
	return render(request, 'AddDepartment.html', {"vdf": dept_vdf})

def deleteDepartment(request,id):
	dept_data= Department.objects.get(pk= id)
	dept_data.delete()
	return redirect('Show_Department_Details')

def showDepartment(request):
	department_list_all= Department.objects.all()
	page_wise= Paginator(department_list_all, per_page= 5, orphans= 2)
	current_page= request.GET.get('page')
	department_list= page_wise.get_page(current_page)
	return render(request, 'ShowDepartment.html',{'dept_list': department_list})



@login_required
def doctor(request):
	if request.method == "POST":
		doc_form_vdf= DoctorForm(request.POST)
		if doc_form_vdf.is_valid():
			doc= Doctor()
			doc.name= doc_form_vdf.cleaned_data['name']
			doc.d_o_b= doc_form_vdf.cleaned_data['d_o_b']
			doc.gender= doc_form_vdf.cleaned_data['gender']
			doc.phone= doc_form_vdf.cleaned_data['phone']
			doc.email= doc_form_vdf.cleaned_data['email']
			doc.address= doc_form_vdf.cleaned_data['address']
			doc.degree= doc_form_vdf.cleaned_data['degree']
			doc.department= doc_form_vdf.cleaned_data['department']
			doc.save()

			doc_vdf= DoctorForm()
			return render(request, 'AddDoctor.html',{"vdf": doc_vdf,'success':"new doctor Data is saved"})
		else:
			return render(request, 'AddDoctor.html',{"vdf": doc_form_vdf,'success':"Data is not saved"})

	doc_vdf= DoctorForm()
	return render(request, 'AddDoctor.html', {"vdf": doc_vdf })

def updateDoctor(request,id):
	doc_data= Doctor.objects.get(pk= id)
	if request.method == "POST":
		doc_form_vdf= DoctorForm(request.POST)
		if doc_form_vdf.is_valid():
			new_doc= Doctor()
			new_doc.name = doc_form_vdf.cleaned_data['name']
			new_doc.d_o_b = doc_form_vdf.cleaned_data['d_o_b']
			new_doc.gender = doc_form_vdf.cleaned_data['gender']
			new_doc.phone = doc_form_vdf.cleaned_data['phone']
			new_doc.email = doc_form_vdf.cleaned_data['email']
			new_doc.address = doc_form_vdf.cleaned_data['address']
			new_doc.degree = doc_form_vdf.cleaned_data['degree']
			new_doc.department = doc_form_vdf.cleaned_data['department']

			new_doc.id= doc_data.id
			new_doc.save()

			return redirect("Show_Doctor_Details")
		else:
			return render(request, 'AddDoctor.html', {"vdf": doc_form_vdf, 'success': "Doctor Data is not "
			                                                                               "saved"})
	doc_vdf= DoctorForm( instance= doc_data)
	return render(request, 'AddDoctor.html', {"vdf": doc_vdf})

def deleteDoctor(request,id):
	doc_data= Doctor.objects.get(pk= id)
	doc_data.delete()
	return redirect('Show_Doctor_Details')

def showDoctor(request):
	doctor_list_all= Doctor.objects.all()
	page_wise= Paginator(doctor_list_all, per_page= 5, orphans= 2)
	current_page= request.GET.get('page')
	doctor_list= page_wise.get_page(current_page)
	return render(request, 'ShowDoctor.html', {'doctor_list': doctor_list})



@login_required
def patient(request):
	if request.method == "POST":
		patient_form_vdf= PatientForm(request.POST)
		if patient_form_vdf.is_valid():
			p= Patient()
			p.name= patient_form_vdf.cleaned_data['name']
			p.gender= patient_form_vdf.cleaned_data['gender']
			p.d_o_b= patient_form_vdf.cleaned_data['d_o_b']
			p.age= patient_form_vdf.cleaned_data['age']
			p.blood= patient_form_vdf.cleaned_data['blood']
			p.disease= patient_form_vdf.cleaned_data['disease']
			p.address= patient_form_vdf.cleaned_data['address']
			p.phone= patient_form_vdf.cleaned_data['phone']
			p.date= patient_form_vdf.cleaned_data['date']
			p.room_no= patient_form_vdf.cleaned_data['room_no']
			p.doctor= patient_form_vdf.cleaned_data['doctor']
			p.save()

			p_vdf= PatientForm()
			return render(request, 'AddPatient.html',{"vdf": p_vdf,'success':"new patient data is saved"})
		else:
			return render(request, 'AddPatient.html',{"vdf": patient_form_vdf,'success':"Data is not saved"})

	p_vdf= PatientForm()
	return render(request, 'AddPatient.html', {"vdf": p_vdf })

def updatePatient(request,id):
	patient_data= Patient.objects.get(pk= id)
	if request.method == "POST":
		patient_form_vdf= PatientForm(request.POST)
		if patient_form_vdf.is_valid():
			new_patient= Patient()
			new_patient.name= patient_form_vdf.cleaned_data['name']
			new_patient.gender= patient_form_vdf.cleaned_data['gender']
			new_patient.d_o_b= patient_form_vdf.cleaned_data['d_o_b']
			new_patient.age= patient_form_vdf.cleaned_data['age']
			new_patient.blood= patient_form_vdf.cleaned_data['blood']
			new_patient.disease= patient_form_vdf.cleaned_data['disease']
			new_patient.address= patient_form_vdf.cleaned_data['address']
			new_patient.phone= patient_form_vdf.cleaned_data['phone']
			new_patient.date= patient_form_vdf.cleaned_data['date']
			new_patient.room_no= patient_form_vdf.cleaned_data['room_no']
			new_patient.doctor= patient_form_vdf.cleaned_data['doctor']
			new_patient.id= patient_data.id
			new_patient.save()

			return redirect("Show_Patient_Details")
		else:
			return render(request, 'AddPatient.html', {"vdf": patient_form_vdf, 'success': "Patient Data is not "
			                                                                               "saved"})
	patient_vdf= PatientForm( instance= patient_data)
	return render(request, 'AddPatient.html', {"vdf": patient_vdf})

def deletePatient(request,id):
	patient_data= Patient.objects.get(pk= id)
	patient_data.delete()
	return redirect('Show_Patient_Details')

def showPatient(request):
	patient_list_all= Patient.objects.all()
	page_wise= Paginator(patient_list_all, per_page= 5, orphans= 2)
	current_page= request.GET.get('page')
	patient_list= page_wise.get_page(current_page)
	return render(request,'ShowPatient.html',{'patient_list' : patient_list })



@login_required
def room(request):
	if request.method == 'POST':
		room_form_vdf= RoomForm(request.POST)
		if room_form_vdf.is_valid():
			r= Room()
			r.room_no= room_form_vdf.cleaned_data['room_no']
			r.room_type= room_form_vdf.cleaned_data['room_type']
			r.status= room_form_vdf.cleaned_data['status']
			r.price= room_form_vdf.cleaned_data['price']
			r.no_of_bed= room_form_vdf.cleaned_data['no_of_bed']
			r.save()

			r_vdf= RoomForm()
			return render(request, 'AddRoom.html',{'vdf':r_vdf, 'success':'New room data has successfully save...'})
		else:
			return render(request, 'AddRoom.html',{'vdf':room_form_vdf, 'success':'New room data has not save...'})
	r_vdf= RoomForm()
	return render(request, 'AddRoom.html', {'vdf': r_vdf, 'success': ''})

def updateRoom(request,id):
	room_data= Room.objects.get(pk= id)
	if request.method == "POST":
		room_form_vdf= RoomForm(request.POST)
		if room_form_vdf.is_valid():
			new_room= Room()
			new_room.room_no= room_form_vdf.cleaned_data['room_no']
			new_room.room_type= room_form_vdf.cleaned_data['room_type']
			new_room.status= room_form_vdf.cleaned_data['status']
			new_room.price= room_form_vdf.cleaned_data['price']
			new_room.no_of_bed= room_form_vdf.cleaned_data['no_of_bed']

			new_room.id= room_data.id
			new_room.save()

			return redirect("Show_Room_Details")
		else:
			return render(request, 'AddRoom.html', {"vdf": room_form_vdf, 'success': "Room Data is not "
			                                                                               "saved"})
	room_vdf= RoomForm( instance= room_data)
	return render(request, 'AddRoom.html', {"vdf": room_vdf})

def deleteRoom(request,id):
	room_data= Room.objects.get(pk= id)
	room_data.delete()
	return redirect('Show_Room_Details')

def showRoom(request):
	room_list_all= Room.objects.all()
	page_wise= Paginator(room_list_all, per_page= 5, orphans= 2)
	current_page= request.GET.get('page')
	room_list= page_wise.get_page(current_page)
	return render(request,'ShowRoom.html',{ "room_list" : room_list })



@login_required
def checkout(request):
	if request.method == "POST":
		checkout_form_vdf= CheckoutForm(request.POST)
		if checkout_form_vdf.is_valid():
			c= Checkout()

			c.patient= checkout_form_vdf.cleaned_data['patient']
			c.gender= checkout_form_vdf.cleaned_data['gender']
			c.age= checkout_form_vdf.cleaned_data['age']
			c.contact= checkout_form_vdf.cleaned_data['contact']
			c.address= checkout_form_vdf.cleaned_data['address']
			c.disease= checkout_form_vdf.cleaned_data['disease']
			c.d_o_b= checkout_form_vdf.cleaned_data['d_o_b']
			c.date_of_adm= checkout_form_vdf.cleaned_data['date_of_adm']
			c.date_of_dis= checkout_form_vdf.cleaned_data['date_of_dis']
			c.room_no= checkout_form_vdf.cleaned_data['room_no']
			c.total_bill= checkout_form_vdf.cleaned_data['total_bill']
			c.save()

			latest_payment= Checkout.objects.latest('bill_no')

			request.session['payer_id']= latest_payment.bill_no
			request.session['first_name']= str(c.patient)
			request.session['contact_phone']= c.contact
			request.session['amount']= str(c.total_bill)

			return redirect('Payment_Process')
		else:
			return render(request, "AddCheckout.html",{'vdf':checkout_form_vdf, 'success': "your billing data has not saved"})
	check_vdf= CheckoutForm()
	return render(request, "AddCheckout.html", {'vdf':check_vdf, 'success': " "})

def updateCheckout(request,id):
	checkout_data= Checkout.objects.get(pk= id)

	if request.method == "POST":
		checkout_form_vdf= CheckoutForm(request.POST)
		if checkout_form_vdf.is_valid():
			new_checkout= Checkout()
			new_checkout.patient= checkout_form_vdf.cleaned_data['patient']
			new_checkout.gender= checkout_form_vdf.cleaned_data['gender']
			new_checkout.age= checkout_form_vdf.cleaned_data['age']
			new_checkout.contact= checkout_form_vdf.cleaned_data['contact']
			new_checkout.address= checkout_form_vdf.cleaned_data['address']
			new_checkout.disease= checkout_form_vdf.cleaned_data['disease']
			new_checkout.d_o_b= checkout_form_vdf.cleaned_data['d_o_b']
			new_checkout.date_of_adm= checkout_form_vdf.cleaned_data['date_of_adm']
			new_checkout.date_of_dis= checkout_form_vdf.cleaned_data['date_of_dis']
			new_checkout.room_no= checkout_form_vdf.cleaned_data['room_no']
			new_checkout.total_bill= checkout_form_vdf.cleaned_data['total_bill']

			new_checkout.bill_no= checkout_data.bill_no
			new_checkout.payment_status= checkout_data.payment_status
			new_checkout.save()

			if checkout_data.payment_status != 'Confirm' :
				latest_payment = Checkout.objects.latest('bill_no')

				request.session['payer_id'] = latest_payment.bill_no
				request.session['first_name'] = str(new_checkout.patient)
				request.session['contact_phone'] = new_checkout.contact
				request.session['amount'] = str(new_checkout.total_bill)

				return redirect('Payment_Process')

			return redirect("Show_Checkout_Details")
		else:
			return render(request, 'AddCheckout.html', {"vdf": checkout_form_vdf, 'success': "Checkout Data is not "
			                                                                               "saved"})
	checkout_vdf= CheckoutForm( instance= checkout_data)
	return render(request, 'AddCheckout.html', {"vdf": checkout_vdf})

def deleteCheckout(request,id):
	checkout_data= Checkout.objects.get(pk= id)
	checkout_data.delete()
	return redirect('Show_Checkout_Details')

def showCheckout(request):
	checkout_list_all= Checkout.objects.all()
	page_wise= Paginator(checkout_list_all, per_page= 5, orphans= 2)
	current_page= request.GET.get('page')
	checkout_list= page_wise.get_page(current_page)
	return render(request, 'ShowCheckout.html',{'checkout_list': checkout_list})

def paymentProcess(request):
	host= request.get_host()
	paypal_dict= {
		'business': settings.PAYPAL_RECEIVER_EMAIL,
		'name': str(request.session['first_name']),
		'amount': request.session['amount'],
		'phone': request.session['contact_phone'],
		'receipt_no': str(request.session['payer_id']),
		'item_name': 'Checkout #' + str(request.session['payer_id']),
		'invoice': str(request.session['payer_id']),
		'currency_code': 'INR',
		'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
		'done_return': 'http://{}{}'.format(host, reverse('Payment_Done')),
		'cancel_return': 'http://{}{}'.format(host, reverse('Payment_Cancelled')),
	}
	form= PayPalPaymentsForm(initial= paypal_dict)
	return render(request, 'PaymentProcess.html', {'form': form, 'paypal_dic': paypal_dict})

@csrf_exempt
def payPalDone(request):
	# get the details of the paypal
	checkout_obj= Checkout.objects.get(pk= request.session['payer_id'])
	checkout_obj.payment_status= "Confirm"
	checkout_obj.save()

	del request.session['payer_id']
	return render(request, 'PaymentDone.html',{'pay': "Payment Successfully done"} )

@csrf_exempt
def payPalCancelled(request):
	#  Delete the order details
	checkout_obj= Checkout.objects.get(pk= request.session['payer_id'])
	# order_obj.delete()
	checkout_obj.payment_status= "Pending"
	checkout_obj.save()

	del request.session['payer_id']

	return render(request, 'PaymentCancelled.html',{'pay': "payment not done"} )



@login_required
def visitor(request):
	if request.method == 'POST':
		visitor_vdf= VisitorForm(request.POST)
		if visitor_vdf.is_valid():
			visitor_vdf.save()

			v_vdf= VisitorForm()
			return render(request, 'AddVisitor.html',{'vdf':v_vdf,'success': "New visitor data has successfully "
			                                                                 "saved"})
		else:
			return render(request, 'AddVisitor.html', {'vdf': visitor_vdf, 'success': "New visitor data has not saved"})
	vdf= VisitorForm()
	return render(request, 'AddVisitor.html', {'vdf': vdf, 'success': ""})

def updateVisitor(request,id):
	visitor_data= Visitor.objects.get(pk= id)
	if request.method == "POST":
		visitor_form_vdf= VisitorForm(request.POST)
		if visitor_form_vdf.is_valid():
			new_visitor= Visitor()

			new_visitor.name= visitor_form_vdf.cleaned_data['name']
			new_visitor.phone= visitor_form_vdf.cleaned_data['phone']
			new_visitor.date= datetime.datetime.now()

			new_visitor.id= visitor_data.id
			# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			new_visitor.patient.set_value(visitor_form_vdf.cleaned_data['patient'])

			new_visitor.save()

			return redirect("Show_Visitor_Details")
		else:
			return render(request, 'AddVisitor.html', {"vdf": visitor_form_vdf, 'success': "Visitor Data is not "
			                                                                               "saved"})
	visitor_vdf= VisitorForm( instance= visitor_data)
	return render(request, 'AddVisitor.html', {"vdf": visitor_vdf})

def deleteVisitor(request,id):
	visitor_data= Visitor.objects.get(pk= id)
	visitor_data.delete()
	return redirect('Show_Visitor_Details')

def showVisitor(request):
	visitor_list_all= Visitor.objects.all()
	page_wise= Paginator(visitor_list_all, per_page= 5, orphans= 2)
	current_page= request.GET.get('page')
	visitor_list= page_wise.get_page(current_page)
	return render(request,'ShowVisitor.html',{'v_list': visitor_list })



@login_required
def staff(request):
	if request.method == "POST":
		staff_vdf= StaffForm(request.POST)
		if staff_vdf.is_valid():
			s= Staff()
			s.name= staff_vdf.cleaned_data['name']
			s.email= staff_vdf.cleaned_data['email']
			s.salary= staff_vdf.cleaned_data['salary']
			s.address= staff_vdf.cleaned_data['address']
			s.gender= staff_vdf.cleaned_data['gender']
			s.qualification= staff_vdf.cleaned_data['qualification']
			s.designation= staff_vdf.cleaned_data['designation']
			s.contact= staff_vdf.cleaned_data['contact']
			s.join_date= staff_vdf.cleaned_data['join_date']
			s.save()

			s_vdf= StaffForm()
			return render(request, 'AddStaff.html',{'vdf':s_vdf, 'success':"new staff data has successfully saved"})
		else:
			return render(request, 'AddStaff.html',{'vdf':staff_vdf, 'success':"new staff data has successfully saved"})
	vdf= StaffForm()
	return render(request, 'AddStaff.html',{'vdf':vdf, 'success':""})

def updateStaff(request,id):
	staff_data= Staff.objects.get(pk= id)
	if request.method == "POST":
		staff_form_vdf= StaffForm(request.POST)
		if staff_form_vdf.is_valid():
			new_staff= Staff()

			new_staff.name= staff_form_vdf.cleaned_data['name']
			new_staff.email= staff_form_vdf.cleaned_data['email']
			new_staff.salary= staff_form_vdf.cleaned_data['salary']
			new_staff.address= staff_form_vdf.cleaned_data['address']
			new_staff.gender= staff_form_vdf.cleaned_data['gender']
			new_staff.qualification= staff_form_vdf.cleaned_data['qualification']
			new_staff.designation= staff_form_vdf.cleaned_data['designation']
			new_staff.contact= staff_form_vdf.cleaned_data['contact']
			new_staff.join_date= staff_form_vdf.cleaned_data['join_date']

			new_staff.s_id= staff_data.s_id
			new_staff.save()

			return redirect("Show_Staff_Details")
		else:
			return render(request, 'AddStaff.html', {"vdf": staff_form_vdf, 'success': "Staff Data is not "
			                                                                               "saved"})
	staff_vdf= StaffForm( instance= staff_data)
	return render(request, 'AddStaff.html', {"vdf": staff_vdf})

def deleteStaff(request,id):
	staff_data= Staff.objects.get(pk= id)
	staff_data.delete()
	return redirect('Show_Staff_Details')

def showStaff(request):
	staff_list_all= Staff.objects.all()
	page_wise= Paginator(staff_list_all, per_page= 5, orphans= 2)
	current_page= request.GET.get('page')
	staff_list= page_wise.get_page(current_page)
	return render(request,'ShowStaff.html',{'s_list': staff_list })



@login_required
def medicalStore(request):
	if request.method == "POST":
		m_store_vdf= MedicalStoreForm(request.POST)
		if m_store_vdf.is_valid():
			ms= MedicalStore()
			ms.name= m_store_vdf.cleaned_data['name']
			ms.type= m_store_vdf.cleaned_data['type']
			ms.mfd_date= m_store_vdf.cleaned_data['mfd_date']
			ms.exp_date= m_store_vdf.cleaned_data['exp_date']
			ms.quantity= m_store_vdf.cleaned_data['quantity']
			ms.buy_cost= m_store_vdf.cleaned_data['buy_cost']
			ms.sell_cost= m_store_vdf.cleaned_data['sell_cost']
			ms.save()

			ms_vdf= MedicalStoreForm()
			return render(request, 'AddMedicalStore.html',{'vdf':ms_vdf,'success':'New store item data has '
			                                                                          'successfully saved'})
		else:
			return render(request, 'AddMedicalStore.html', {'vdf': m_store_vdf, 'success': 'New store item data has '
			                                                                              'not saved'})
	m_vdf= MedicalStoreForm()
	return render(request, 'AddMedicalStore.html', {'vdf': m_vdf, 'success': ''})

def updateMedicalStore(request,id):
	ms_data= MedicalStore.objects.get(pk= id)
	if request.method == "POST":
		ms_form_vdf= MedicalStoreForm(request.POST)
		if ms_form_vdf.is_valid():
			new_ms= MedicalStore()
			new_ms.name= ms_form_vdf.cleaned_data['name']
			new_ms.type= ms_form_vdf.cleaned_data['type']
			new_ms.mfd_date= ms_form_vdf.cleaned_data['mfd_date']
			new_ms.exp_date= ms_form_vdf.cleaned_data['exp_date']
			new_ms.quantity= ms_form_vdf.cleaned_data['quantity']
			new_ms.buy_cost= ms_form_vdf.cleaned_data['buy_cost']
			new_ms.sell_cost= ms_form_vdf.cleaned_data['sell_cost']

			new_ms.id= ms_data.id
			new_ms.save()

			return redirect("Show_Medical_Store_Details")
		else:
			return render(request, 'AddMedicalStore.html', {"vdf": ms_form_vdf, 'success': "MedicalStore Data is not "
			                                                                               "saved"})
	ms_vdf= MedicalStoreForm( instance= ms_data)
	return render(request, 'AddMedicalStore.html', {"vdf": ms_vdf})

def deleteMedicalStore(request,id):
	ms_data= MedicalStore.objects.get(pk= id)
	ms_data.delete()
	return redirect('Show_Medical_Store_Details')

def showMedicalStore(request):
	medical_store_list_all= MedicalStore.objects.all()
	page_wise= Paginator(medical_store_list_all, per_page= 5, orphans= 2)
	current_page= request.GET.get('page')
	medical_store_list= page_wise.get_page(current_page)
	return render(request,'ShowMedicalStore.html',{'ms_list': medical_store_list })



@login_required
def orderMedicine(request):
	if request.method == "POST":
		order_vdf= OrderMedicineForm(request.POST)
		if order_vdf.is_valid():
			order_vdf.save()

			latest_payment= OrderMedicine.objects.latest('id')
			request.session['payer_id']= latest_payment.id
			request.session['first_name']= str(order_vdf.cleaned_data['name'])
			request.session['contact_phone']= order_vdf.cleaned_data['phone']
			request.session['amount']= str(order_vdf.cleaned_data['buy_cost'])

			return redirect('Order_Payment_Process')
		else:
			return render(request, 'OrderMedicine.html', {'vdf': order_vdf,'success' :'Your order is not '
			                                                                          'successfully save'})

	order= OrderMedicineForm()
	return render(request, 'OrderMedicine.html',{'vdf': order})

def showOrderMedicine(request):
	order_list_all= OrderMedicine.objects.all()
	page= Paginator(order_list_all, per_page= 10, orphans= 3)
	current_page= request.GET.get('page')
	order_list= page.get_page(current_page)
	return render(request,'ShowOrderMedicine.html',{"order_list": order_list})

def orderPaymentProcess(request):
	host= request.get_host()
	paypal_dict= {
		'business': settings.PAYPAL_RECEIVER_EMAIL,
		'name': str(request.session['first_name']),
		'amount': request.session['amount'],
		'phone': request.session['contact_phone'],
		'receipt_no': str(request.session['payer_id']),
		'item_name': 'Checkout #' + str(request.session['payer_id']),
		'invoice': str(request.session['payer_id']),
		'currency_code': 'INR',
		'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
		'done_return': 'http://{}{}'.format(host, reverse('Payment_Done')),
		'cancel_return': 'http://{}{}'.format(host, reverse('Payment_Cancelled')),
	}
	form= PayPalPaymentsForm(initial= paypal_dict)
	return render(request, 'OrderPaymentProcess.html', {'form': form, 'paypal_dic': paypal_dict})

@csrf_exempt
def orderPaymentDone(request):
	# get the details of the paypal
	order_obj= OrderMedicine.objects.get(pk= request.session['payer_id'])
	order_obj.payment_status= "Confirm"
	order_obj.save()

	del request.session['payer_id']
	return render(request, 'OrderPaymentDone.html',{'pay': "Payment Successfully done"} )

@csrf_exempt
def orderPaymentCancelled(request):
	#  Delete the order details
	order_obj= OrderMedicine.objects.get(pk= request.session['payer_id'])
	# order_obj.delete()
	order_obj.payment_status= "Pending"
	order_obj.save()

	del request.session['payer_id']

	return render(request, 'OrderPaymentCancelled.html',{'pay': "payment not done"} )



@login_required
def showHome(request):
	return render(request, "Home.html", {'title': "Hospital Management System- Home page"})



def showContactDetails(request):
	return render(request,'ContactDetails.html',{})



def adminForm(request):
	if request.method == 'POST':
		admin_form_vdf= AdminForm(request.POST)
		if admin_form_vdf.is_valid():
			# create aan object for User model for authentications
			# this function save dataa to the database automatically . there is no need to use save() function
			User.objects.create_user(
				username= admin_form_vdf.cleaned_data['email_id'],
				first_name= admin_form_vdf.cleaned_data['name'],
				email= admin_form_vdf.cleaned_data['email_id'],
				password= admin_form_vdf.cleaned_data['password']
			)

			admin_vdf= AdminForm()
			return render(request, "AdminForm.html", {'vdf': admin_vdf,'success':"you are successfully register"})

		else:
			return render(request, "AdminForm.html", {'vdf': admin_form_vdf,'success':"you are not successfully register"})

	admin_vdf= AdminForm()

	return render(request, "AdminForm.html", {'vdf': admin_vdf,'title':'registration Page'})

@login_required
def showAdmin(request):
	admin_list_all= Admin.objects.all()
	pages= Paginator(admin_list_all,per_page= 10,orphans= 3)
	current_page= request.GET.get('page')
	admin_list= pages.get_page(current_page)
	return render(request,'ShowAdmin.html',{'admin_list': admin_list, 'title' :'Admin list'})
