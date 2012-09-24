import backbone
from backbone.views import BackboneAPIView
from django_erd.models import ModelRenderSettings

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils import simplejson
from django.utils.translation import ugettext as _


class ModelRenderSettings(BackboneAPIView):
    model = ModelRenderSettings
    display_fields = ('name', 'fields', 'foreign_keys', 'top', 'left', 'z', 'selected')

    def get_collection(self, request):
        """
        Handles get requests for the list of all objects.
        """
        qs = self.queryset(request)
        data = [
            self.serialize(obj, ['id'] + list(self.display_fields)) for obj in qs
        ]
        return HttpResponse(self.json_dumps(data), mimetype='application/json')

    def put(self, request, id=None):
        """
        Handles put requests.
        """
        data = simplejson.loads(request.raw_post_data)
        id = data.get('id', None)
        if id:
            obj = get_object_or_404(self.queryset(request), id=id)
            if not self.has_update_permission(request, obj):
                return HttpResponseForbidden(_('You do not have permission to perform this action.'))
            else:
                return self.update_object(request, obj)
        else:
            # No putting on a collection.
            return HttpResponseForbidden()


backbone.site.register(ModelRenderSettings)
