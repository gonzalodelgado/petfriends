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

from django.db import models


PET_TYPES = 'dog', 'cat', 'bird', 'other'


class Client(models.Model):
    """
    A pet owner
    """
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    home_address = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_pets(self):
        return self.pet_set.all()


class Pet(models.Model):
    """
    A pet
    """
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    pet_type = models.CharField(max_length=10,
        choices=[(choice, choice) for choice in PET_TYPES])
    owner = models.ForeignKey(Client)

    def __unicode__(self):
        return u'%s, %s\'s %s' % (self.name, self.owner, self.pet_type)
