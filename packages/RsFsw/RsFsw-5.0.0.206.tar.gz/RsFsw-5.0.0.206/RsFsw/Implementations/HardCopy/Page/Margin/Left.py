from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Left:
	"""Left commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("left", core, parent)

	def set(self, left: float) -> None:
		"""SCPI: HCOPy:PAGE:MARGin:LEFT \n
		Snippet: driver.hardCopy.page.margin.left.set(left = 1.0) \n
		This command defines the margin at the left side of the printout page on which no elements are printed. The margins are
		defined according to method RsFsw.HardCopy.Page.Margin.Unit.set. \n
			:param left: 1|2 Printing device.
		"""
		param = Conversions.decimal_value_to_str(left)
		self._core.io.write(f'HCOPy:PAGE:MARGin:LEFT {param}')

	def get(self) -> float:
		"""SCPI: HCOPy:PAGE:MARGin:LEFT \n
		Snippet: value: float = driver.hardCopy.page.margin.left.get() \n
		This command defines the margin at the left side of the printout page on which no elements are printed. The margins are
		defined according to method RsFsw.HardCopy.Page.Margin.Unit.set. \n
			:return: left: No help available"""
		response = self._core.io.query_str(f'HCOPy:PAGE:MARGin:LEFT?')
		return Conversions.str_to_float(response)
