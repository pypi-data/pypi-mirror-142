from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Snumber:
	"""Snumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snumber", core, parent)

	def set(self, serial_no: str) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:SNUMber \n
		Snippet: driver.sense.correction.cvl.snumber.set(serial_no = '1') \n
		This command defines the serial number of the mixer for which the conversion loss table is to be used. This setting is
		checked against the current mixer setting before the table can be assigned to the range. Before this command can be
		performed, the conversion loss table must be selected (see [SENSe:]CORRection:CVL:SELect) . This command is only
		available with option B21 (External Mixer) installed. \n
			:param serial_no: Serial number with a maximum of 16 characters
		"""
		param = Conversions.value_to_quoted_str(serial_no)
		self._core.io.write(f'SENSe:CORRection:CVL:SNUMber {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:CORRection:CVL:SNUMber \n
		Snippet: value: str = driver.sense.correction.cvl.snumber.get() \n
		This command defines the serial number of the mixer for which the conversion loss table is to be used. This setting is
		checked against the current mixer setting before the table can be assigned to the range. Before this command can be
		performed, the conversion loss table must be selected (see [SENSe:]CORRection:CVL:SELect) . This command is only
		available with option B21 (External Mixer) installed. \n
			:return: serial_no: Serial number with a maximum of 16 characters"""
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:SNUMber?')
		return trim_str_response(response)
