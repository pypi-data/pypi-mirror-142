from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: MMEMory:LOAD:IQ:STReam:AUTO \n
		Snippet: driver.applications.k10Xlte.massMemory.load.iq.stream.auto.set(state = False) \n
		Only available for files that contain more than one data stream from multiple channels: automatically defines which data
		stream in the file is used as input for the channel. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The data stream specified by method RsFsw.MassMemory.Load.Iq.Stream.set is used as input for the channel. ON | 1 The first data stream in the file is used as input for the channel. Applications that support multiple data streams use the first data stream in the file for the first input stream, the second for the second stream etc.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'MMEMory:LOAD:IQ:STReam:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: MMEMory:LOAD:IQ:STReam:AUTO \n
		Snippet: value: bool = driver.applications.k10Xlte.massMemory.load.iq.stream.auto.get() \n
		Only available for files that contain more than one data stream from multiple channels: automatically defines which data
		stream in the file is used as input for the channel. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The data stream specified by method RsFsw.MassMemory.Load.Iq.Stream.set is used as input for the channel. ON | 1 The first data stream in the file is used as input for the channel. Applications that support multiple data streams use the first data stream in the file for the first input stream, the second for the second stream etc."""
		response = self._core.io.query_str(f'MMEMory:LOAD:IQ:STReam:AUTO?')
		return Conversions.str_to_bool(response)
