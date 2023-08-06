from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset: float) -> None:
		"""SCPI: [SENSe]:RTMS:CAPTure:OFFSet \n
		Snippet: driver.applications.k70Vsa.sense.rtms.capture.offset.set(offset = 1.0) \n
		This setting is only available for secondary applications in MSRT mode, not for the MSRT primary. It has a similar effect
		as the trigger offset in other measurements. \n
			:param offset: This parameter defines the time offset between the capture buffer start and the start of the extracted secondary application data. The offset must be a positive value, as the secondary application can only analyze data that is contained in the capture buffer. Range: - [pretrigger time] to min (posttrigger time; sweep time) , Unit: S
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SENSe:RTMS:CAPTure:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:RTMS:CAPTure:OFFSet \n
		Snippet: value: float = driver.applications.k70Vsa.sense.rtms.capture.offset.get() \n
		This setting is only available for secondary applications in MSRT mode, not for the MSRT primary. It has a similar effect
		as the trigger offset in other measurements. \n
			:return: offset: This parameter defines the time offset between the capture buffer start and the start of the extracted secondary application data. The offset must be a positive value, as the secondary application can only analyze data that is contained in the capture buffer. Range: - [pretrigger time] to min (posttrigger time; sweep time) , Unit: S"""
		response = self._core.io.query_str(f'SENSe:RTMS:CAPTure:OFFSet?')
		return Conversions.str_to_float(response)
