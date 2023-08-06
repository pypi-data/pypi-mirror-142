from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cbwidth:
	"""Cbwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbwidth", core, parent)

	def set(self, channel_bandwidth: enums.ChannelBandwidth) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:CBWidth \n
		Snippet: driver.applications.k91Wlan.sense.power.achannel.cbwidth.set(channel_bandwidth = enums.ChannelBandwidth.BW10) \n
		This command sets the channel bandwidth to be applied for the Spectrum Emission Mask measurement. \n
			:param channel_bandwidth: BW2_5 | BW5 | BW10 | BW20 | BW40 | BW80 | BW160 | BW320 BW2_5 2.5 MHz BW5 5 MHz BW10 10 MHz BW20 20 MHz BW40 40 MHz (Requires a bandwidth extension option.) BW80 80 MHz (Requires a bandwidth extension option.) BW160 160 MHz (Requires a bandwidth extension option.)
		"""
		param = Conversions.enum_scalar_to_str(channel_bandwidth, enums.ChannelBandwidth)
		self._core.io.write(f'SENSe:POWer:ACHannel:CBWidth {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ChannelBandwidth:
		"""SCPI: [SENSe]:POWer:ACHannel:CBWidth \n
		Snippet: value: enums.ChannelBandwidth = driver.applications.k91Wlan.sense.power.achannel.cbwidth.get() \n
		This command sets the channel bandwidth to be applied for the Spectrum Emission Mask measurement. \n
			:return: channel_bandwidth: BW2_5 | BW5 | BW10 | BW20 | BW40 | BW80 | BW160 | BW320 BW2_5 2.5 MHz BW5 5 MHz BW10 10 MHz BW20 20 MHz BW40 40 MHz (Requires a bandwidth extension option.) BW80 80 MHz (Requires a bandwidth extension option.) BW160 160 MHz (Requires a bandwidth extension option.)"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:CBWidth?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelBandwidth)
