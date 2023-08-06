from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ports:
	"""Ports commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ports", core, parent)

	def set(self, port_type: int) -> None:
		"""SCPI: [SENSe]:MIXer:PORTs \n
		Snippet: driver.applications.k14Xnr5G.sense.mixer.ports.set(port_type = 1) \n
		No command help available \n
			:param port_type: No help available
		"""
		param = Conversions.decimal_value_to_str(port_type)
		self._core.io.write(f'SENSe:MIXer:PORTs {param}')

	def get(self) -> int:
		"""SCPI: [SENSe]:MIXer:PORTs \n
		Snippet: value: int = driver.applications.k14Xnr5G.sense.mixer.ports.get() \n
		No command help available \n
			:return: port_type: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:PORTs?')
		return Conversions.str_to_int(response)
