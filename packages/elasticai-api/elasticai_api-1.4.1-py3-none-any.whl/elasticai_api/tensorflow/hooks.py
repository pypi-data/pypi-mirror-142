# Copyright 2021 The ElasticDL Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

import tensorflow as tf
from tensorflow.python.training import training_util
from tensorflow.python.training.session_run_hook import (
    SessionRunArgs,
    SessionRunHook,
)

from elasticai_api.common.master_client import GlobalMasterClient
from elasticai_api.util.log_utils import default_logger as logger


class ReportModelMetricHook(SessionRunHook):
    def __init__(self):
        """Report variables and operators in a model to
        the ElasticDL master.
        """
        self._last_timestamp = 0
        self._start_session_time = 0
        self._is_chief = False
        super(ReportModelMetricHook, self).__init__()

    def begin(self):
        from alps.core.global_vars import global_context

        self._is_chief = global_context().is_chief
        if not self._is_chief:
            return
        self._start_session_time = int(time.time())
        self._global_step = training_util._get_or_create_global_step_read()

    def after_create_session(self, session, coord):
        if not self._is_chief:
            return
        try:
            trainable_variables = tf.trainable_variables()
            all_ops = tf.get_default_graph().get_operations()
            GlobalMasterClient.MASTER_CLIENT.report_model_metric(
                trainable_variables, len(all_ops)
            )
            self._last_timestamp = int(time.time())
        except Exception as e:
            logger.warning("Fail to report model metrics", e)

    def before_run(self, run_context):  # pylint: disable=unused-argument
        if not self._is_chief:
            return
        return SessionRunArgs(self._global_step)

    def after_run(self, run_context, run_values):
        if not self._is_chief:
            return
        try:
            global_step = run_values.results
            timestamp = int(time.time())
            secs = self.get_wait_seconds(timestamp)
            if global_step > 100 and timestamp - self._last_timestamp > secs:
                logger.info("Report global step = {}".format(global_step))
                self._last_timestamp = timestamp
                GlobalMasterClient.MASTER_CLIENT.report_global_step(
                    global_step, self._last_timestamp
                )
        except Exception:
            logger.info("Fail to report global step")

    def get_wait_seconds(self, timestamp):
        """Adjust the waited seconds by the training time"""
        if timestamp - self._start_session_time < 1800:
            return 60
        elif timestamp - self._start_session_time < 3600:
            return 180
        else:
            return 300
