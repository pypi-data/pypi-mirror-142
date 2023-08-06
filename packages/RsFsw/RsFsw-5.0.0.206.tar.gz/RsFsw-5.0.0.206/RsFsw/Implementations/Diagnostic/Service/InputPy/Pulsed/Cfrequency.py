from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cfrequency:
	"""Cfrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfrequency", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: DIAGnostic:SERVice:INPut:PULSed:CFRequency \n
		Snippet: driver.diagnostic.service.inputPy.pulsed.cfrequency.set(frequency = 1.0) \n
		This command defines the frequency of the calibration signal. Before you can use the command, you have to feed in a
		calibration signal with method RsFsw.Diagnostic.Service.InputPy.Select.set. \n
			:param frequency: Possible frequencies of the calibration signal are fix. If you define a frequency that is not available, the R&S FSW uses the next available frequency. Example: a frequency of 20 MHz is rounded up to the next available frequency (25 MHz) . Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'DIAGnostic:SERVice:INPut:PULSed:CFRequency {param}')

	def get(self) -> float:
		"""SCPI: DIAGnostic:SERVice:INPut:PULSed:CFRequency \n
		Snippet: value: float = driver.diagnostic.service.inputPy.pulsed.cfrequency.get() \n
		This command defines the frequency of the calibration signal. Before you can use the command, you have to feed in a
		calibration signal with method RsFsw.Diagnostic.Service.InputPy.Select.set. \n
			:return: frequency: Possible frequencies of the calibration signal are fix. If you define a frequency that is not available, the R&S FSW uses the next available frequency. Example: a frequency of 20 MHz is rounded up to the next available frequency (25 MHz) . Unit: Hz"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:INPut:PULSed:CFRequency?')
		return Conversions.str_to_float(response)
