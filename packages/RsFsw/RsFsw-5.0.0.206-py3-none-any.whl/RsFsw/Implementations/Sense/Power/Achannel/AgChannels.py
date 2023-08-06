from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AgChannels:
	"""AgChannels commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("agChannels", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:AGCHannels \n
		Snippet: driver.sense.power.achannel.agChannels.set(state = False) \n
		This command activates or deactivates gap channels in an MSR signal. For more information see 'Measurement on
		multi-standard radio (MSR) signals'. \n
			:param state: ON | OFF | 1 | 0 ON | 1 The gap channels are displayed and channel power results are calculated and displayed in the Result Summary. OFF | 0 The gap channels are not displayed in the diagram and channel power results are not calculated nor displayed in the Result Summary.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:ACHannel:AGCHannels {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:ACHannel:AGCHannels \n
		Snippet: value: bool = driver.sense.power.achannel.agChannels.get() \n
		This command activates or deactivates gap channels in an MSR signal. For more information see 'Measurement on
		multi-standard radio (MSR) signals'. \n
			:return: state: ON | OFF | 1 | 0 ON | 1 The gap channels are displayed and channel power results are calculated and displayed in the Result Summary. OFF | 0 The gap channels are not displayed in the diagram and channel power results are not calculated nor displayed in the Result Summary."""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:AGCHannels?')
		return Conversions.str_to_bool(response)
