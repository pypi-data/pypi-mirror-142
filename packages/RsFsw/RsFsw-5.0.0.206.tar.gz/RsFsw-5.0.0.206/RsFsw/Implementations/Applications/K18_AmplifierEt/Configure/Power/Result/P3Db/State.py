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
		"""SCPI: CONFigure:POWer:RESult:P3DB[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.power.result.p3Db.state.set(state = False) \n
		This command turns automatic calculation of the reference point required to determine the compression points (1 dB, 2 dB
		and 3 dB) on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:POWer:RESult:P3DB:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:POWer:RESult:P3DB[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.power.result.p3Db.state.get() \n
		This command turns automatic calculation of the reference point required to determine the compression points (1 dB, 2 dB
		and 3 dB) on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:POWer:RESult:P3DB:STATe?')
		return Conversions.str_to_bool(response)
