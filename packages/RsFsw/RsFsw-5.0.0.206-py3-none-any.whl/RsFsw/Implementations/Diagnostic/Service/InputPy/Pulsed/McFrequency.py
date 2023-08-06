from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McFrequency:
	"""McFrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcFrequency", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: DIAGnostic:SERVice:INPut:PULSed:MCFRequency \n
		Snippet: driver.diagnostic.service.inputPy.pulsed.mcFrequency.set(frequency = 1.0) \n
		This command sets the calibration frequency for frequencies greater than 7 GHz. This command only takes effect if a
		microwave calibration signal is selected for input (method RsFsw.Diagnostic.Service.InputPy.Select.set) . \n
			:param frequency: Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'DIAGnostic:SERVice:INPut:PULSed:MCFRequency {param}')

	def get(self) -> float:
		"""SCPI: DIAGnostic:SERVice:INPut:PULSed:MCFRequency \n
		Snippet: value: float = driver.diagnostic.service.inputPy.pulsed.mcFrequency.get() \n
		This command sets the calibration frequency for frequencies greater than 7 GHz. This command only takes effect if a
		microwave calibration signal is selected for input (method RsFsw.Diagnostic.Service.InputPy.Select.set) . \n
			:return: frequency: Unit: Hz"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:INPut:PULSed:MCFRequency?')
		return Conversions.str_to_float(response)
