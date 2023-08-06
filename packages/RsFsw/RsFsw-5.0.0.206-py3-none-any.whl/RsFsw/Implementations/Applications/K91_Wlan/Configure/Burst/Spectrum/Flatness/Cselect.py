from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cselect:
	"""Cselect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cselect", core, parent)

	def set(self, channel_type: enums.ChannelTypeResults) -> None:
		"""SCPI: CONFigure:BURSt:SPECtrum:FLATness:CSELect \n
		Snippet: driver.applications.k91Wlan.configure.burst.spectrum.flatness.cselect.set(channel_type = enums.ChannelTypeResults.EFFective) \n
		This remote control command configures the Spectrum Flatness and Group Delay results to be based on either effective or
		physical channels. This command is only valid for IEEE 802.11n and IEEE 802.11ac standards. While the physical channels
		cannot always be determined, the effective channel can always be estimated from the known training fields. Thus, for some
		PPDUs or measurement scenarios, only the results based on the mapping of the space-time stream to the Rx antenna
		(effective channel) are available, as the mapping of the Rx antennas to the Tx antennas (physical channel) could not be
		determined. For more information see 'Physical vs effective channels'. \n
			:param channel_type: EFFective | PHYSical
		"""
		param = Conversions.enum_scalar_to_str(channel_type, enums.ChannelTypeResults)
		self._core.io.write(f'CONFigure:BURSt:SPECtrum:FLATness:CSELect {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ChannelTypeResults:
		"""SCPI: CONFigure:BURSt:SPECtrum:FLATness:CSELect \n
		Snippet: value: enums.ChannelTypeResults = driver.applications.k91Wlan.configure.burst.spectrum.flatness.cselect.get() \n
		This remote control command configures the Spectrum Flatness and Group Delay results to be based on either effective or
		physical channels. This command is only valid for IEEE 802.11n and IEEE 802.11ac standards. While the physical channels
		cannot always be determined, the effective channel can always be estimated from the known training fields. Thus, for some
		PPDUs or measurement scenarios, only the results based on the mapping of the space-time stream to the Rx antenna
		(effective channel) are available, as the mapping of the Rx antennas to the Tx antennas (physical channel) could not be
		determined. For more information see 'Physical vs effective channels'. \n
			:return: channel_type: EFFective | PHYSical"""
		response = self._core.io.query_str(f'CONFigure:BURSt:SPECtrum:FLATness:CSELect?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelTypeResults)
