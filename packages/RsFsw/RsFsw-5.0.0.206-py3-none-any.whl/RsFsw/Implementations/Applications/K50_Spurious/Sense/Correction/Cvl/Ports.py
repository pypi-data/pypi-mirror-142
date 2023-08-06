from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ports:
	"""Ports commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ports", core, parent)

	def set(self, port: float) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:PORTs \n
		Snippet: driver.applications.k50Spurious.sense.correction.cvl.ports.set(port = 1.0) \n
		This command defines the mixer type in the conversion loss table. This setting is checked against the current mixer
		setting before the table can be assigned to the range. Before this command can be performed, the conversion loss table
		must be selected (see [SENSe:]CORRection:CVL:SELect) . This command is only available with option B21 (External Mixer)
		installed. \n
			:param port: 2 | 3
		"""
		param = Conversions.decimal_value_to_str(port)
		self._core.io.write(f'SENSe:CORRection:CVL:PORTs {param}')

	def get(self, port: float) -> float:
		"""SCPI: [SENSe]:CORRection:CVL:PORTs \n
		Snippet: value: float = driver.applications.k50Spurious.sense.correction.cvl.ports.get(port = 1.0) \n
		This command defines the mixer type in the conversion loss table. This setting is checked against the current mixer
		setting before the table can be assigned to the range. Before this command can be performed, the conversion loss table
		must be selected (see [SENSe:]CORRection:CVL:SELect) . This command is only available with option B21 (External Mixer)
		installed. \n
			:param port: 2 | 3
			:return: port: No help available"""
		param = Conversions.decimal_value_to_str(port)
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:PORTs? {param}')
		return Conversions.str_to_float(response)
