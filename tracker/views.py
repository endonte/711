from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from seveneleven.users.models import User
from django.utils import timezone
from .models import Driver, Store, StoreRequest
from .forms import DriverForm, StoreForm, StoreRequestForm
from dal import autocomplete

class StoreRequestAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        #if not self.request.user.is_authenticated():
        #    return StoreRequest.objects.none()

        qs = Store.objects.all()

        if self.q:
            qs = qs.filter(store_no__istartswith=self.q)

        return qs

class StoreListView(ListView, ModelFormMixin):
    model = Store
    form_class = StoreForm
    template_name = 'seveneleven/store-list.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.save()
            self.form = self.get_form(self.form_class)

            return HttpResponseRedirect('/tracker/stores')

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(StoreListView, self).get_context_data(*args, **kwargs)

        context['stores'] = Store.objects.all()
        context['form'] = self.form
        context['errorlist'] = self.form.errors

        return context

class DriverListView(ListView, ModelFormMixin):
    model = Driver
    form_class = DriverForm
    template_name = 'seveneleven/driver-list.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.save()
            self.form = self.get_form(self.form_class)

            return HttpResponseRedirect('/tracker/drivers')

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(DriverListView, self).get_context_data(*args, **kwargs)

        context['drivers'] = Driver.objects.all()
        context['form'] = self.form
        context['errorlist'] = self.form.errors

        return context


class CreateRequestListView(ListView, ModelFormMixin):
    model = StoreRequest
    form_class = StoreRequestForm
    template_name = 'seveneleven/create-request.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save(commit=False)
            self.object.request_created_by = request.user
            self.object.request_date = timezone.now()
            self.object.save()
            self.form = self.get_form(self.form_class)

            return HttpResponseRedirect('/tracker/requests')

        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateRequestListView, self).get_context_data(*args, **kwargs)

        context['storerequests'] = StoreRequest.objects.exclude(request_invoice_no__isnull=False)
        context['form'] = self.form
        context['errorlist'] = self.form.errors

        return context
