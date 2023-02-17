from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Income, Outcome, Profit
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView

import xlwt
from _datetime import datetime


class IncomeListView(ListView):
    model = Income
    template_name = 'charges/income.html'


class IncomeCreateView(CreateView):
    model = Income
    template_name = 'charges/income_create.html'
    fields = '__all__'
    success_url = reverse_lazy('income')


class IncomeUpdateView(UpdateView):
    model = Income
    template_name = 'charges/income_update.html'
    fields = '__all__'
    success_url = reverse_lazy('income')


class IncomeDeleteVieW(DeleteView):
    model = Income
    template_name = 'charges/income_delete.html'
    success_url = reverse_lazy('income')


class OutcomeListView(ListView):
    model = Outcome
    template_name = 'charges/outcome.html'


class ProfitListView(ListView):
    model = Profit
    template_name = 'charges/profit.html'


class OutcomeCreateView(CreateView):
    model = Outcome
    template_name = 'charges/outcome_create.html'
    fields = ('car_outcome_id', 'outcome_amount', 'outcome_remark')
    success_url = reverse_lazy('outcome')


def charges_default(request):
    income = Income.objects.all()
    outcome = Outcome.objects.all()
    income.delete()
    outcome.delete()
    return redirect('profit')


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="City_Rent_{date}.xls"'.format(
        date=datetime.now().strftime(
            '%d-%m-%Y'))

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('{date}.xls'.format(
        date=datetime.now().strftime(
            '%d-%m-%Y')))
    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.font.colour_index = 4
    font_style.font.height = 280
    column = ['Отчет за {date}'.format(
        date=datetime.now().strftime(
            '%B %Y'))]
    ws.write(row_num, 3, column, font_style)
    row_num += 2

    font_style.font.height = 240
    column = ['Доходы']
    ws.write(row_num, 3, column, font_style)
    row_num += 1

    font_style.font.height = 220
    columns = ['Машина', 'Номер машины', 'Сумма', 'Дата', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Income.objects.order_by('id') \
        .values_list('car_income_id__title', 'car_income_id__car_number',
                     'income_amount', 'order_date')

    rows = [[x.strftime("%d-%m-%Y") if isinstance(x, datetime) else x for x in row] for row in rows]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    row_num += 2

    # Расходы
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.font.colour_index = 4
    font_style.font.height = 240
    column = ['Расходы']
    ws.write(row_num, 3, column, font_style)
    row_num += 1

    font_style.font.height = 220
    columns = ['Машина', 'Номер машины', 'Сумма', 'Дата', 'Ремарка', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    outcome_rows = Outcome.objects.order_by('id') \
        .values_list('car_outcome_id__title', 'car_outcome_id__car_number',
                     'outcome_amount', 'order_date', 'outcome_remark')

    outcome_rows = [[x.strftime("%d-%m-%Y") if isinstance(x, datetime) else x for x in row] for row in outcome_rows]
    for row in outcome_rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    row_num += 2

    # Прибыль
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.font.colour_index = 4
    font_style.font.height = 240
    column = ['Прибыль']
    ws.write(row_num, 3, column, font_style)
    row_num += 1

    font_style.font.height = 220
    columns = ['Машина', 'Номер машины', 'Сумма', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Profit.objects.order_by('id') \
        .values_list('car_profit_id__title', 'car_profit_id__car_number',
                     'amount')

    rows = [[x.strftime("%d-%m-%Y") if isinstance(x, datetime) else x for x in row] for row in rows]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    row_num += 2

    wb.save(response)
    return response
