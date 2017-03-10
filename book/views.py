from django.shortcuts import render
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
    
        return response
    
class ModifyPerson(View):
    
    def get(self,request,person_id):
        response = HttpResponse('GET')
        person = Person.objects.get(pk=person_id)
        address = person.address
        
        context = {'person':person}
        template = loader.get_template('book/new_form.html')
        return render(request,'book/new_form.html',context)
    
    def post(self,request):
        response=HttpResponse('NEW PERSON MODIFIED')
        
        
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
        
#         address = Address.objects.create(city=form_city, street=form_street, house_number=form_house_number)
#         person = Person.objects.create(name=form_name,surname=form_surname,description=form_description,address=address)
#         email = Email.objects.create(email=form_email,person=person)
#         telephone = Telephone.objects.create(tel_number=form_telephone,type=form_type,person=person)         
    
        return response

    
def all_persons(request):
    response = HttpResponse()
    
    persons = Person.objects.all()
    response.write('Address Book:<br>')
    response.write('<ol>')   
    for person in persons:
        response.write('<li>{} {}</li>'.format(person.name, person.surname))
    response.write('</ol>')
        
    return response
