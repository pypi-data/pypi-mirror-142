from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:REFSignal:CGW:AMODe[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.cgw.amode.state.set(state = False) \n
		Sets and queries the 'Force ARB Mode' setting. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:REFSignal:CGW:AMODe:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:REFSignal:CGW:AMODe[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.refSignal.cgw.amode.state.get() \n
		Sets and queries the 'Force ARB Mode' setting. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:CGW:AMODe:STATe?')
		return Conversions.str_to_bool(response)
