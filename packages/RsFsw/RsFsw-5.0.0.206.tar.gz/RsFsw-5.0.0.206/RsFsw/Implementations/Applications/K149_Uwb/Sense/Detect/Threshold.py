from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Threshold:
	"""Threshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("threshold", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: [SENSe]:DETect:THReshold \n
		Snippet: driver.applications.k149Uwb.sense.detect.threshold.set(level = 1.0) \n
		Sets the detection threshold in dB/dBm relative to the burst detection reference level. \n
			:param level: numeric value Unit: dB
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SENSe:DETect:THReshold {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DETect:THReshold \n
		Snippet: value: float = driver.applications.k149Uwb.sense.detect.threshold.get() \n
		Sets the detection threshold in dB/dBm relative to the burst detection reference level. \n
			:return: level: numeric value Unit: dB"""
		response = self._core.io.query_str(f'SENSe:DETect:THReshold?')
		return Conversions.str_to_float(response)
