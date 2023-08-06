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

	def set(self, channel: enums.AdjChannel) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:AACHannel \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.aaChannel.set(channel = enums.AdjChannel.E500) \n
		This command selects the bandwidth of the adjacent channel for ACLR measurements. \n
			:param channel: E500 Selects an WCDMA signal with 3.84 MHz bandwidth as assumed adjacent channel carrier. NOSBw Selects an 5G NR signal as assumed adjacent channel carrier.
		"""
		param = Conversions.enum_scalar_to_str(channel, enums.AdjChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:AACHannel {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AdjChannel:
		"""SCPI: [SENSe]:POWer:ACHannel:AACHannel \n
		Snippet: value: enums.AdjChannel = driver.applications.k14Xnr5G.sense.power.achannel.aaChannel.get() \n
		This command selects the bandwidth of the adjacent channel for ACLR measurements. \n
			:return: channel: E500 Selects an WCDMA signal with 3.84 MHz bandwidth as assumed adjacent channel carrier. NOSBw Selects an 5G NR signal as assumed adjacent channel carrier."""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:AACHannel?')
		return Conversions.str_to_scalar_enum(response, enums.AdjChannel)
