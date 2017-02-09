from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .forms import Register
from .models import Join
from uuid import uuid4 as uid


def get_ip(request):
    try:
        x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forward:
            ip = x_forward.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except Exception as e:
        print(e)
        ip = ""
    return ip


def get_ref_id():
    ref_id = str(uid()).replace('-', '').lower()

    try:
        # tries to retrieve ref_id, using random ref_id
        _ = Join.objects.get(ref_id=ref_id)
        # if it exists, function starts over
        print("16-bit UUID Match Error")
        get_ref_id()
    #     else it returns the ref_id as an exception
    except ObjectDoesNotExist:
        print("16-bit UUID Accepted")
        return ref_id
    # print(ref_id)
    # return ref_id


def home(request):
    # print(request.META.get('REMOTE_ADDR'))
    # model Forms
    form = Register(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        # first_name = form.cleaned_data['first_name']
        # email = form.cleaned_data['email']
        # ip_address = form.cleaned_data['ip_address']
        # new_join_old = Join.objects.filter(email=email)
        # if not new_join_old:
        #     created = Join.objects.create(first_name=first_name, email=email, ip_address=ip_address)
        new_join.ip_address = get_ip(request)
        new_join.ref_id = get_ref_id()
        new_join.save()

    context = {'form': form}
    template = 'home.html'

    return render(request=request, template_name=template, context=context)

