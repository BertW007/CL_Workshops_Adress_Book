from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from book.models import Person, Address, Telephone, Email
from django.template import loader

class AddPerson(View):
    
    def get(self,request):
        template = loader.get_template('book/new_form.html')
        return render(request,'book/new_form.html')
    
    def post(self,request):
        form_name = request.POST.get('name')
        form_surname = request.POST.get('surname')
        form_city = request.POST.get('city')
        form_street = request.POST.get('street')
        form_house_number = request.POST.get('house_number')
        form_email = request.POST.get('email')
        form_telephone = request.POST.get('telephone')
        form_type = request.POST.get('type')
        form_description = request.POST.get('description')
        
        address = Address.objects.create(city=form_city, street=form_street, house_number=form_house_number)
        person = Person.objects.create(name=form_name,surname=form_surname,description=form_description,address=address)
        email = Email.objects.create(email=form_email,person=person)
        telephone = Telephone.objects.create(tel_number=form_telephone,type=form_type,person=person)         
    
        return redirect('/person_details/{}'.format(person.id))
    
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
    
        return redirect('/person_details/{}'.format(person_id))
    
class AllPersons(View):
    
    def get(self,request):
        response = HttpResponse('GET')
        persons = Person.objects.order_by('name')
        context = {'persons':persons}
        template = loader.get_template('book/all_persons.html')
          
        return render(request,'book/all_persons.html',context)
        
    def post(self,request):
        persons = Person.objects.filter(name__icontains=request.POST.get('search'))|Person.objects.filter(surname__icontains=request.POST.get('search'))
        persons = persons.order_by('name')
        context = {'persons':persons}
        template = loader.get_template('book/all_persons.html')
           
        return render(request,'book/all_persons.html',context)

# def all_persons(request):
#     
#     
#     persons = Person.objects.order_by('name')
#     context = {'persons':persons}
#     template = loader.get_template('book/all_persons.html')
#       
#     return render(request,'book/all_persons.html',context)

def delete_person(request,person_id):
    Person.objects.get(pk=person_id).delete()
    return redirect('/all_persons/')

def person_details(request,person_id):
    response = HttpResponse()
    person = Person.objects.get(pk=person_id)
    address = person.address
    telephones = person.telephone_set.all()
    emails = person.email_set.all()
        
    context = {'person':person,
               'address':address,
               'telephones':telephones,
               'emails':emails}
    template = loader.get_template('book/details.html')
      
    return render(request,'book/details.html',context)

class AddEmail(View):
    
    def get(self,request,person_id):
        person = Person.objects.get(pk=person_id)
        template = loader.get_template('book/email.html')
        context = {'person':person}
        return render(request,'book/email.html',context)
    
    def post(self,request,person_id):
        form_email = request.POST.get('email')
        person = Person.objects.get(pk=person_id)
        email = Email.objects.create(email=form_email,person=person)
        return redirect('/person_details/{}'.format(person_id))

class EditEmail(View):
    
    def get(self,request,person_id,email_id):
        person = Person.objects.get(pk=person_id)
        email = person.email_set.get(pk=email_id)
        context = {'person':person,
                   'email':email,
                   }
        template = loader.get_template('book/email.html')
        return render(request,'book/email.html',context)
    
    def post(self,request,person_id,email_id):
        person = Person.objects.get(pk=person_id)
        email = Email.objects.get(pk=email_id) 
        email.email = request.POST.get('email')
        email.save()       
        return redirect('/person_details/{}'.format(person_id))

def delete_email(request,person_id,email_id):
    Email.objects.get(pk=email_id).delete()
    return redirect('/person_details/{}'.format(person_id))

class AddTelephone(View):
    
    def get(self,request,person_id):
        person = Person.objects.get(pk=person_id)
        template = loader.get_template('book/telephone.html')
        context = {'person':person}
        return render(request,'book/telephone.html',context)
    
    def post(self,request,person_id):
        form_telephone = request.POST.get('telephone')
        form_type = request.POST.get('type')
        person = Person.objects.get(pk=person_id)
        telephone = Telephone.objects.create(tel_number=form_telephone,type=form_type,person=person)
        return redirect('/person_details/{}'.format(person_id))

class EditTelephone(View):
    
    def get(self,request,person_id,telephone_id):
        person = Person.objects.get(pk=person_id)
        telephone = person.telephone_set.get(pk=telephone_id)
        context = {'person':person,
                   'telephone':telephone,
                   }
        template = loader.get_template('book/telephone.html')
        return render(request,'book/telephone.html',context)
    
    def post(self,request,person_id,telephone_id):
        person = Person.objects.get(pk=person_id)
        telephone = Telephone.objects.get(pk=telephone_id) 
        telephone.tel_number = request.POST.get('telephone')
        telephone.type = request.POST.get('type')
        telephone.save()       
        return redirect('/person_details/{}'.format(person_id))

def delete_telephone(request,person_id,telephone_id):
    Telephone.objects.get(pk=telephone_id).delete()
    return redirect('/person_details/{}'.format(person_id))
    

    
        
    
