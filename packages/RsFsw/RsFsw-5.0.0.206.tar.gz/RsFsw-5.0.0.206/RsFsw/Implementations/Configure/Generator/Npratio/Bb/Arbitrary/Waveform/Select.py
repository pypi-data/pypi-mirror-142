from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def get(self) -> str:
		"""SCPI: CONFigure:GENerator:NPRatio:BB:ARBitrary:WAVeform:SELect \n
		Snippet: value: str = driver.configure.generator.npratio.bb.arbitrary.waveform.select.get() \n
		Queries the ARB waveform file currently used by the signal generator. \n
			:return: arb_waveform: No help available"""
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:BB:ARBitrary:WAVeform:SELect?')
		return trim_str_response(response)
