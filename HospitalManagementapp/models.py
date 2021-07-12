from django.db import models
from django.db.models.functions import datetime
from django.utils.timezone import now
class Admin( models.Model ):
	id = models.AutoField(primary_key=True,null=False,blank=False)
	name= models.CharField( max_length= 50, unique= True, null= False, blank= False )
	phone_no= models.CharField( max_length= 10, null= False, blank= False, unique= True )
	email_id= models.EmailField( max_length= 50, null= False, blank= False, unique= True , help_text="this is your "
	                                                                                                 "user name")
	password= models.CharField( max_length= 10, null= False, blank= False, unique= True )


class Department(models.Model ):
	id= models.AutoField(primary_key= True, null= False, blank= False )
	name= models.CharField(max_length= 50, null= False, blank= False )
	head= models.CharField(max_length= 50, null= False, blank= False )

	def __str__(self ):
		return "%s" % self.name


class Doctor(models.Model ):
	id= models.AutoField(primary_key= True, null= False, blank= False )
	name= models.CharField(max_length= 50, null= False, blank= False )
	d_o_b= models.DateField(null= False, blank= False)
	gender= models.CharField(max_length= 10, null= False, blank= False )
	phone= models.CharField(max_length= 10, null= False, blank= False )
	email= models.EmailField(max_length= 50, null= False, blank= False )
	address= models.CharField(max_length= 50, null= False, blank= False )
	degree= models.CharField(max_length= 100, null= False, blank= False )
	department= models.ForeignKey(Department, on_delete= models.CASCADE, default= 0, blank= False, null= False )

	def __str__(self ):
		return "%s" % self.name


class Patient(models.Model ):
	id= models.AutoField(primary_key= True, null= False, blank= False )
	name= models.CharField(max_length= 200, null= False, blank= False )
	age= models.IntegerField(null= False, blank= False )
	d_o_b= models.DateField( null= False, blank= False )
	blood= models.CharField(max_length= 10, null= False, blank= False )
	gender= models.CharField(max_length= 10, null= False, blank= False )
	phone= models.CharField(max_length= 10, null= False, blank= False )
	disease= models.CharField(max_length= 100, null= False, blank= False )
	address= models.CharField(max_length= 100, null= False, blank= False )
	room_no= models.CharField(max_length= 100, null= False, blank= False )
	date= models.DateField( default= datetime.datetime.now(), null= False, blank= False )
	doctor= models.ForeignKey( Doctor, on_delete= models.CASCADE, default= None, null= False, blank= False  )

	def __str__( self  ):
		return "%s" %self.name


class Room( models.Model ):
	room_status= ( ( 'empty', 'Empty'  ), ( 'full', 'Full'  )  )
	id= models.AutoField( primary_key= True, null= False, blank= False  )
	room_no= models.IntegerField( null= False, blank= False  )
	room_type= models.CharField( max_length= 50, null= False, blank= False )
	status= models.CharField( max_length= 20, default= 'Empty', choices= room_status, null= False, blank= False )
	no_of_bed= models.IntegerField( null= False, blank= False )
	price= models.IntegerField( null= False, blank= False )

	def __str__( self ):
		return "%d" % self.room_no


class Visitor( models.Model ):
	id= models.AutoField( primary_key= True, blank= False, null= False  )
	name= models.CharField( max_length= 50, null= False, blank= False  )
	phone= models.CharField( max_length= 10, null= False  )
	patient= models.CharField( max_length=50,null=False, blank= False  )
	date = models.DateField(default=datetime.datetime.now(),null=False, blank=False)

	def __str__( self  ):
		return "%s" % self.name


class Staff( models.Model ):
	s_id= models.AutoField( primary_key= True, null= False, blank= False )
	name= models.CharField( max_length= 50, null= False, blank= False )
	contact= models.CharField( max_length= 10, null= False, blank= False )
	email= models.EmailField( max_length= 50, null= False, blank= False )
	gender= models.CharField( max_length= 20, null= False, blank= False )
	designation= models.CharField( max_length= 50, null= False, blank= False )
	qualification= models.CharField( max_length= 50, null= False, blank= False )
	join_date= models.DateField( null= False, blank= False, help_text= "date must be in ( mm/dd/yy ) format" )
	salary= models.IntegerField( null= False, blank= False )
	address= models.CharField( max_length= 50, null= False, blank= False )

	def __str__( self ):
		return "%s" % self.name


class Checkout( models.Model ):
	bill_no= models.AutoField( primary_key= True, null= False, blank= False )
	patient= models.CharField( max_length=50, null= False, blank= False )
	d_o_b= models.DateField( null= False, blank= False )
	gender= models.CharField( max_length= 20, null= False, blank= False )
	age= models.IntegerField( null= False, blank= False )
	contact= models.CharField( max_length= 10, null= False, blank= False )
	address= models.CharField( max_length= 50, null= False, blank= False )
	disease= models.CharField( max_length= 50, null= False, blank= False )
	date_of_adm= models.DateField( null= False, blank= False )
	date_of_dis= models.DateField( null= False, blank= False )
	room_no= models.IntegerField( null= False, blank= False )
	payment_status= models.CharField( max_length= 50, default= "Pending", null= False, blank= False )
	total_bill= models.IntegerField( null= False, blank= False )


class MedicalStore( models.Model ):
	id= models.AutoField( primary_key= True, null= False, blank= False )
	name= models.CharField( max_length= 50, null= False, blank= False )
	buy_cost= models.DecimalField( max_digits= 10, decimal_places= 2, null= False, blank= False )
	sell_cost= models.DecimalField( max_digits= 10, decimal_places= 2, null= False, blank= False )
	quantity= models.IntegerField( null= False, blank= False )
	type= models.CharField( max_length= 50, null= True, blank= True )
	mfd_date= models.DateField( null= False, blank= False )
	exp_date= models.DateField( null= False, blank= False )

	def __str__( self ):
		return "%s" % self.name


class OrderMedicine( models.Model ):
	id= models.AutoField( primary_key= True, null= False, blank= False )
	name= models.CharField( max_length= 50, null= False, blank= False )
	phone= models.CharField( max_length= 10, null= False, blank= False )
	med_name= models.ManyToManyField( MedicalStore,default=0, blank= False )
	buy_cost= models.DecimalField( max_digits= 10, decimal_places= 2, null= False, blank= False )
	order_date= models.DateField( default= datetime.datetime.now(), null= False,
	                              blank= False )
	payment_status= models.CharField( max_length= 50, default= "Pending", null= False, blank= False )
