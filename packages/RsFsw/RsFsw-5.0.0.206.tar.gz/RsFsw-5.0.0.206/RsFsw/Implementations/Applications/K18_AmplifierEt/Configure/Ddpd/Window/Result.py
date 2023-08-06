from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def set(self, result: enums.DdpdResult, window=repcap.Window.Default) -> None:
		"""SCPI: CONFigure:DDPD:WINDow<n>:RESult \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.window.result.set(result = enums.DdpdResult.ACB1, window = repcap.Window.Default) \n
		Configures the result type of the DDPD Results result display. \n
			:param result: EVM Error Vector Magnitude ACL1 AClrLower1 ACU1 AClrUpper1 ACB1 AClrBalanced1
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.enum_scalar_to_str(result, enums.DdpdResult)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CONFigure:DDPD:WINDow{window_cmd_val}:RESult {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.DdpdResult:
		"""SCPI: CONFigure:DDPD:WINDow<n>:RESult \n
		Snippet: value: enums.DdpdResult = driver.applications.k18AmplifierEt.configure.ddpd.window.result.get(window = repcap.Window.Default) \n
		Configures the result type of the DDPD Results result display. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: result: EVM Error Vector Magnitude ACL1 AClrLower1 ACU1 AClrUpper1 ACB1 AClrBalanced1"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CONFigure:DDPD:WINDow{window_cmd_val}:RESult?')
		return Conversions.str_to_scalar_enum(response, enums.DdpdResult)
