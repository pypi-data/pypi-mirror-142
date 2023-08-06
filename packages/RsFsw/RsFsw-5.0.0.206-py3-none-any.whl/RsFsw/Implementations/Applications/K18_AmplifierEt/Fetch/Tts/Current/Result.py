from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:TTS:CURRent[:RESult] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.tts.current.result.get() \n
		This command queries the trigger to sync result. This is the time from start of capture (i.e. including pre-trigger
		samples) to the start of the sync range, which is not necessarily the beginning of the reference waveform. \n
			:return: time: numeric value Unit: s"""
		response = self._core.io.query_str(f'FETCh:TTS:CURRent:RESult?')
		return Conversions.str_to_float(response)
