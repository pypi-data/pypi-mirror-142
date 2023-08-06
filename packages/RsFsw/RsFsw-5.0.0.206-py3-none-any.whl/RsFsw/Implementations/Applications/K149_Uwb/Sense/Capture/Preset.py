from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preset:
	"""Preset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preset", core, parent)

	def set(self, channel_number: enums.ChannelNumber) -> None:
		"""SCPI: [SENSe]:CAPTure:PRESet \n
		Snippet: driver.applications.k149Uwb.sense.capture.preset.set(channel_number = enums.ChannelNumber.C0) \n
		Selects the HRP UWB Channel. \n
			:param channel_number: C0 | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | C13 | C14 | C15
		"""
		param = Conversions.enum_scalar_to_str(channel_number, enums.ChannelNumber)
		self._core.io.write(f'SENSe:CAPTure:PRESet {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ChannelNumber:
		"""SCPI: [SENSe]:CAPTure:PRESet \n
		Snippet: value: enums.ChannelNumber = driver.applications.k149Uwb.sense.capture.preset.get() \n
		Selects the HRP UWB Channel. \n
			:return: channel_number: C0 | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | C13 | C14 | C15"""
		response = self._core.io.query_str(f'SENSe:CAPTure:PRESet?')
		return Conversions.str_to_scalar_enum(response, enums.ChannelNumber)
