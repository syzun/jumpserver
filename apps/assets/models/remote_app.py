# coding: utf-8
#

import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from orgs.mixins import OrgModelMixin
from common.fields.model import EncryptJsonDictTextField
from .. import const


__all__ = [
    'RemoteApp',
]


class RemoteApp(OrgModelMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    asset = models.ForeignKey(
        'assets.Asset', on_delete=models.CASCADE, verbose_name=_('Asset')
    )
    system_user = models.ForeignKey(
        'assets.SystemUser', on_delete=models.CASCADE,
        verbose_name=_('System user')
    )
    type = models.CharField(
        default=const.REMOTE_APP_TYPE_CHROME,
        choices=const.REMOTE_APP_TYPE_CHOICES,
        max_length=128, verbose_name=_('RemoteApp type')
    )
    path = models.CharField(
        max_length=128, blank=False, null=False,
        verbose_name=_('RemoteApp path')
    )
    params = EncryptJsonDictTextField(
        max_length=4096, blank=True, null=True, verbose_name=_('parameters')
    )
    created_by = models.CharField(
        max_length=32, null=True, blank=True, verbose_name=_('Created by')
    )
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name=_('Date created')
    )
    comment = models.TextField(
        max_length=128, default='', blank=True, verbose_name=_('Comment')
    )

    class Meta:
        verbose_name = _("RemoteApp")
        unique_together = [('org_id', 'name')]

    def __str__(self):
        return self.name
