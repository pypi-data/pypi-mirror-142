from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Osync:
	"""Osync commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("osync", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:ROSCillator:OSYNc \n
		Snippet: driver.sense.roscillator.osync.set(state = False) \n
		If enabled, a 100 MHz reference signal is provided to the 'SYNC TRIGGER OUTPUT' connector. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:ROSCillator:OSYNc {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:ROSCillator:OSYNc \n
		Snippet: value: bool = driver.sense.roscillator.osync.get() \n
		If enabled, a 100 MHz reference signal is provided to the 'SYNC TRIGGER OUTPUT' connector. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:ROSCillator:OSYNc?')
		return Conversions.str_to_bool(response)
