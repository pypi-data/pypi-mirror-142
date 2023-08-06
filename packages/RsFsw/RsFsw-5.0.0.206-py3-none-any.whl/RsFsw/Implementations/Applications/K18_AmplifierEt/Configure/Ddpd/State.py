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
		"""SCPI: CONFigure:DDPD[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.state.set(state = False) \n
		This command selects the type of DPD. \n
			:param state: ON | 1 Selects direct DPD. OFF | 0 Selects polynomial DPD.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:DDPD:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:DDPD[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.ddpd.state.get() \n
		This command selects the type of DPD. \n
			:return: state: ON | 1 Selects direct DPD. OFF | 0 Selects polynomial DPD."""
		response = self._core.io.query_str(f'CONFigure:DDPD:STATe?')
		return Conversions.str_to_bool(response)
