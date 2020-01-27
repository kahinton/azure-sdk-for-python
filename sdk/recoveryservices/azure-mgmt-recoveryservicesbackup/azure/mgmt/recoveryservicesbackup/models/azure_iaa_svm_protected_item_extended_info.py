# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AzureIaaSVMProtectedItemExtendedInfo(Model):
    """Additional information on Azure IaaS VM specific backup item.

    :param oldest_recovery_point: The oldest backup copy available for this
     backup item.
    :type oldest_recovery_point: datetime
    :param recovery_point_count: Number of backup copies available for this
     backup item.
    :type recovery_point_count: int
    :param policy_inconsistent: Specifies if backup policy associated with the
     backup item is inconsistent.
    :type policy_inconsistent: bool
    """

    _attribute_map = {
        'oldest_recovery_point': {'key': 'oldestRecoveryPoint', 'type': 'iso-8601'},
        'recovery_point_count': {'key': 'recoveryPointCount', 'type': 'int'},
        'policy_inconsistent': {'key': 'policyInconsistent', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(AzureIaaSVMProtectedItemExtendedInfo, self).__init__(**kwargs)
        self.oldest_recovery_point = kwargs.get('oldest_recovery_point', None)
        self.recovery_point_count = kwargs.get('recovery_point_count', None)
        self.policy_inconsistent = kwargs.get('policy_inconsistent', None)