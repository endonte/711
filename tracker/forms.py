from django import forms
from .models import Driver, Store, StoreRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from dal import autocomplete



class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = (
                'driver_full_name',
                'driver_nickname',
                'driver_contact_no',
                'driver_wechat_id',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        #self.helper.form_action = ''
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(DriverForm, self).__init__(*args, **kwargs)


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = (
                'store_no',
                'store_address1',
                'store_address2',
                'store_postal',
                'store_contact_no',
                'store_district_area',
                'assigned_driver',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        #self.helper.form_action = ''
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(StoreForm, self).__init__(*args, **kwargs)


class StoreRequestForm(forms.ModelForm):
    #requesting_store = forms.ModelChoiceField(
    #    queryset=Store.objects.all(),
    #    widget=autocomplete.ModelSelect2(url='tracker/storerequest-autocomplete'),
    #)
    class Meta:
        model = StoreRequest
        fields = (
                'requesting_store',
                'assigned_driver',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        #self.helper.form_action = ''
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(StoreRequestForm, self).__init__(*args, **kwargs)
