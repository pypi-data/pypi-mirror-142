from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UaaChannel:
	"""UaaChannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uaaChannel", core, parent)

	def set(self, bandwidth: enums.AdjChannelBw) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:UAAChannel \n
		Snippet: driver.applications.k10Xlte.sense.power.achannel.uaaChannel.set(bandwidth = enums.AdjChannelBw.EUTRa) \n
		For MC ACLR measurements, the command selects the bandwidth of the upper adjacent channel. \n
			:param bandwidth: EUTRA Selects an EUTRA signal of the same bandwidth like the TX channel as assumed adjacent channel carrier. UTRA128 Selects an UTRA signal with a bandwidth of 1.28MHz as assumed adjacent channel carrier. UTRA384 Selects an UTRA signal with a bandwidth of 3.84MHz as assumed adjacent channel carrier. UTRA768 Selects an UTRA signal with a bandwidth of 7.68MHz as assumed adjacent channel carrier.
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.AdjChannelBw)
		self._core.io.write(f'SENSe:POWer:ACHannel:UAAChannel {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AdjChannelBw:
		"""SCPI: [SENSe]:POWer:ACHannel:UAAChannel \n
		Snippet: value: enums.AdjChannelBw = driver.applications.k10Xlte.sense.power.achannel.uaaChannel.get() \n
		For MC ACLR measurements, the command selects the bandwidth of the upper adjacent channel. \n
			:return: bandwidth: EUTRA Selects an EUTRA signal of the same bandwidth like the TX channel as assumed adjacent channel carrier. UTRA128 Selects an UTRA signal with a bandwidth of 1.28MHz as assumed adjacent channel carrier. UTRA384 Selects an UTRA signal with a bandwidth of 3.84MHz as assumed adjacent channel carrier. UTRA768 Selects an UTRA signal with a bandwidth of 7.68MHz as assumed adjacent channel carrier."""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:UAAChannel?')
		return Conversions.str_to_scalar_enum(response, enums.AdjChannelBw)
