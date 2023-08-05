#!/usr/bin python
# -*- coding: utf-8 -*-
"""Provide GCSError defines and GCSError exception class."""
# too many lines in module pylint: disable=C0302
# line too long pylint: disable=C0301

import json
import os

from ...PILogger import PIDebug
from ..pierror_base import PIErrorBase

__signature__ = 0xce0657d2e84dfab9f090ad9f7e87cd1d

# /*!
#  * \brief Structure of an UMF error.
#  * \- RSD:   		Reserved bit
#  * \- FGroup ID: 	Functional Group ID
#  * \- Error Class:  Config or Processing error
#  * \- Error Code:   The error code
#  *  _______________________________________________________________________________________________________________________________
#  * |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
#  * |               Reserve                 |          ErrorClass           |                     ErrorID                           |
#  * |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
#  *
#  */

# error definition begin  ## DO NOT MODIFY THIS LINE!!!
E0_PI_ERROR_NO_ERROR = 0
E49154_PI_ERROR_CMD_CMD_NUMBER_OF_ARGUMENTS = 49154
E49155_PI_ERROR_CMD_CMD_UNKNOWN_COMMAND = 49155
E49156_PI_ERROR_CMD_CMD_COMMAND_LEVEL_TOO_LOW_FOR_COMMAND_ACCESS = 49156
E49157_PI_ERROR_CMD_CMD_INVALID_PWD = 49157
E49158_PI_ERROR_CMD_CMD_UNKNOWN_SECTION_COMMAND = 49158
E49159_PI_ERROR_CMD_CMD_INVALID_CHAR = 49159
E81928_PI_ERROR_CMD_MOT_STP = 81928
E245769_PI_ERROR_PARAM_DBG_WRONG_DATA_TYPE = 245769
E49161_PI_ERROR_PARAM_CMD_WRONG_DATA_TYPE = 49161
E49162_PI_ERROR_PARAM_CMD_UNKNOWN_PARAMETER_ID = 49162
E49163_PI_ERROR_PARAM_CMD_COMMAND_LEVEL_TOO_LOW_FOR_PARAMETER_ACCESS = 49163
E49164_PI_ERROR_PARAM_CMD_INVALID_VALUE = 49164
E49165_PI_ERROR_PARAM_CMD_WRONG_PARAMETER_TYPE = 49165
E49166_PI_ERROR_PARAM_CMD_VALUE_OUT_OF_RANGE = 49166
E49167_PI_ERROR_MOT_CMD_UNKNOWN_AXIS_ID = 49167
E49168_PI_ERROR_MOT_CMD_ON_LIMIT_SWITCH = 49168
E49169_PI_ERROR_MOT_CMD_INVALID_MODE_OF_OPERATION = 49169
E49170_PI_ERROR_MOT_CMD_AXIS_NOT_REF = 49170
E81938_PI_ERROR_MOT_MOT_AXIS_NOT_REF = 81938
E49171_PI_ERROR_MOT_CMD_INVALID_AXIS_STATE = 49171
E49172_PI_ERROR_MOT_CMD_TARGET_OUT_OF_RANGE = 49172
E49173_PI_ERROR_MOT_CMD_AXIS_DISABLED = 49173
E49174_PI_ERROR_MOT_CMD_FAULT_REACTION_ACTIVE = 49174
E81943_PI_ERROR_MOT_MOT_LIMIT_SWITCH_ACTIVATED = 81943
E81944_PI_ERROR_MOT_MOT_OVER_CURRENT_PROTECTION = 81944
E32793_PI_ERROR_MOT_WARN_OUTPUT_LIMIT = 32793
E81946_PI_ERROR_MOT_MOT_POSITION_ERROR_TOO_LARGE = 81946
E81947_PI_ERROR_MOT_MOT_STOP = 81947
E245788_PI_ERROR_REC_DBG_MAX_DATA_RECORDER_NUMBER_REACHED = 245788
E245789_PI_ERROR_REC_DBG_ALREADY_REGISTERED = 245789
E49182_PI_ERROR_REC_CMD_WRONG_FORMAT = 49182
E49183_PI_ERROR_REC_CMD_UNKNOWN_RECORDER_ID = 49183
E49184_PI_ERROR_REC_CMD_NOT_IN_CONFIG_MODE = 49184
E49185_PI_ERROR_REC_CMD_WRONG_RECORDER_TRIGGER = 49185
E49186_PI_ERROR_REC_CMD_WRONG_STARTPOINT = 49186
E49187_PI_ERROR_REC_CMD_WRONG_NUMPOINT = 49187
E49188_PI_ERROR_REC_CMD_ALREADY_RUNNING = 49188
E49189_PI_ERROR_REC_CMD_TRACE_DOES_NOT_EXIST = 49189
E49190_PI_ERROR_REC_CMD_NOT_ENOUGH_RECORDED_DATA = 49190
E49191_PI_ERROR_REC_CMD_TRACES_NOT_CONFIGURED = 49191
E32808_PI_ERROR_COM_WARN_COMMUNICATION_ERROR = 32808
E49193_PI_ERROR_COM_CMD_FW_INDEX_UNKNOWN = 49193
E65578_PI_ERROR_COM_CRIT_TIMEOUT = 65578
E65579_PI_ERROR_COM_CRIT_INVALID_SOCKET = 65579
E245804_PI_ERROR_SYS_DBG_WRONG_UNIT_ID_FORMAT = 245804
E245805_PI_ERROR_SYS_DBG_UNIT_NOT_INITIALIZED = 245805
E245806_PI_ERROR_SYS_DBG_MAX_CONNECTION_NUMBER_REACHED = 245806
E245807_PI_ERROR_SYS_DBG_CONNECTION_OUTPUT_WRONG_ARGUMENTS = 245807
E245808_PI_ERROR_SYS_DBG_CONNECTION_INPUT_WRONG_ARGUMENTS = 245808
E245809_PI_ERROR_SYS_DBG_WRONG_DEVICE_ID = 245809
E245810_PI_ERROR_SYS_DBG_WRONG_FUNCTION_ID = 245810
E245811_PI_ERROR_SYS_DBG_WRONG_PROXY_ID = 245811
E245812_PI_ERROR_SYS_DBG_CONNECTION_OUTPUT_INDEX_OUT_OF_RANGE = 245812
E245813_PI_ERROR_SYS_DBG_INTERFACE_REGISTRATION_FAILED = 245813
E245814_PI_ERROR_SYS_DBG_DEVICE_REGISTRATION_FAILED = 245814
E245815_PI_ERROR_SYS_DBG_PROXY_REGISTRATION_FAILED = 245815
E16440_PI_ERROR_SYS_INFO_INPUT_PORT_ALREADY_CONNECTED = 16440
E16441_PI_ERROR_SYS_INFO_UNIT_ALREADY_REGISTERED = 16441
E16442_PI_ERROR_SYS_INFO_CONNECTION_HAS_NO_INPUT = 16442
E16443_PI_ERROR_SYS_INFO_CONNECTION_HAS_NO_OUTPUT = 16443
E16444_PI_ERROR_SYS_INFO_CONNECTION_NOT_FOUND = 16444
E16445_PI_ERROR_SYS_INFO_INPUT_PORT_NOT_CONNECTED = 16445
E32830_PI_ERROR_SYS_WARN_DATA_CORRUPT = 32830
E49215_PI_ERROR_SYS_CMD_UNIT_TYPE_NOT_SUPPORTED = 49215
E65599_PI_ERROR_SYS_CRIT_UNIT_TYPE_NOT_SUPPORTED = 65599
E49216_PI_ERROR_SYS_CMD_FW_UPDATE_ERROR = 49216
E49217_PI_ERROR_SYS_CMD_UNIT_NOT_FOUND = 49217
E49218_PI_ERROR_SYS_CMD_CUNIT_NOT_FOUND = 49218
E49219_PI_ERROR_SYS_CMD_FUNIT_NOT_FOUND = 49219
E65604_PI_ERROR_SYS_CRIT_NOT_ENOUGH_MEMORY = 65604
E65605_PI_ERROR_SYS_CRIT_FLASH_READ_FAILED = 65605
E65606_PI_ERROR_SYS_CRIT_NO_DATA_AVAILABLE = 65606
E65607_PI_ERROR_SYS_CRIT_FATAL_ERROR = 65607
E49224_PI_ERROR_MOT_CMD_AXIS_IN_FAULT = 49224
E81993_PI_ERROR_MOT_MOT_REF_SIGNAL_NOT_FOUND = 81993
E65610_PI_ERROR_SYS_CRIT_TIMEOUT = 65610
E49227_PI_ERROR_MOT_CMD_ON_IPR = 49227
E16459_PI_ERROR_MOT_INFO_ON_IPR = 16459
E81996_PI_ERROR_MOT_MOT_HALT_WAS_COMMANDED = 81996
E81919_PI_ERROR_SYS_CRIT_SYS_UNIT_TYPE_NOT_SUPPORTED = 81919
E65535_PI_ERROR_SYS_CMD_UNIT_TYPE_WRONG = 65535

# error definition end  ## DO NOT MODIFY THIS LINE!!!


PI_GCS30_ERRORS_ERRORS_DICT_KEY = 'errors'
PI_GCS30_ERRORS_CLASSES_DICT_KEY = 'classes'
PI_GCS30_ERRORS_MODULES_DICT_KEY = 'modules'
PI_GCS30_ERRORS_ID_KEY = 'id'
PI_GCS30_ERRORS_CLASS_KEY = 'class'
PI_GCS30_ERRORS_MODULE_KEY = 'module'
PI_GCS30_ERRORS_DESCRIPTION_KEY = 'description'
PI_GCS30_ERRORS_TYP_KEY = 'typ'
PI_GCS30_ERRORS_VALUE_KEY = 'value'
PI_GCS30_ERRORS_ALIAS_KEY = 'alias'

ERROR_FILE_PATH = os.path.dirname(__file__) + '/Error.json'
POSSIBLE_ERRORS = {}

def parse_error_jdson(file_name):
    """
    Parses the jdson file 'file_name' into a dictionary which is usede by the PIPython to handle the errors
    :param file_name: the GCS3 3.0 Error jdson file (path and file)
    :return: dic which ist used by PIPython to handle the errors
    """
    possible_errors = {}
    error_jdson = json.load(file_name)
    for dict_key in error_jdson:
        if dict_key == PI_GCS30_ERRORS_ERRORS_DICT_KEY:
            possible_errors[PI_GCS30_ERRORS_ERRORS_DICT_KEY] = {}
            for err_id in error_jdson[PI_GCS30_ERRORS_ERRORS_DICT_KEY]:
                error_module_key = error_jdson[PI_GCS30_ERRORS_ERRORS_DICT_KEY][err_id][
                    PI_GCS30_ERRORS_MODULE_KEY]

                module_alias = error_jdson[PI_GCS30_ERRORS_MODULES_DICT_KEY][error_module_key][
                    PI_GCS30_ERRORS_ALIAS_KEY]

                for class_key in error_jdson[PI_GCS30_ERRORS_ERRORS_DICT_KEY][err_id][PI_GCS30_ERRORS_CLASS_KEY]:
                    error_class_alias = error_jdson[PI_GCS30_ERRORS_CLASSES_DICT_KEY][class_key][
                        PI_GCS30_ERRORS_ALIAS_KEY]
                    error_key = err_id.replace('$MODULE', module_alias).replace('$CLASS', error_class_alias)
                    error_dict = error_jdson[PI_GCS30_ERRORS_ERRORS_DICT_KEY][err_id].copy()
                    error_dict[PI_GCS30_ERRORS_CLASS_KEY] = class_key
                    possible_errors[PI_GCS30_ERRORS_ERRORS_DICT_KEY][error_key] = error_dict

        else:
            possible_errors[dict_key] = error_jdson[dict_key]

    return possible_errors

with open(ERROR_FILE_PATH, 'r') as error_file:
    POSSIBLE_ERRORS = parse_error_jdson(error_file)

class GCS30Error(PIErrorBase):
    """GCSError exception."""

    def __init__(self, value, message=''):
        """GCSError exception.
        :param value : Error value as integer.
        :param message : Optional message to show in exceptions string representation.
        """
        PIErrorBase.__init__(self, value, message)
        if isinstance(value, GCS30Error):
            self.err = value.err
        else:
            self.err = GCS30Error.get_error_dict(value)
            if self.err:
                self.msg = self.translate_error(self.err)

        PIDebug('GCS30Error: %s', self.msg)

    @staticmethod
    def translate_error(value):
        """Return a readable error message of 'value'.
        :param value : Error value as integer or a gcs30 error dictionary.
        :return : Error message as string if 'value' was an integer else 'value' itself.
        """

        if not isinstance(value, (int, dict)):
            return value

        if isinstance(value, int):
            error_dict = GCS30Error.get_error_dict(value)
        else:
            error_dict = value

        try:
            msg = 'ERROR: ' + str(error_dict[PI_GCS30_ERRORS_VALUE_KEY]) + '\n'
            msg = msg + error_dict[PI_GCS30_ERRORS_DESCRIPTION_KEY] + ' (' + str(
                error_dict[PI_GCS30_ERRORS_ID_KEY]) + ')\n'
            msg = msg + error_dict[PI_GCS30_ERRORS_CLASS_KEY][PI_GCS30_ERRORS_DESCRIPTION_KEY] + ' (' + str(
                error_dict[PI_GCS30_ERRORS_CLASS_KEY][PI_GCS30_ERRORS_ID_KEY]) + ')\n'
        except KeyError:
            if isinstance(value, int):
                error_class, error_id = GCS30Error.parse_errorcode(value)
                msg = 'ERROR: ' + str(value) + '\nUnknown error: class: ' + str(
                    error_class) + ', error: ' + str(error_id) + '\n'
            else:
                msg = 'ERROR: Unknown error\n'

        return msg

    @staticmethod
    def parse_errorcode(error_number):
        """
        parses a error code returnd by the controller into the mocule, class, and error number
        :param error_number: the error code
        :return: [moduel, class, error_number]
        """
        error_class = (error_number & 0x0003C000) >> 14
        error_id = error_number & 0x00003fff

        return error_class, error_id

    @staticmethod
    def parse_to_errorcode(error_class, error_id):
        """
        parses module id, error class and error id to error number
        :type module_id: int
        :param error_class: the error class
        :type error_class: int
        :param error_id: the error id
        :type error_id: int
        :return: error_number
        """
        error_number = (((error_class << 14) & 0x0003C000) | \
                       (error_id & 0x00003fff))
        return error_number

    @staticmethod
    def get_error_dict(error_number):
        """
        gets the gcs30 error dictionary form the error number
        :param error_number:
        :return:
        """
        error_dict = {}
        error_class, error_id = GCS30Error.parse_errorcode(error_number)

        classes_dict = {}
        for classe in POSSIBLE_ERRORS[PI_GCS30_ERRORS_CLASSES_DICT_KEY]:
            if POSSIBLE_ERRORS[PI_GCS30_ERRORS_CLASSES_DICT_KEY][classe][PI_GCS30_ERRORS_ID_KEY] == error_class:
                classes_dict = POSSIBLE_ERRORS[PI_GCS30_ERRORS_CLASSES_DICT_KEY][classe]
                classes_dict[PI_GCS30_ERRORS_TYP_KEY] = classe

        for err in POSSIBLE_ERRORS[PI_GCS30_ERRORS_ERRORS_DICT_KEY]:
            if POSSIBLE_ERRORS[PI_GCS30_ERRORS_ERRORS_DICT_KEY][err][PI_GCS30_ERRORS_ID_KEY] == error_id and \
                    POSSIBLE_ERRORS[PI_GCS30_ERRORS_ERRORS_DICT_KEY][err][
                        PI_GCS30_ERRORS_CLASS_KEY] == classes_dict[PI_GCS30_ERRORS_TYP_KEY]:
                error_dict = {PI_GCS30_ERRORS_TYP_KEY: err}
                error_dict[PI_GCS30_ERRORS_CLASS_KEY] = classes_dict
                error_dict[PI_GCS30_ERRORS_ID_KEY] = POSSIBLE_ERRORS[PI_GCS30_ERRORS_ERRORS_DICT_KEY][err][
                    PI_GCS30_ERRORS_ID_KEY]
                error_dict[PI_GCS30_ERRORS_DESCRIPTION_KEY] = POSSIBLE_ERRORS[PI_GCS30_ERRORS_ERRORS_DICT_KEY][err][
                    PI_GCS30_ERRORS_DESCRIPTION_KEY]
                error_dict[PI_GCS30_ERRORS_VALUE_KEY] = error_number

        return error_dict
