from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from book.models import Person, Address, Telephone, Email
from django.template import loader


class AddPerson(View):
    
    def get(self,request):
        response = HttpResponse('GET')
        template = loader.get_template('book/new_form.html')
        return HttpResponse(template.render())
    
    def post(self,request):
        response=HttpResponse('POST')
        
#         form_name = request.POST.get('name')
#         form_year = int(request.POST.get('year'))
#         form_active = bool(request.POST.get('is_active'))
#         
#         student = Student.objects.create(name=form_name,year_at_university=form_year,is_active=form_active)
        
        return response
    
def all_persons(request):
    response = HttpResponse()
    
    persons = Person.objects.all()
    response.write('Address Book:<br>')
    response.write('<ol>')   
    for person in persons:
        response.write('<li>{}</li>'.format(person.name))
    response.write('</ol>')
        
    return response
