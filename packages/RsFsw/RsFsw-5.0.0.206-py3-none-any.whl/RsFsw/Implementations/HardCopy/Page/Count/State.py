from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: HCOPy:PAGE:COUNt:STATe \n
		Snippet: driver.hardCopy.page.count.state.set(state = False) \n
		This command includes or excludes the page number for printouts consisting of multiple pages (method RsFsw.HardCopy.
		Content.set) . \n
			:param state: 1 | 0 | ON | OFF 1 | ON The page number is printed. 0 | OFF The page number is not printed.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'HCOPy:PAGE:COUNt:STATe {param}')

	def get(self) -> bool:
		"""SCPI: HCOPy:PAGE:COUNt:STATe \n
		Snippet: value: bool = driver.hardCopy.page.count.state.get() \n
		This command includes or excludes the page number for printouts consisting of multiple pages (method RsFsw.HardCopy.
		Content.set) . \n
			:return: state: 1 | 0 | ON | OFF 1 | ON The page number is printed. 0 | OFF The page number is not printed."""
		response = self._core.io.query_str(f'HCOPy:PAGE:COUNt:STATe?')
		return Conversions.str_to_bool(response)
