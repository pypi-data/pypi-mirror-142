from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Default:
	"""Default commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("default", core, parent)

	def set(self, default_values: bool) -> None:
		"""SCPI: [SENSe]:CAPTure:DEFault \n
		Snippet: driver.applications.k149Uwb.sense.capture.default.set(default_values = False) \n
		Toggles the default values between on/off. \n
			:param default_values: ON | OFF
		"""
		param = Conversions.bool_to_str(default_values)
		self._core.io.write(f'SENSe:CAPTure:DEFault {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:CAPTure:DEFault \n
		Snippet: value: bool = driver.applications.k149Uwb.sense.capture.default.get() \n
		Toggles the default values between on/off. \n
			:return: default_values: ON | OFF"""
		response = self._core.io.query_str(f'SENSe:CAPTure:DEFault?')
		return Conversions.str_to_bool(response)
