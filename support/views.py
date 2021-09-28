from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import PartForm
from .models import Part
from datetime import datetime


class IndexView(generic.ListView):
    template_name = 'support/index.html'
    queryset = ''


def part_delete(request, part_id):
    part = Part.objects.get(pk=part_id)
    part.delete()
    return redirect('part-list')


def part_update(request, part_id):
    part = Part.objects.get(pk=part_id)
    form = PartForm(request.POST or None, instance=part)
    if form.is_valid():
        form.save()
        return redirect('part-list')
    return render(request, 'support/part_update.html', {'form': form})


def part_show(request, part_id):
    part = Part.objects.get(pk=part_id)
    return render(request, 'support/part_show.html', {'part': part})


def part_list(request):

    if request.method == 'POST':
        searched_item = request.POST['searched_item']
        parts_list = Part.objects.filter(Q(part_name__contains=searched_item) | Q(part_supplier_name__contains=searched_item)).order_by('part_name')
    else:
        parts_list = Part.objects.all().order_by('part_name')
        searched_item = ''
    return render(request, 'support/parts_list.html', {'parts_list': parts_list, 'searched_item': searched_item})


def part_add(request):
    # now = datetime.now()
    # date = now.date()
    # time = now.strftime('%I:%M:%S %p')
    submitted = False
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/parts/add?submitted=True')
    else:
        form = PartForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'support/part_add_form.html',
                  {'form': form,
                   'submitted': submitted,
                   # 'date': date,
                   # 'time': time,
                   })
