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
		"""SCPI: CONFigure:CFReduction:SBANdwidth:AUTO \n
		Snippet: driver.applications.k18AmplifierEt.configure.cfReduction.sbandwidth.auto.set(state = False) \n
		Sets and queries the signal bandwidth mode. \n
			:param state: 0 | 1 | OFF | ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:CFReduction:SBANdwidth:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:CFReduction:SBANdwidth:AUTO \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.cfReduction.sbandwidth.auto.get() \n
		Sets and queries the signal bandwidth mode. \n
			:return: state: 0 | 1 | OFF | ON"""
		response = self._core.io.query_str(f'CONFigure:CFReduction:SBANdwidth:AUTO?')
		return Conversions.str_to_bool(response)
