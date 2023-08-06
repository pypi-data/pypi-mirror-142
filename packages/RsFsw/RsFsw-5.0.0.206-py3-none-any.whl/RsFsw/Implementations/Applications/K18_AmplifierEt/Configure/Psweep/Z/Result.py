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

	def set(self, result: enums.ResultItemK18, window=repcap.Window.Default) -> None:
		"""SCPI: CONFigure:PSWeep:Z<n>:RESult \n
		Snippet: driver.applications.k18AmplifierEt.configure.psweep.z.result.set(result = enums.ResultItemK18.ACB1, window = repcap.Window.Default) \n
		This command selects the result type displayed on the z-axis of the parameter sweep diagram. \n
			:param result: See table below for supported result types.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Z')
		"""
		param = Conversions.enum_scalar_to_str(result, enums.ResultItemK18)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CONFigure:PSWeep:Z{window_cmd_val}:RESult {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.ResultItemK18:
		"""SCPI: CONFigure:PSWeep:Z<n>:RESult \n
		Snippet: value: enums.ResultItemK18 = driver.applications.k18AmplifierEt.configure.psweep.z.result.get(window = repcap.Window.Default) \n
		This command selects the result type displayed on the z-axis of the parameter sweep diagram. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Z')
			:return: result: See table below for supported result types."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CONFigure:PSWeep:Z{window_cmd_val}:RESult?')
		return Conversions.str_to_scalar_enum(response, enums.ResultItemK18)
