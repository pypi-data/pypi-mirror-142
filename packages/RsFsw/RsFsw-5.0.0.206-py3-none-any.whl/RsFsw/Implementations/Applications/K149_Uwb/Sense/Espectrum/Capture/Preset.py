from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preset:
	"""Preset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preset", core, parent)

	def set(self, channel_number: enums.ChannelNumber, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:CAPTure:PRESet \n
		Snippet: driver.applications.k149Uwb.sense.espectrum.capture.preset.set(channel_number = enums.ChannelNumber.C0, subBlock = repcap.SubBlock.Default) \n
		No command help available \n
			:param channel_number: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.enum_scalar_to_str(channel_number, enums.ChannelNumber)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:CAPTure:PRESet {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default) -> enums.ChannelNumber:
		"""SCPI: [SENSe]:ESPectrum<sb>:CAPTure:PRESet \n
		Snippet: value: enums.ChannelNumber = driver.applications.k149Uwb.sense.espectrum.capture.preset.get(subBlock = repcap.SubBlock.Default) \n
		No command help available \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: channel_number: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:CAPTure:PRESet?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelNumber)
