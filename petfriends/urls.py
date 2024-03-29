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

from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.views.generic import DetailView

from clientsandpets.models import Client
from clientsandpets.views import ClientCreateView, ClientSerializedDetailView


urlpatterns = patterns('',
    url(r'^$', ClientCreateView.as_view(
        template_name='create_client.html', success_url='/%(id)d/confirm/'),
       name='client_create'),
    url(r'^(?P<pk>\d+)/confirm/$', DetailView.as_view(
        template_name='create_client_confirm.html', model=Client)),
    url(r'^clients/(?P<pk>\d+)/$', ClientSerializedDetailView.as_view(
        model=Client)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
