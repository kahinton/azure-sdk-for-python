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

from msrest.pipeline import ClientRawResponse
import uuid

from .. import models


class UsageAggregatesOperations(object):
    """UsageAggregatesOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    :ivar api_version: Client Api Version. Constant value: "2015-06-01-preview".
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2015-06-01-preview"

        self.config = config

    def list(
            self, reported_start_time, reported_end_time, show_details=None, aggregation_granularity="Daily", continuation_token=None, custom_headers=None, raw=False, **operation_config):
        """Query aggregated Azure subscription consumption data for a date range.

        :param reported_start_time: The start of the time range to retrieve
         data for.
        :type reported_start_time: datetime
        :param reported_end_time: The end of the time range to retrieve data
         for.
        :type reported_end_time: datetime
        :param show_details: `True` returns usage data in instance-level
         detail, `false` causes server-side aggregation with fewer details. For
         example, if you have 3 website instances, by default you will get 3
         line items for website consumption. If you specify showDetails =
         false, the data will be aggregated as a single line item for website
         consumption within the time period (for the given subscriptionId,
         meterId, usageStartTime and usageEndTime).
        :type show_details: bool
        :param aggregation_granularity: `Daily` (default) returns the data in
         daily granularity, `Hourly` returns the data in hourly granularity.
         Possible values include: 'Daily', 'Hourly'
        :type aggregation_granularity: str or :class:`AggregationGranularity
         <azure.mgmt.commerce.models.AggregationGranularity>`
        :param continuation_token: Used when a continuation token string is
         provided in the response body of the previous call, enabling paging
         through a large result set. If not present, the data is retrieved from
         the beginning of the day/hour (based on the granularity) passed in.
        :type continuation_token: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`UsageAggregationPaged
         <azure.mgmt.commerce.models.UsageAggregationPaged>`
        :raises:
         :class:`ErrorResponseException<azure.mgmt.commerce.models.ErrorResponseException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/providers/Microsoft.Commerce/UsageAggregates'
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['reportedStartTime'] = self._serialize.query("reported_start_time", reported_start_time, 'iso-8601')
                query_parameters['reportedEndTime'] = self._serialize.query("reported_end_time", reported_end_time, 'iso-8601')
                if show_details is not None:
                    query_parameters['showDetails'] = self._serialize.query("show_details", show_details, 'bool')
                if aggregation_granularity is not None:
                    query_parameters['aggregationGranularity'] = self._serialize.query("aggregation_granularity", aggregation_granularity, 'AggregationGranularity')
                if continuation_token is not None:
                    query_parameters['continuationToken'] = self._serialize.query("continuation_token", continuation_token, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.UsageAggregationPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.UsageAggregationPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
