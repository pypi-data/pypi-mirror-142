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
		Snippet: driver.applications.k6Pulse.sense.detect.threshold.set(level = 1.0) \n
		The threshold determines whether a pulse is detected or not. The top of a pulse must exceed the threshold in order to be
		detected. The threshold is defined in relation to the reference defined by [SENSe:]DETect:REFerence. \n
			:param level: numeric value in dB or dBm, depending on reference type
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SENSe:DETect:THReshold {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DETect:THReshold \n
		Snippet: value: float = driver.applications.k6Pulse.sense.detect.threshold.get() \n
		The threshold determines whether a pulse is detected or not. The top of a pulse must exceed the threshold in order to be
		detected. The threshold is defined in relation to the reference defined by [SENSe:]DETect:REFerence. \n
			:return: level: numeric value in dB or dBm, depending on reference type"""
		response = self._core.io.query_str(f'SENSe:DETect:THReshold?')
		return Conversions.str_to_float(response)
