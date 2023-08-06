from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Color:
	"""Color commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("color", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: HCOPy:DEVice:COLor \n
		Snippet: driver.hardCopy.device.color.set(state = False) \n
		This command turns color printing on and off. \n
			:param state: ON | OFF | 0 | 1 ON | 1 Color printing OFF | 0 Black and white printing
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'HCOPy:DEVice:COLor {param}')

	def get(self) -> bool:
		"""SCPI: HCOPy:DEVice:COLor \n
		Snippet: value: bool = driver.hardCopy.device.color.get() \n
		This command turns color printing on and off. \n
			:return: state: ON | OFF | 0 | 1 ON | 1 Color printing OFF | 0 Black and white printing"""
		response = self._core.io.query_str(f'HCOPy:DEVice:COLor?')
		return Conversions.str_to_bool(response)
