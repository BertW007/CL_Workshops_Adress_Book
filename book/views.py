from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from book.models import Person, Address, Telephone, Email
from django.template import loader


class AddPerson(View):
    
    def get(self,request):
        response = HttpResponse('GET')
        template = loader.get_template('book/new_form.html')
        return render(request,'book/new_form.html')
    
    def post(self,request):
        response=HttpResponse('NEW PERSON ADDED')
        
        form_name = request.POST.get('name')
        form_surname = request.POST.get('surname')
        form_city = request.POST.get('city')
        form_street = request.POST.get('street')
        form_house_number = request.POST.get('house_number')
        form_email = request.POST.get('email')
        form_telephone = request.POST.get('telephone')
        form_type = request.POST.get('type')
        form_description = request.POST.get('description')
        
#         response.write('''
#         form_name = {}<br>
#         form_surname = {}<br>
#         form_city = {}<br>
#         form_street = {}<br>
#         form_house_number = {}<br>
#         form_email = {}<br>
#         form_telephone = {}<br>
#         form_type = {}<br>
#         form_description = {}<br>
#         '''.format(form_name,form_surname,form_city,form_street,form_house_number,form_email,form_telephone,form_type,form_description))
        
        address = Address.objects.create(city=form_city, street=form_street, house_number=form_house_number)
        person = Person.objects.create(name=form_name,surname=form_surname,description=form_description,address=address)
        email = Email.objects.create(email=form_email,person=person)
        telephone = Telephone.objects.create(tel_number=form_telephone,type=form_type,person=person)         
    
        return redirect('/all_persons/')
    
class ModifyPerson(View):
    
    def get(self,request,person_id):
        response = HttpResponse('GET')
        person = Person.objects.get(pk=person_id)
        address = person.address
        email = person.email_set.all()[0]
        telephone = person.telephone_set.all()[0]
        
        context = {'person':person,
                   'address':address,
                   'email':email,
                   'telephone':telephone}
        template = loader.get_template('book/new_form.html')
        return render(request,'book/new_form.html',context)
    
    def post(self,request,person_id):
        
        person = Person.objects.get(pk=person_id)
        
        person.name = request.POST.get('name')
        person.surname = request.POST.get('surname')
        person.city = request.POST.get('city')
        person.street = request.POST.get('street')
        person.house_number = request.POST.get('house_number')
        person.email = request.POST.get('email')
        person.telephone = request.POST.get('telephone')
        person.type = request.POST.get('type')
        person.description = request.POST.get('description')
        person.save()
        
        response=HttpResponse('PERSON DETAILS MODIFIED')       
    
        return redirect('/all_persons/')

    
def all_persons(request):
    response = HttpResponse()
    
    persons = Person.objects.order_by('name')
    response.write('''<!DOCTYPE html>
                        <html lang="en">
                        <head>
                          <title>Address Book</title>
                          <meta charset="utf-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1">
                          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
                          <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
                        </head>
                        <body>
                            <div class="col-xs-5">
                                <ol class="list-group">
                                    <li class="list-group-item active justify-content-between">
                                        <div class="row">
                                            <div class="col-xs-6"><h4>Address Book:</h4></div>
                                        </div>
                                    </li>''')
      
    for person in persons:
        response.write('''                         
                        <li class="list-group-item justify-content-between">  
                            <div class="col-xs-8"> 
                                <a href="http://127.0.0.1:8000/person_details/{}">{} {}</a>
                            </div>
                                <a href="http://127.0.0.1:8000/modify/{}" type="button" class="btn btn-primary">Edit</a>
                                <a href="http://127.0.0.1:8000/delete_person/{}" type="button" class="btn btn-danger">Delete</a>
                        </li>'''.format(person.id, person.name, person.surname,person.id,person.id))
        
    response.write('''</ol>
                        <a href="http://127.0.0.1:8000/new/" type="button" class="btn btn-success pull-right" >Add</a>
                    </div>
                    </body>
                    </html>''')
        
    return response

def delete_person(request,person_id):
    Person.objects.get(pk=person_id).delete()
    return redirect('/all_persons/')

def person_details(request,person_id):
    response = HttpResponse()
    person = Person.objects.get(pk=person_id)
    address = person.address
    email = person.email_set.all()[0]
    telephone = person.telephone_set.all()[0]
        
    context = {'person':person,
               'address':address,
               'email':email,
               'tel1':telephone.tel_number,
               'tel2':telephone.get_type_display()}
    template = loader.get_template('book/details.html')
    
    
    return render(request,'book/details.html',context)
    
   

    

    
        
    
