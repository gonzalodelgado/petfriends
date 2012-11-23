# Copyright 2012 Gonzalo Delgado
#
# This file is part of petfriends.
#
# petfriends is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# petfriends is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with petfriends.  If not, see <http://www.gnu.org/licenses/>.

from django.views.generic import CreateView
from django.forms.models import inlineformset_factory

from clientsandpets.models import Client, Pet
from clientsandpets.forms import PetFormSet
from clientsandpets.conf.settings import MAX_PETS



class ClientCreateView(CreateView):
    model = Client
    formset_class = inlineformset_factory(
        Client, Pet, formset=PetFormSet, can_delete=False, extra=MAX_PETS)

    def data_valid(self, form, formset):
        response = self.form_valid(form)    # calls form.save
        formset.instance = self.object
        formset.save()
        return response

    def data_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset))

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form(self.get_form_class())
        formset = self.formset_class(save_as_new=True)
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form(self.get_form_class())
        formset = self.formset_class(request.POST)
        if form.is_valid() and formset.is_valid():
            return self.data_valid(form, formset)
        else:
            return self.data_invalid(form, formset)
