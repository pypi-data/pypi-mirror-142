from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:SINFo:SRATe \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.sinfo.symbolRate.get() \n
		This command queries the sample rate of the currently used reference signal. \n
			:return: sample_rate: numeric value Unit: Hz"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:SINFo:SRATe?')
		return Conversions.str_to_float(response)
