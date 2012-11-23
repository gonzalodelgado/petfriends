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

from django.forms import ValidationError
from django.forms.models import BaseInlineFormSet

from clientsandpets.conf.settings import MIN_PETS


class PetFormSet(BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            return super(PetFormSet, self).clean()
        cleaned_data_count = len(filter(lambda f: f.cleaned_data, self.forms))
        if cleaned_data_count < MIN_PETS:
            raise ValidationError('Client must have at least %s pet' % MIN_PETS)
        return super(PetFormSet, self).clean()
