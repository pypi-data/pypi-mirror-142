from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ports:
	"""Ports commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ports", core, parent)

	def set(self, arg_0: int) -> None:
		"""SCPI: [SENSe]:MIXer:PORTs \n
		Snippet: driver.applications.k18AmplifierEt.sense.mixer.ports.set(arg_0 = 1) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'SENSe:MIXer:PORTs {param}')

	def get(self) -> int:
		"""SCPI: [SENSe]:MIXer:PORTs \n
		Snippet: value: int = driver.applications.k18AmplifierEt.sense.mixer.ports.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:PORTs?')
		return Conversions.str_to_int(response)
