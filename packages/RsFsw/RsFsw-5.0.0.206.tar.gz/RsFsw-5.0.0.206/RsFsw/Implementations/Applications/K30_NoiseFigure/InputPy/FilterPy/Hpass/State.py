from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:FILTer:HPASs[:STATe] \n
		Snippet: driver.applications.k30NoiseFigure.inputPy.filterPy.hpass.state.set(state = False, inputIx = repcap.InputIx.Default) \n
		Activates an additional internal high-pass filter for RF input signals from 1 GHz to 3 GHz. This filter is used to remove
		the harmonics of the R&S FSW in order to measure the harmonics for a DUT, for example. This function requires an
		additional high-pass filter hardware option. (Note: for RF input signals outside the specified range, the high-pass
		filter has no effect. For signals with a frequency of approximately 4 GHz upwards, the harmonics are suppressed
		sufficiently by the YIG-preselector, if available.) \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:FILTer:HPASs:STATe {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<ip>:FILTer:HPASs[:STATe] \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.inputPy.filterPy.hpass.state.get(inputIx = repcap.InputIx.Default) \n
		Activates an additional internal high-pass filter for RF input signals from 1 GHz to 3 GHz. This filter is used to remove
		the harmonics of the R&S FSW in order to measure the harmonics for a DUT, for example. This function requires an
		additional high-pass filter hardware option. (Note: for RF input signals outside the specified range, the high-pass
		filter has no effect. For signals with a frequency of approximately 4 GHz upwards, the harmonics are suppressed
		sufficiently by the YIG-preselector, if available.) \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:FILTer:HPASs:STATe?')
		return Conversions.str_to_bool(response)
