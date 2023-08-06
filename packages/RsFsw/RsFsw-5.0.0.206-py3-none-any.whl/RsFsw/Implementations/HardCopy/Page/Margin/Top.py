from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Top:
	"""Top commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("top", core, parent)

	def set(self, top: float) -> None:
		"""SCPI: HCOPy:PAGE:MARGin:TOP \n
		Snippet: driver.hardCopy.page.margin.top.set(top = 1.0) \n
		This command defines the margin at the top of the printout page on which no elements are printed. The margins are defined
		according to method RsFsw.HardCopy.Page.Margin.Unit.set. \n
			:param top: 1|2 Printing device.
		"""
		param = Conversions.decimal_value_to_str(top)
		self._core.io.write(f'HCOPy:PAGE:MARGin:TOP {param}')

	def get(self) -> float:
		"""SCPI: HCOPy:PAGE:MARGin:TOP \n
		Snippet: value: float = driver.hardCopy.page.margin.top.get() \n
		This command defines the margin at the top of the printout page on which no elements are printed. The margins are defined
		according to method RsFsw.HardCopy.Page.Margin.Unit.set. \n
			:return: top: No help available"""
		response = self._core.io.query_str(f'HCOPy:PAGE:MARGin:TOP?')
		return Conversions.str_to_float(response)
