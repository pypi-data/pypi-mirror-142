from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Track:
	"""Track commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("track", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:FREQuency:TRACk \n
		Snippet: driver.applications.k40PhaseNoise.sense.frequency.track.set(state = False) \n
		This command turns frequency tracking on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:FREQuency:TRACk {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:FREQuency:TRACk \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.sense.frequency.track.get() \n
		This command turns frequency tracking on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:FREQuency:TRACk?')
		return Conversions.str_to_bool(response)
