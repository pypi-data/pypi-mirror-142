from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, sample_rate: float) -> None:
		"""SCPI: CONFigure:REFSignal:GOS:SRATe \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.gos.symbolRate.set(sample_rate = 1.0) \n
		This command defines the clock (or sample) rate of the internally generated reference signal. \n
			:param sample_rate: numeric value Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'CONFigure:REFSignal:GOS:SRATe {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:GOS:SRATe \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.gos.symbolRate.get() \n
		This command defines the clock (or sample) rate of the internally generated reference signal. \n
			:return: sample_rate: numeric value Unit: Hz"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:GOS:SRATe?')
		return Conversions.str_to_float(response)
