from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:ADEMod:MTIMe:AUTO \n
		Snippet: driver.applications.k17Mcgd.sense.ademod.mtime.auto.set(state = False) \n
		This command enables or disables automatic measurement time selection. Note that this command is maintained for
		compatibility reasons only. Use [SENSe:]MTIMe:AUTO for new remote control programs. \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:ADEMod:MTIMe:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:ADEMod:MTIMe:AUTO \n
		Snippet: value: bool = driver.applications.k17Mcgd.sense.ademod.mtime.auto.get() \n
		This command enables or disables automatic measurement time selection. Note that this command is maintained for
		compatibility reasons only. Use [SENSe:]MTIMe:AUTO for new remote control programs. \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:ADEMod:MTIMe:AUTO?')
		return Conversions.str_to_bool(response)
