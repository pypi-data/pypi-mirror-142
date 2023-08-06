from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AaChannel:
	"""AaChannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aaChannel", core, parent)

	def set(self, channel: enums.AdjChannelBw) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:AACHannel \n
		Snippet: driver.applications.k10Xlte.sense.power.achannel.aaChannel.set(channel = enums.AdjChannelBw.EUTRa) \n
		This command selects the bandwidth of the adjacent channel for ACLR measurements. For MC ACLR measurements, the command
		selects the bandwidth of the lower adjacent channel. \n
			:param channel: EUTRA Selects an EUTRA signal of the same bandwidth like the TX channel as assumed adjacent channel carrier. UTRA128 Selects an UTRA signal with a bandwidth of 1.28MHz as assumed adjacent channel carrier. UTRA384 Selects an UTRA signal with a bandwidth of 3.84MHz as assumed adjacent channel carrier. UTRA768 Selects an UTRA signal with a bandwidth of 7.68MHz as assumed adjacent channel carrier.
		"""
		param = Conversions.enum_scalar_to_str(channel, enums.AdjChannelBw)
		self._core.io.write(f'SENSe:POWer:ACHannel:AACHannel {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AdjChannelBw:
		"""SCPI: [SENSe]:POWer:ACHannel:AACHannel \n
		Snippet: value: enums.AdjChannelBw = driver.applications.k10Xlte.sense.power.achannel.aaChannel.get() \n
		This command selects the bandwidth of the adjacent channel for ACLR measurements. For MC ACLR measurements, the command
		selects the bandwidth of the lower adjacent channel. \n
			:return: channel: EUTRA Selects an EUTRA signal of the same bandwidth like the TX channel as assumed adjacent channel carrier. UTRA128 Selects an UTRA signal with a bandwidth of 1.28MHz as assumed adjacent channel carrier. UTRA384 Selects an UTRA signal with a bandwidth of 3.84MHz as assumed adjacent channel carrier. UTRA768 Selects an UTRA signal with a bandwidth of 7.68MHz as assumed adjacent channel carrier."""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:AACHannel?')
		return Conversions.str_to_scalar_enum(response, enums.AdjChannelBw)
