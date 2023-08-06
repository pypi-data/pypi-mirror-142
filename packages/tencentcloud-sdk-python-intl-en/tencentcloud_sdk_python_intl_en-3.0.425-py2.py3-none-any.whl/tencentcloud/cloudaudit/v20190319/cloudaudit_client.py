# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cloudaudit.v20190319 import models


class CloudauditClient(AbstractClient):
    _apiVersion = '2019-03-19'
    _endpoint = 'cloudaudit.tencentcloudapi.com'
    _service = 'cloudaudit'


    def DescribeAuditTracks(self, request):
        """This API is used to query the CloudAudit tracking set list.

        :param request: Request instance for DescribeAuditTracks.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditTracksRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeAuditTracksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAuditTracks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAuditTracksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEvents(self, request):
        """This API is used to query CloudAudit logs.

        :param request: Request instance for DescribeEvents.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeEventsRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)