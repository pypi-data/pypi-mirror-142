from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bottom:
	"""Bottom commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bottom", core, parent)

	def set(self, bottom: float) -> None:
		"""SCPI: HCOPy:PAGE:MARGin:BOTTom \n
		Snippet: driver.hardCopy.page.margin.bottom.set(bottom = 1.0) \n
		This command defines the margin at the bottom of the printout page on which no elements are printed. The margins are
		defined according to method RsFsw.HardCopy.Page.Margin.Unit.set. \n
			:param bottom: 1|2 Printing device.
		"""
		param = Conversions.decimal_value_to_str(bottom)
		self._core.io.write(f'HCOPy:PAGE:MARGin:BOTTom {param}')

	def get(self) -> float:
		"""SCPI: HCOPy:PAGE:MARGin:BOTTom \n
		Snippet: value: float = driver.hardCopy.page.margin.bottom.get() \n
		This command defines the margin at the bottom of the printout page on which no elements are printed. The margins are
		defined according to method RsFsw.HardCopy.Page.Margin.Unit.set. \n
			:return: bottom: No help available"""
		response = self._core.io.query_str(f'HCOPy:PAGE:MARGin:BOTTom?')
		return Conversions.str_to_float(response)
