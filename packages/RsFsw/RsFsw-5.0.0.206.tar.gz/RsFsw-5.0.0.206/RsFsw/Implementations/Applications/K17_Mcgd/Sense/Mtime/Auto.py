from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:MTIMe:AUTO \n
		Snippet: driver.applications.k17Mcgd.sense.mtime.auto.set(state = False) \n
		This command enables or disables automatic measurement time selection. \n
			:param state: ON | 1 Enables automatic measurement time selection. OFF | 0 Measurement time is defined manually.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:MTIMe:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:MTIMe:AUTO \n
		Snippet: value: bool = driver.applications.k17Mcgd.sense.mtime.auto.get() \n
		This command enables or disables automatic measurement time selection. \n
			:return: state: ON | 1 Enables automatic measurement time selection. OFF | 0 Measurement time is defined manually."""
		response = self._core.io.query_str(f'SENSe:MTIMe:AUTO?')
		return Conversions.str_to_bool(response)
