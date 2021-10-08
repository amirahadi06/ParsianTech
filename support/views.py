from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import PartForm, ProductForm, PartPackForm
from .models import Part, Product, PartPack


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
    form = PartForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('part-list')

    if request.method == 'POST':
        searched_item = request.POST['searched_item']
        parts_list = Part.objects.filter(
            Q(part_name__contains=searched_item) | Q(part_supplier_name__contains=searched_item)).order_by('part_name')
    else:
        parts_list = Part.objects.all().order_by('part_name')
        searched_item = ''

    return render(request, 'support/parts_list.html',
                  {'parts_list': parts_list, 'searched_item': searched_item, 'form': form})


def part_add(request):
    # now = datetime.now()
    # date = now.date()
    # time = now.strftime('%I:%M:%S %p')
    submitted = False
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
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


def product_delete(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('product-list')


def product_update(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_parts = PartPack.objects.filter(product_name=product.id)

    if request.method == "POST" and 'data_sub' in request.POST:
        product_data_form = ProductForm(request.POST, instance=product)
        if product_data_form.is_valid():
            product_data_form.save()
    else:
        product_data_form = ProductForm(instance=product)

    if request.method == "POST" and 'part_sub' in request.POST:
        product_partpack_form = PartPackForm(request.POST)
        if product_partpack_form.is_valid():
            product_partpack_form.save()
    else:
        product_partpack_form = PartPackForm(initial={'product_name': product.id})

    return render(request, 'support/product_update.html', {
                                                           'product_data_form': product_data_form,
                                                           'product_partpack_form': product_partpack_form,
                                                           'product_parts': product_parts,
                                                           'product_name': product.product_name,
                                                           'parts_count' : product_parts.count(),
                                                            })


def product_show(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'support/product_show.html', {'product': product})


def product_list(request):
    if request.method == 'POST':
        searched_item = request.POST['searched_item']
        products_list = Product.objects.filter(Q(product_name__contains=searched_item)).order_by('product_name')
    else:
        products_list = Product.objects.all().order_by('product_name')
        searched_item = ''

    return render(request, 'support/products_list.html',
                  {'products_list': products_list, 'searched_item': searched_item})


def product_add(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'support/product_add_form.html',
                  {'form': form,
                   'submitted': submitted,
                   })


def partpack_delete(request, partpack_id):
    part = PartPack.objects.get(pk=partpack_id)
    part.delete()
    return redirect('product-update', part.product_name.id)
