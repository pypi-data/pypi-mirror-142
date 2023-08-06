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
		Snippet: driver.applications.k9X11Ad.trace.iq.symbolRate.set(sample_rate = 1.0) \n
		No command help available \n
			:param sample_rate: For standard IEEE 802.11ad signals, a sample rate of 2.64 GHz is used (requires an optional bandwidth extension with at least 2 GHz) . The valid sample rates are described in 'Sample Rate and Maximum Usable I/Q Bandwidth for RF Input'. Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'TRACe:IQ:SRATe {param}')

	def get(self) -> float:
		"""SCPI: TRACe:IQ:SRATe \n
		Snippet: value: float = driver.applications.k9X11Ad.trace.iq.symbolRate.get() \n
		No command help available \n
			:return: sample_rate: For standard IEEE 802.11ad signals, a sample rate of 2.64 GHz is used (requires an optional bandwidth extension with at least 2 GHz) . The valid sample rates are described in 'Sample Rate and Maximum Usable I/Q Bandwidth for RF Input'. Unit: HZ"""
		response = self._core.io.query_str(f'TRACe:IQ:SRATe?')
		return Conversions.str_to_float(response)
