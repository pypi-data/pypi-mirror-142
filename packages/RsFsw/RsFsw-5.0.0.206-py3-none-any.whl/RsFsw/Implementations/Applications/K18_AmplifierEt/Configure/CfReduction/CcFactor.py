from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcFactor:
	"""CcFactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccFactor", core, parent)

	def get(self) -> float:
		"""SCPI: CONFigure:CFReduction:CCFactor \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.cfReduction.ccFactor.get() \n
		Queries the crest factor of the waveform after the calculation of the resulting crest factor is completed. \n
			:return: ccf: No help available"""
		response = self._core.io.query_str(f'CONFigure:CFReduction:CCFactor?')
		return Conversions.str_to_float(response)
