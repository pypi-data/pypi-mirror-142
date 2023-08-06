from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, sample_rate: float) -> None:
		"""SCPI: TRACe:IQ:SRATe \n
		Snippet: driver.applications.k91Wlan.trace.iq.symbolRate.set(sample_rate = 1.0) \n
		This command sets the final user sample rate for the acquired I/Q data. Thus, the user sample rate can be modified
		without affecting the actual data capturing settings on the R&S FSW. \n
			:param sample_rate: The valid sample rates are described in 'Sample rate and maximum usable I/Q bandwidth for RF input'. Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'TRACe:IQ:SRATe {param}')

	def get(self) -> float:
		"""SCPI: TRACe:IQ:SRATe \n
		Snippet: value: float = driver.applications.k91Wlan.trace.iq.symbolRate.get() \n
		This command sets the final user sample rate for the acquired I/Q data. Thus, the user sample rate can be modified
		without affecting the actual data capturing settings on the R&S FSW. \n
			:return: sample_rate: The valid sample rates are described in 'Sample rate and maximum usable I/Q bandwidth for RF input'. Unit: HZ"""
		response = self._core.io.query_str(f'TRACe:IQ:SRATe?')
		return Conversions.str_to_float(response)
