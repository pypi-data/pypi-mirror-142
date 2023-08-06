from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FcOffset:
	"""FcOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fcOffset", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure[:NR5G]:FCOFfset \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.fcOffset.set(state = False) \n
		This command turns a fixed frequency offset for component carriers on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:NR5G:FCOFfset {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure[:NR5G]:FCOFfset \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.nr5G.fcOffset.get() \n
		This command turns a fixed frequency offset for component carriers on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:NR5G:FCOFfset?')
		return Conversions.str_to_bool(response)
