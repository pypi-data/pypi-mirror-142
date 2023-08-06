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
		"""SCPI: CONFigure:FRSPan:AUTO \n
		Snippet: driver.applications.k18AmplifierEt.configure.frSpan.auto.set(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:FRSPan:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:FRSPan:AUTO \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.frSpan.auto.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'CONFigure:FRSPan:AUTO?')
		return Conversions.str_to_bool(response)
