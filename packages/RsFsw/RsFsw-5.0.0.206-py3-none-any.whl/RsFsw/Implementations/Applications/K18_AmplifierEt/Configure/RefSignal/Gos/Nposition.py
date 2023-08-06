from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nposition:
	"""Nposition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nposition", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: CONFigure:REFSignal:GOS:NPOSition \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.gos.nposition.set(frequency = 1.0) \n
		This command defines the offset of a notch relative to the center frequency in the internally generated reference signal. \n
			:param frequency: numeric value Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:REFSignal:GOS:NPOSition {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:GOS:NPOSition \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.gos.nposition.get() \n
		This command defines the offset of a notch relative to the center frequency in the internally generated reference signal. \n
			:return: frequency: numeric value Unit: Hz"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:GOS:NPOSition?')
		return Conversions.str_to_float(response)
