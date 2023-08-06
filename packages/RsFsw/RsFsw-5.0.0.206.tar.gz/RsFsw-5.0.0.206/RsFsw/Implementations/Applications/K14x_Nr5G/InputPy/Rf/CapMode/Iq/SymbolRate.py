from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, sample_rate: float) -> None:
		"""SCPI: INPut:RF:CAPMode:IQ:SRATe \n
		Snippet: driver.applications.k14Xnr5G.inputPy.rf.capMode.iq.symbolRate.set(sample_rate = 1.0) \n
		No command help available \n
			:param sample_rate: No help available
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'INPut:RF:CAPMode:IQ:SRATe {param}')

	def get(self) -> float:
		"""SCPI: INPut:RF:CAPMode:IQ:SRATe \n
		Snippet: value: float = driver.applications.k14Xnr5G.inputPy.rf.capMode.iq.symbolRate.get() \n
		No command help available \n
			:return: sample_rate: No help available"""
		response = self._core.io.query_str(f'INPut:RF:CAPMode:IQ:SRATe?')
		return Conversions.str_to_float(response)
