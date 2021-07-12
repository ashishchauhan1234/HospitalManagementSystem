from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.utils.datetime_safe import datetime

from .models import *
from django import forms
from django.utils.translation import ugettext as _


class DepartmentForm(forms.ModelForm): 
	class Meta: 
		model= Department
		fields= ['name', 'head']

		labels = {
			'name': _("Department name"), 
			'head': _("director name"),
			}

	def clean_name(self): 
		input_dept_name= self.cleaned_data['name']
		if len(input_dept_name.strip()) == 0: 
			raise forms.ValidationError("please enter department name")

		return input_dept_name

	def clean_head(self): 
		input_head_name= self.cleaned_data['head']
		if len(input_head_name.strip()) == 0: 
			raise forms.ValidationError("please enter the name of department's head")
		return input_head_name


gender_choice= (('Male', 'Male'), ('Female', 'Female'))
class DoctorForm(forms.ModelForm): 
	gender= forms.ChoiceField(choices= gender_choice, widget= forms.RadioSelect())

	class Meta: 
		model= Doctor
		fields= ['name', 'gender', 'degree', 'department', 'phone', 'address', 'email','d_o_b']

		labels= {
			'name': _('name'),
			'd_o_b': _("Date of Birth"),
			'gender': _("Gender"),
			'phone': _('Phone no'),
			'email': _('Email Id'),
			'address': _('Address'),
			'degree': _("Qualification"),
			'department': _('department'),
		}

	def clean_name(self): 
		input_doc_name= self.cleaned_data['name']
		if len(input_doc_name.strip()) == 0:
			raise forms.ValidationError("please enter doctor name")
		return input_doc_name

	def clean_d_o_b(self):
		input_dob= self.cleaned_data['d_o_b']
		if input_dob == None:
			raise forms.ValidationError("please enter Date of birth")
		return input_dob

	def clean_gender(self):
		input_gen= self.cleaned_data['gender']
		if len(input_gen.strip()) == 0:
			raise forms.ValidationError("please enter gender")
		return input_gen

	def clean_phone(self):
		input_phone= self.cleaned_data['phone']
		if len(input_phone) < 10:
			raise forms.ValidationError("please enter correct patient phone no")
		elif not input_phone.isdigit():
			raise forms.ValidationError("all character must be integer")
		return input_phone

	def clean_email(self):
		input_email= self.cleaned_data['email']
		validator= EmailValidator("Enter valid email Id")
		validator(input_email)
		return input_email

	def clean_address(self): 
		input_add= self.cleaned_data['address']
		if len(input_add.strip()) == 0: 
			raise forms.ValidationError("please enter doctor address")
		return input_add

	def clean_degree(self):
		input_degree= self.cleaned_data['degree']
		if len(input_degree.strip()) == 0:
			raise forms.ValidationError("please enter degree")

		return input_degree



class PatientForm(forms.ModelForm):
	gender= forms.ChoiceField(choices= gender_choice, widget= forms.RadioSelect())

	class Meta:
		model= Patient
		fields= ['name', 'age', 'gender', 'phone', 'disease', 'doctor', 'address', 'date', 'room_no', 'blood','d_o_b']

		labels= {
			'name': _("name"),
			'age': _("age"),
			'd_o_b':_('Date of Birth'),
			'blood': _("Blood Group"),
			'gender': _("Gender"),
			'phone': _("Phone no"),
			'disease': _("Disease"),
			'doctor': _("Doctor name"),
		     'room_no': _('room no'),
		     'address': _('address'),
			'date': _('Admit date'),
		}


	def clean_name(self):
		input_patient_name= self.cleaned_data['name']
		if len(input_patient_name.strip()) == 0:
			raise forms.ValidationError("please enter patient name")
		return input_patient_name

	def clean_gender(self):
		input_gen= self.cleaned_data['gender']
		if len(input_gen.strip()) == 0:
			raise forms.ValidationError("please select Gender")
		return input_gen

	def clean_age(self):
		input_age= self.cleaned_data['age']
		if input_age == None:
			raise forms.ValidationError("please enter patient age")
		return input_age

	def clean_d_o_b(self):
		input_date= self.cleaned_data['d_o_b']
		if input_date == None:
			raise forms.ValidationError("please enter date of birth")
		return input_date

	def clean_phone(self):
		input_phone= self.cleaned_data['phone']
		if len(input_phone) < 10:
			raise forms.ValidationError("please enter correct patient phone no")
		elif not input_phone.isdigit():
			raise forms.ValidationError("all character must be integer")
		return input_phone

	def clean_address(self):
		input_add= self.cleaned_data['address']
		if len(input_add.strip()) == 0:
			raise forms.ValidationError("please enter patient address")
		return input_add

	def clean_blood(self):
		input_blood_grp= self.cleaned_data['blood']
		if len(input_blood_grp.strip()) == 0:
			raise forms.ValidationError("please enter patient blood grp")
		return input_blood_grp

	def clean_disease(self):
		input_disease= self.cleaned_data['disease']
		if len(input_disease.strip()) == 0:
			raise forms.ValidationError("please enter patient disease")
		return input_disease

	def clean_date(self):
		input_date= self.cleaned_data['date']
		if input_date == None:
			raise forms.ValidationError("please enter patient admitting date")
		return input_date

	def clean_room_no(self):
		input_room_no= self.cleaned_data['room_no']
		if len(input_room_no.strip()) == 0:
			raise forms.ValidationError("Please write the type of room no")
		return input_room_no

	def clean_doctor(self):
		input_doctor= self.cleaned_data['doctor']
		if input_doctor == None:
			raise forms.ValidationError("Please appoint doctor..")
		return input_doctor



class StaffForm(forms.ModelForm):
	gender= forms.ChoiceField(choices= gender_choice, widget= forms.RadioSelect())

	class Meta: 
		model= Staff
		fields= ['name', 'contact', 'gender', 'salary', 'address', 'designation', 'email', 'qualification', 'join_date']

		labels= {
			'name': _("Name"), 
			'designation': _('designation'), 
			'salary': _("Salary"), 
			'address': _("Address"), 
			'contact': _("Contact no "), 
			'gender': _("Gender"), 
			'email': _("Email Id"), 
			'join_date': _("Joining Date"), 
			'qualification': _('Qualification')
		}

	def clean_contact(self): 
		input_phone= self.cleaned_data['contact']
		if not input_phone.isdigit(): 
			raise forms.ValidationError("please enter the phone no")
		elif len(input_phone.strip()) < 10: 
			raise forms.ValidationError("please enter the correct phone no")
		return input_phone

	def clean_email(self): 
		input_email= self.cleaned_data['email']

		validator= EmailValidator("please write valid Email Id")
		validator(input_email)

		# if input_email.isdigit(): 
		# 	raise forms.ValidationError("please enter the phone no")

		return input_email

	def clean_name(self): 
		input_name= self.cleaned_data['name']
		if len(input_name.strip()) == 0: 
			raise forms.ValidationError("please enter the name")
		return input_name

	def clean_qualification(self): 
		input_qualification= self.cleaned_data['qualification']
		if len(input_qualification.strip()) == 0: 
			raise forms.ValidationError("please enter your qualification")
		return input_qualification

	def clean_join_date(self): 
		input_date= self.cleaned_data['join_date']
		if input_date == None: 
			raise forms.ValidationError("please enter your joining date")
		return input_date

	def clean_address(self): 
		input_add= self.cleaned_data['address']
		if len(input_add.strip()) == 0: 
			raise forms.ValidationError("please enter the address")
		return input_add

	def clean_gender(self): 
		input_gen= self.cleaned_data['gender']
		if len(input_gen.strip()) == 0: 
			raise forms.ValidationError("please enter the gender")
		return input_gen

	def clean_salary(self): 
		input_sal= self.cleaned_data['salary']
		if input_sal == None: 
			raise forms.ValidationError("please enter the salary")
		return input_sal

	def clean_designation(self): 
		input_des= self.cleaned_data['designation']
		if len(input_des.strip()) == 0: 
			raise forms.ValidationError("please enter the role of staff ")
		return input_des



room_choices= (('', 'Select'), ('Gen', 'General'), ('VIP', 'VIP'), ('Emg', 'Emergency room'))
class RoomForm(forms.ModelForm): 
	room_type= forms.ChoiceField(choices= room_choices, widget= forms.Select())
	class Meta: 
		model= Room
		fields= ['room_no', 'room_type', 'status', 'price', 'no_of_bed']

		labels= {
			'room_no': _("Room no"), 
			'room_type': _("Type of room"), 
			'no_of_bed': _("No of beds"), 
			'price': _("Room price")
		}

	def clean_room_no(self): 
		input_room_no= self.cleaned_data['room_no']
		if input_room_no == None: 
			raise forms.ValidationError("Please enter the room no ")
		return input_room_no

	def clean_room_type(self): 
		input_room_type= self.cleaned_data['room_type']
		if len(input_room_type.strip()) == 0: 
			raise forms.ValidationError("please write the type of room")
		return input_room_type

	def clean_status(self): 
		input_status= self.cleaned_data['status']
		if len(input_status.strip()) == 0: 
			raise forms.ValidationError("please select the status of room(is the room is either full or empty. ")
		return input_status

	def clean_price(self): 
		input_price= self.cleaned_data['price']
		if input_price == None: 
			raise forms.ValidationError("please enter the price of room")
		return input_price

	def clean_no_of_bed(self): 
		input_data= self.cleaned_data['no_of_bed']
		if input_data == None: 
			raise forms.ValidationError("please enter the no of beds in the room..")
		return input_data


class CheckoutForm(forms.ModelForm): 
	gender= forms.ChoiceField(choices= gender_choice, widget= forms.RadioSelect())

	class Meta: 
		model= Checkout
		fields= ['date_of_dis', 'date_of_adm', 'address', 'total_bill', 'age', 'gender',
		          'disease', 'contact', 'patient', 'room_no','d_o_b']

		labels= {
			'patient': _('Patient name'),
			'd_o_b': _('Date of birth'),
			'age': _(' patient age'),
			'gender': _(' gender'),
			'contact': _('Contact no'),
			'address': _('Patient address '),
			'date_of_adm': _('admitting date'),
			'disease': _('Disease'),
			'room_no': _('Room no'),
			'date_of_dis': _('Discharge Date'),
			'total_bill': _('total Amount'),
		}

	def clean_patient(self):
		input_name = self.cleaned_data['patient']
		if len(input_name) == 0:
			raise forms.ValidationError("Please enter patient name")
		return input_name

	def clean_d_o_b(self):
		input_data= self.cleaned_data['d_o_b']
		if input_data == None:
			raise forms.ValidationError("please write date of birth..")
		return input_data

	def clean_age(self):
		input_data= self.cleaned_data['age']
		if input_data == None:
			raise forms.ValidationError("please write patient age")
		return input_data

	def clean_gender(self):
		input_data= self.cleaned_data['gender']
		if len(input_data.strip()) == 0:
			raise forms.ValidationError("please write patient gender..")
		return input_data

	def clean_contact(self):
		input_data= self.cleaned_data['contact']
		if input_data == None:
			raise forms.ValidationError("please write patient contact no")
		elif not input_data.isdigit() or len(input_data) < 10:
			raise forms.ValidationError("please write correct patient contact no")
		return input_data

	def clean_room_no(self):
		input_room_no= self.cleaned_data['room_no']
		if input_room_no == None: 
			raise forms.ValidationError("please write patient room no")
		return input_room_no

	def clean_total_bill(self): 
		input_bill= self.cleaned_data['total_bill']
		if input_bill == None: 
			raise forms.ValidationError("please write total bill amount")
		return input_bill

	def clean_date_of_adm(self): 
		input_data= self.cleaned_data['date_of_adm']
		if input_data == None: 
			raise forms.ValidationError("please write patient admitted date")
		return input_data

	def clean_date_of_dis(self): 
		input_data= self.cleaned_data['date_of_dis']
		if input_data == None: 
			raise forms.ValidationError("please write patient discharge date")
		return input_data

	def clean_address(self): 
		input_data= self.cleaned_data['address']
		if len(input_data.strip()) == None: 
			raise forms.ValidationError("please write patient address..")
		return input_data

	def clean_disease(self): 
		input_data= self.cleaned_data['disease']
		if input_data == None: 
			raise forms.ValidationError("please write the patient disease ")
		return input_data


type_choice= (('tablets', 'Tablets'), ('liquid', 'Liquid'))
class MedicalStoreForm(forms.ModelForm): 
	type= forms.MultipleChoiceField(widget= forms.CheckboxSelectMultiple, choices= type_choice, label= "Forms of "
	                                                                                                  "medicine")

	class Meta: 
		model= MedicalStore
		fields= ['name', 'buy_cost', 'sell_cost', 'quantity', 'mfd_date', 'exp_date']

		labels= {
			'name': _('Medicine name'),
			'buy_cost': _('Cost Price'), 
			'sell_cost': _('Selling Price'), 
			'quantity': _('Quantity'),
			'mfd_date': _('Manufacturing Date'),
			'exp_date': _('Expiring date')
		}

	def clean_name(self): 
		input_name= self.cleaned_data['name']
		if len(input_name.strip()) == 0: 
			raise forms.ValidationError("Please Enter item names")
		return input_name

	def clean_mfd_date(self): 
		input_date= self.cleaned_data['mfd_date']
		if input_date == None: 
			raise forms.ValidationError("Please Enter manufacture date of item")
		return input_date

	def clean_exp_date(self): 
		input_date= self.cleaned_data['exp_date']
		if input_date == None: 
			raise forms.ValidationError("Please Enter Expiring date of item")
		return input_date

	def clean_quantity(self): 
		input_quantity= self.cleaned_data['quantity']
		if input_quantity == None: 
			raise forms.ValidationError("Please Enter item quantity")
		return input_quantity

	def clean_type(self): 
		input_type= self.cleaned_data['type']
		if input_type == None: 
			raise forms.ValidationError("Please select item forms")
		return input_type

	def clean_buy_cost(self): 
		input_cost= self.cleaned_data['buy_cost']
		if input_cost == None: 
			raise forms.ValidationError("Please Enter item buy price")
		return input_cost

	def clean_sell_cost(self): 
		input_date= self.cleaned_data['sell_cost']
		if input_date == None: 
			raise forms.ValidationError("Please Enter item selling price")
		return input_date


class OrderMedicineForm(forms.ModelForm): 

	class Meta: 
		model= OrderMedicine
		fields= ['name', 'phone', 'med_name', 'buy_cost', 'order_date']

		labels= {
			'name': _('Customer name'), 
			'phone': _("Phone no"), 
			'med_name': _("Medicines"),
			'buy_cost': _("Cost Price"),
			'order_date': _("Order date"),
		}

		widgets= {
			'med_name': forms.CheckboxSelectMultiple(),
		}
		error_messages= {
			'med_name': {'required': _("Please select at least one medicine ...")}
		}

	def clean_name(self): 
		input_name= self.cleaned_data['name']
		if len(input_name.strip()) == 0: 
			raise forms.ValidationError("Please enter customer name ")
		return input_name

	def clean_phone(self): 
		input_phone= self.cleaned_data['phone']
		if (not input_phone.isdigit()) or  len(input_phone.strip()) < 10: 
			raise forms.ValidationError("Please enter correct customer phone no ")
		return input_phone

	# def clean_med_name(self):
	# 	input_med= self.cleaned_data['med_name']
	# 	if input_med == 0:
	# 		raise forms.ValidationError("Please select medicines ")
	# 	return input_med

	def clean_buy_cost(self):
		input_cost= self.cleaned_data['buy_cost']
		if input_cost == None: 
			raise forms.ValidationError("Please enter cost of the medicines ")
		return input_cost

	def clean_order_date(self): 
		input_date= self.cleaned_data['order_date']
		if input_date == None: 
			raise forms.ValidationError("Please enter today date ")
		return input_date


class VisitorForm(forms.ModelForm): 
	class Meta: 
		model= Visitor
		fields= ['name', 'date', 'patient', 'phone']

		labels= {
			'name': _("Name of visitor"), 
			'phone': _("Visitor's phone no"), 
			'patient': _("Patient name"), 
			'date': _("Visiting date"),
		}

		widgets = {
			'patient': forms.CheckboxSelectMultiple(),
			'date': forms.DateInput(format="%d/%m/%Y")
		}

	def clean_name(self): 
		input_name= self.cleaned_data['name']
		if len(input_name.strip()) == 0: 
			raise forms.ValidationError("Enter the visitor name")
		return input_name

	def clean_date(self):
		input_date= self.cleaned_data['date']
		if input_date == None:
			raise forms.ValidationError("Enter the visitor date")
		return input_date

	def clean_phone(self): 
		input_phone= self.cleaned_data['phone']
		if len(input_phone.strip()) < 10: 
			raise forms.ValidationError("Enter the correct visitor phone no")
		elif not input_phone.isdigit(): 
			raise forms.ValidationError("Enter the correct phone no")
		return input_phone


class AdminForm(forms.ModelForm): 

	rePassword= forms.CharField(max_length= 10, widget= forms.PasswordInput(), label= "Re-Enter password",
	                              required= False)

	def __init__(self, *args, **kwargs): 
		super(AdminForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items(): 
			if field_name == 'password': 
				field.required= False

	class Meta: 
		model= Admin
		fields= ['name', 'password', 'phone_no', 'email_id']

		label= {
			'name': 'Enter your name', 
			'phone_no': 'Phone no', 
			'email_id': 'Email id', 
			'password': 'Password'
		}
		widgets= {
			'password': forms.PasswordInput(),
			'email_id': forms.EmailInput(help('USer name'))
		}
		help_texts= {
			'email': _("Your email is your username"), 
			'password': _("must be of 8 character")
		}

	def clean_name(self): 
		input_name= self.cleaned_data['name']
		if input_name == None or  len(input_name.strip()) == 0:
			raise forms.ValidationError("Enter the admin name")
		return input_name

	def clean_phone_no(self): 
		input_phone= self.cleaned_data['phone_no']
		if len(input_phone.strip()) < 10 or (not input_phone.isdigit()): 
			raise forms.ValidationError("Enter the correct phone no")
		return input_phone

	def clean_email(self): 
		input_email= self.cleaned_data['email']

		validator= EmailValidator("please write valid Email Id")
		validator(input_email)
		if User.objects.filter(email= input_email ).exists():
			raise forms.ValidationError("EmailId has already registered ....")
		return input_email

	def clean_password(self): 
		input_password= self.cleaned_data['password']
		if len(input_password.strip()) < 8: 
			raise forms.ValidationError("please Enter at least 8 character password")
		return input_password

	def clean_rePassword(self): 
		input_password2= self.cleaned_data['rePassword']

		if input_password2 == "": 
			raise forms.ValidationError("please Enter valid password")

		input_password= self.data['password']
		if input_password == "": 
			raise forms.ValidationError("please Enter valid password")

		if input_password != input_password2: 
			raise forms.ValidationError("password does not match ....")

		return input_password2
