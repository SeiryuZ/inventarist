from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import OperationProductForm


@staff_member_required
def product_operation(request, operation):
    form = OperationProductForm(data=request.POST or None, operation=operation)
    if request.method == 'POST':
        if form.is_valid():
            product = form.save()
            product.logs.create(user=request.user, product=product, action=2)

            operation_string = 'dikurangi' if form.operation == 'substraction' else 'ditambah'
            message_string = "%s dari jumlah %s telah %s %s menjadi %s" % (product.name,
                                                                           form.quantity_was,
                                                                           operation_string,
                                                                           form.operation_quantity,
                                                                           product.quantity)
            messages.success(request, message_string)
            return redirect('/administration/product-operation/%s' % operation)

        print form.errors
    context = {
        'form': form,
        'operation': operation
    }
    return render(request, 'admin/product_operation.html', context)
