from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from datetime import timedelta
from django.db.models import Max
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from django.db.models import Sum
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
# Create your views here.
from . models import Studentinfo, CaseProfile, GoodMoral, CommunityServiceTracker
from .decorators import sao_admin_required

def NewCase(request):
    query = request.GET.get('q')
    student = None
    no_student_found = False

    if query:
        try:
            student = Studentinfo.objects.get(studentID=query)
        except Studentinfo.DoesNotExist:
            student = None
            no_student_found = True

    if request.method == "POST" and student:
        violation = request.POST.get('violation')
        description = request.POST.get('description')
        received_by = request.POST.get('received_by')
        reported_by = request.POST.get('reported_by')
        case_date = request.POST.get('case_date')
        case_class = request.POST.get('classified')
      
        case_profile = CaseProfile.objects.create(
            student=student,
            violation=violation, 
            description=description, 
            received_by=received_by,
            reported_by=reported_by,
            case_date=case_date,
            case_class=case_class,
            # sanction_completed = status
        )
        student.sanction_completed = False
        case_profile.determine_sanction()

        # Return JSON response indicating success
        return JsonResponse({'success': True})

    context = {'student': student, 'query': query, 'no_student_found': no_student_found}
    return render(request, 'base/newCaseProfile.html', context)

    
from django.shortcuts import get_object_or_404

def caseList(request):
    query = request.GET.get('q')
    student = None
    cases = CaseProfile.objects.none()  # Initialize cases with an empty queryset
    suspension_end_date = None
    no_student_found = False

    if query:
        try:
            student = Studentinfo.objects.get(studentID=query)
            student_not_exist = False
        except Studentinfo.DoesNotExist:
            student = None
            no_student_found = True

    if student:
        cases = CaseProfile.objects.filter(student=student)
        student_exist = True
    if request.method == "POST" and student:
        sanction = request.POST.get('sanction')
        service_hours = request.POST.get('service-hours')
        if service_hours is None or service_hours == '':
                service_hours = 0
        service_deadline = request.POST.get('service-deadline')
        # if service_deadline == '':
        #         service_deadline = None
        suspension_duration = request.POST.get('suspension_duration')

        if service_deadline == '1':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=1)
        elif service_deadline == '2':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=2)
        elif service_deadline == '3':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=3)
        elif service_deadline == '4':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=4)
        elif service_deadline == '5':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=5)
        elif service_deadline == '6':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=6)
        elif service_deadline == '7':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=7)
        elif service_deadline == '8':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=8)
        elif service_deadline == '9':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=9)
        elif service_deadline == '10':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=10)
        elif service_deadline == '11':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=11)
        elif service_deadline == '12':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=12)
        elif service_deadline == '13':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=13)
        elif service_deadline == '14':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=14)
        elif service_deadline == '15':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=15)
        elif service_deadline == '16':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=16)
        elif service_deadline == '17':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=17)
        elif service_deadline == '18':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=18)
        elif service_deadline == '19':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=19)
        elif service_deadline == '20':
            service_end_date = student.caseprofile_set.first().case_date + timedelta(weeks=20)
        else:
            service_end_date = None

        if suspension_duration == '1':
            suspension_end_date = student.caseprofile_set.first().case_date + timedelta(days=4 * 30)
        elif suspension_duration == '2':
            suspension_end_date = student.caseprofile_set.first().case_date + timedelta(days=8 * 30)

        # Update student attributes instead of creating a new object
        student.sanction = sanction
        student.community_service_hours = service_hours
        student.community_service_deadline = service_end_date
        student.suspension_start_date = student.caseprofile_set.first().case_date
        student.suspension_end_date = suspension_end_date
        student.save()

    context = {
        'student': student,
        'cases': cases,
        'no_student_found': no_student_found
    }
    return render(request, 'base/NewCase-list.html', context)


#COMMUNITY SERVICE TABLE
def serviceTracker(request, student_id):
    student = get_object_or_404(Studentinfo, studentID=student_id)
    if student:
        community_services = CommunityServiceTracker.objects.filter(student=student)
        time_rendered = [service.time_rendered() for service in community_services]
        total_hours = 0
        total_minutes = 0
        
        for service in community_services:
            hours, minutes = service.total_time_rendered()
            total_hours += hours
            total_minutes += minutes
        
        # Adjust total hours if total minutes exceed 60
        total_hours += total_minutes // 60
        total_minutes %= 60
        
        if student.community_service_hours is not None:
            total_time_rendered_hours = total_hours
            if total_time_rendered_hours >= student.community_service_hours:
                student.sanction_completed = True
                student.save()
            else:
                student.sanction_completed = False
                student.save()

    if request.method == "POST" and student:
        date_str = request.POST.get('service_date')
        service_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        time_in = request.POST.get('time_in')
        time_out = request.POST.get('time_out')
        student_signature = request.POST.get('student_signature')
        remarks = request.POST.get('remarks')

        CommunityServiceTracker.objects.create(
            student = student,
            service_date = service_date,
            time_in = time_in,
            time_out = time_out,
            student_signature = student_signature,
            remarks = remarks
        )

        return redirect(reverse('studentLife_discipline:community-service-tracker', args=[student_id]))
    
    context = {'student':student, 'community_services':community_services, 'time_rendered':time_rendered, 'total_hours': total_hours,
        'total_minutes': total_minutes}
    return render(request, 'base/CommunityServiceTracker.html', context)

#GOOD MORAL
def req_goodmoral(request):
    no_student_found = False 

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if student_id:
            try:
                student = Studentinfo.objects.get(studentID=student_id)
                return redirect('studentLife_discipline:goodmoral_detail', student_id=student_id)
            except Studentinfo.DoesNotExist:
                student = None
                no_student_found = True
                # return HttpResponse("No student found")
            
    context = {'no_student_found': no_student_found}
    return render(request, 'base/goodmoral_login.html', context)

def goodmoral_detail(request, student_id):
    student = get_object_or_404(Studentinfo, studentID=student_id)
    cases = student.caseprofile_set.count()

    # Check if the student has already made a GoodMoral request
    existing_request = GoodMoral.objects.filter(student=student).first()
    request_made = False
    can_make_request = True

    if existing_request:
        one_week_ago = timezone.now() - timedelta(weeks=1)
        if existing_request.decision_date and existing_request.decision_date > one_week_ago:
            can_make_request = False

    if request.method == "POST" and student and can_make_request:
        reason = request.POST.get('student_reason')
        uploaded_file = request.FILES.get('apology_letter')
        
        if reason:
            # Create a new GoodMoral request
            GoodMoral.objects.create(
                student=student,
                reason=reason,
                decision_date=timezone.now()  
            )
            request_made = True 
        
        if uploaded_file:
            # Update the student's apology letter
            student.apology_letter = uploaded_file
            student.save()
        return redirect('studentLife_discipline:goodmoral_detail', student_id=student_id)
    
    if student.sanction == "apology_letter":
        if student.apology_letter:
            student.sanction_completed = True
            student.save()

    context = {
        'student': student,
        'case_count': cases,
        'existing_request': existing_request,
        'request_made': request_made,
        'can_make_request': can_make_request,
    }
    return render(request, 'base/goodmoralTable.html', context)
def GoodMoralTemplate(request, student_id):
    student = Studentinfo.objects.get(studentID=student_id)
    goodmoral = GoodMoral.objects.filter(student=student)
    cases = student.caseprofile_set.count()

    context={
        'student': student,
        'goodmoral': goodmoral,
        'cases':cases,
    }
    return render(request, 'base/good_moral_certificate.html', context)

#TRASANCTION REPORT
@sao_admin_required
def transaction(request):
    goodmorals = GoodMoral.objects.all()
    query = request.GET.get('query')
    date_filter = request.GET.get('date_filter')
    month_filter = request.GET.get('month_filter')
    current_time = timezone.now()

    # Check and reset status if one week has passed
    one_week_ago = current_time - timedelta(weeks=1)
    for goodmoral in goodmorals:
        if goodmoral.decision_date and goodmoral.decision_date < one_week_ago:
            goodmoral.is_approved = False
            goodmoral.is_declined = False
            goodmoral.decision_date = None
            goodmoral.save()

    if query:
        goodmorals = goodmorals.filter(
            Q(student__lastname__icontains=query) |
            Q(student__firstname__icontains=query) |
            Q(student__middlename__icontains=query)
        )

    if date_filter == 'daily':
        goodmorals = goodmorals.filter(created__date=current_time.date())

    if month_filter:
        month_filter = int(month_filter)
        goodmorals = goodmorals.filter(created__month=month_filter, created__year=current_time.year)

    return render(request, 'base/Transactionreport.html', {'goodmorals': goodmorals})

def approve_request(request, pk):
    goodmoral = get_object_or_404(GoodMoral, pk=pk)
    goodmoral.is_approved = True
    goodmoral.is_declined = False
    goodmoral.decision_date = timezone.now()  # Set decision date
    goodmoral.save()
    return redirect('studentLife_discipline:transaction')

def decline_request(request, pk):
    goodmoral = get_object_or_404(GoodMoral, pk=pk)
    goodmoral.is_approved = False
    goodmoral.is_declined = True
    goodmoral.decision_date = timezone.now()  # Set decision date
    goodmoral.save()
    return redirect('studentLife_discipline:transaction')
#COMPLETING CRUD OPERATIONS
@require_http_methods(["DELETE"])
def deletecaserecord(request, pk):
    case = get_object_or_404(CaseProfile, pk=pk)
    case.delete()
    return JsonResponse({'message': 'Case deleted successfully'}, status=200)

def updateCase(request, pk):
    case = get_object_or_404(CaseProfile, pk=pk)
    student = case.student

    if request.method == "POST":
        case.violation = request.POST.get('violation')
        case.description = request.POST.get('description')
        case.received_by = ", ".join(request.POST.getlist('received_by[]'))
        case.reported_by = request.POST.get('reported_by')
        case.case_date = request.POST.get('case_date')
        case.save()
        case.determine_sanction()

        # Return a JSON response indicating success
        return JsonResponse({'success': True})

    context = {
        'case': case,
        'student': student,
        'query': student.studentID
    }
    return render(request, 'base/update-case.html', context)


#MODALS
def savedcaseprofile(request):
    return render(request, 'modal/SavedCaseProfile.html')

#def deletecaserecord(request):
#    return render(request, 'modal/deleteCaseRecord.html')

