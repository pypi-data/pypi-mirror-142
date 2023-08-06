from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Suppress:
	"""Suppress commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("suppress", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:SPURs:SUPPress \n
		Snippet: driver.applications.k40PhaseNoise.sense.spurs.suppress.set(state = False) \n
		This command turns spur removal for all traces and windows on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SPURs:SUPPress {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SPURs:SUPPress \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.sense.spurs.suppress.get() \n
		This command turns spur removal for all traces and windows on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:SPURs:SUPPress?')
		return Conversions.str_to_bool(response)
