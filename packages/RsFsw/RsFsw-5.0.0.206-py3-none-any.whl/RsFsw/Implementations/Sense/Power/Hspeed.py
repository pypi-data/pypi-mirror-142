from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hspeed:
	"""Hspeed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hspeed", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:POWer:HSPeed \n
		Snippet: driver.sense.power.hspeed.set(state = False) \n
		This command turns high speed ACLR and channel power measurements on and off. If on, the R&S FSW performs a measurement
		on each channel in the time domain. It returns to the frequency domain when the measurement is done.
		In some telecommunications standards, high speed measurements use weighting filters with characteristic or steep-edged
		channel filters for band limitation. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:HSPeed {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:HSPeed \n
		Snippet: value: bool = driver.sense.power.hspeed.get() \n
		This command turns high speed ACLR and channel power measurements on and off. If on, the R&S FSW performs a measurement
		on each channel in the time domain. It returns to the frequency domain when the measurement is done.
		In some telecommunications standards, high speed measurements use weighting filters with characteristic or steep-edged
		channel filters for band limitation. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:POWer:HSPeed?')
		return Conversions.str_to_bool(response)
