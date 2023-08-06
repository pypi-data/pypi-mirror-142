from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mtable:
	"""Mtable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mtable", core, parent)

	def set(self, display_mode: enums.AutoMode) -> None:
		"""SCPI: DISPlay:MTABle \n
		Snippet: driver.applications.k60Transient.display.mtable.set(display_mode = enums.AutoMode.AUTO) \n
		No command help available \n
			:param display_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(display_mode, enums.AutoMode)
		self._core.io.write(f'DISPlay:MTABle {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoMode:
		"""SCPI: DISPlay:MTABle \n
		Snippet: value: enums.AutoMode = driver.applications.k60Transient.display.mtable.get() \n
		No command help available \n
			:return: display_mode: No help available"""
		response = self._core.io.query_str(f'DISPlay:MTABle?')
		return Conversions.str_to_scalar_enum(response, enums.AutoMode)
