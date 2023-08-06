from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:GENerator:CONNection[:STATe] \n
		Snippet: driver.configure.generator.connection.state.set(state = False) \n
		Connects or disconnects the signal generator specified by method RsFsw.Configure.Generator.IpConnection.Address.set. The
		IP address must be specified before you use this command. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Disconnects the generator. ON | 1 Connects the generator.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:GENerator:CONNection:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:GENerator:CONNection[:STATe] \n
		Snippet: value: bool = driver.configure.generator.connection.state.get() \n
		Connects or disconnects the signal generator specified by method RsFsw.Configure.Generator.IpConnection.Address.set. The
		IP address must be specified before you use this command. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Disconnects the generator. ON | 1 Connects the generator."""
		response = self._core.io.query_str(f'CONFigure:GENerator:CONNection:STATe?')
		return Conversions.str_to_bool(response)
