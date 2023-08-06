from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:MDPD[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.mdpd.state.set(state = False) \n
		Switches the memory polynomial state on and off. \n
			:param state: ON | 1 OFF | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:MDPD:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:MDPD[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.mdpd.state.get() \n
		Switches the memory polynomial state on and off. \n
			:return: state: ON | 1 OFF | 0"""
		response = self._core.io.query_str(f'CONFigure:MDPD:STATe?')
		return Conversions.str_to_bool(response)
