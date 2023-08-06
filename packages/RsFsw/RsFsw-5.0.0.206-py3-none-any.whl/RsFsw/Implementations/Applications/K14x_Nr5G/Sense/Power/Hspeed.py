from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hspeed:
	"""Hspeed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hspeed", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:POWer:HSPeed \n
		Snippet: driver.applications.k14Xnr5G.sense.power.hspeed.set(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:HSPeed {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:HSPeed \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.power.hspeed.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:HSPeed?')
		return Conversions.str_to_bool(response)
