from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mixer:
	"""Mixer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mixer", core, parent)

	def set(self, comment: str) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:MIXer \n
		Snippet: driver.applications.k6Pulse.sense.correction.cvl.mixer.set(comment = '1') \n
		This command defines the mixer name in the conversion loss table. This setting is checked against the current mixer
		setting before the table can be assigned to the range. Before this command can be performed, the conversion loss table
		must be selected (see [SENSe:]CORRection:CVL:SELect) . This command is only available with option B21 (External Mixer)
		installed. \n
			:param comment: string Name of mixer with a maximum of 16 characters
		"""
		param = Conversions.value_to_quoted_str(comment)
		self._core.io.write(f'SENSe:CORRection:CVL:MIXer {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:CORRection:CVL:MIXer \n
		Snippet: value: str = driver.applications.k6Pulse.sense.correction.cvl.mixer.get() \n
		This command defines the mixer name in the conversion loss table. This setting is checked against the current mixer
		setting before the table can be assigned to the range. Before this command can be performed, the conversion loss table
		must be selected (see [SENSe:]CORRection:CVL:SELect) . This command is only available with option B21 (External Mixer)
		installed. \n
			:return: comment: No help available"""
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:MIXer?')
		return trim_str_response(response)
