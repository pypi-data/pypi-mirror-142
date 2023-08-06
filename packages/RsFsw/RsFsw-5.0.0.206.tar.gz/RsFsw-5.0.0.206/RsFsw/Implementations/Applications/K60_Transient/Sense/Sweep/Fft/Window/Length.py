from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:FFT:WINDow:LENGth \n
		Snippet: value: float = driver.applications.k60Transient.sense.sweep.fft.window.length.get() \n
		No command help available \n
			:return: window_length: 32 | 64 | 128 | 256 | 512 | 1024 | 2048 | 4096"""
		response = self._core.io.query_str(f'SENSe:SWEep:FFT:WINDow:LENGth?')
		return Conversions.str_to_float(response)
