from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self, result_type: enums.ResultTypeA, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:NPRatio:RESult \n
		Snippet: value: float = driver.calculate.npratio.result.get(result_type = enums.ResultTypeA.ALL, window = repcap.Window.Default) \n
		Queries the power results of the noise power ratio measurement. \n
			:param result_type: CPOWer | NPOWer | NPRatio | ALL CPOWer Returns the total measured power divided by the channel bandwidth (without notches) or integration bandwidth (with notches) in dBm/Hz NPOWer Returns the power measured in each notch divided by the notch bandwidth in dBm/Hz NPRatio Returns the ratio of the total channel power density divided by the notch power density for each notch in dB ALL Returns all power results for the channel and n defined notches in the following order: ChannelPowerDens,NotchPowerDens1,..,NotchPowerDensn,NPR1,..,NPRn
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: result_type_result: No help available"""
		param = Conversions.enum_scalar_to_str(result_type, enums.ResultTypeA)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:NPRatio:RESult? {param}')
		return Conversions.str_to_float(response)
