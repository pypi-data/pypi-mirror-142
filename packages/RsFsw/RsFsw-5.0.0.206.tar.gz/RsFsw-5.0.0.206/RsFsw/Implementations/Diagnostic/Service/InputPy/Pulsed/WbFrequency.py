from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WbFrequency:
	"""WbFrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wbFrequency", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: DIAGnostic:SERVice:INPut:PULSed:WBFRequency \n
		Snippet: driver.diagnostic.service.inputPy.pulsed.wbFrequency.set(frequency = 1.0) \n
		Defines the frequency of the internal broadband calibration signal to be used for IF filter calibration. This command is
		only available if the bandwidth extension option R&S FSW-B160 is installed. Before you can use the command, you have to
		feed in a calibration signal with method RsFsw.Diagnostic.Service.InputPy.Select.set. \n
			:param frequency: 2 MHz | 4 MHz | 8 MHz | 16 MHz If you define a frequency that is not available, the R&S FSW uses the next available frequency. Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'DIAGnostic:SERVice:INPut:PULSed:WBFRequency {param}')

	def get(self) -> float:
		"""SCPI: DIAGnostic:SERVice:INPut:PULSed:WBFRequency \n
		Snippet: value: float = driver.diagnostic.service.inputPy.pulsed.wbFrequency.get() \n
		Defines the frequency of the internal broadband calibration signal to be used for IF filter calibration. This command is
		only available if the bandwidth extension option R&S FSW-B160 is installed. Before you can use the command, you have to
		feed in a calibration signal with method RsFsw.Diagnostic.Service.InputPy.Select.set. \n
			:return: frequency: 2 MHz | 4 MHz | 8 MHz | 16 MHz If you define a frequency that is not available, the R&S FSW uses the next available frequency. Unit: Hz"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:INPut:PULSed:WBFRequency?')
		return Conversions.str_to_float(response)
