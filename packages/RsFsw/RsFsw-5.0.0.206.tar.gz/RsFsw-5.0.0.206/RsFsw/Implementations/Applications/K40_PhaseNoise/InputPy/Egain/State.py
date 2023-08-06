from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, arg_0: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<1|2>:EGAin[:STATe] \n
		Snippet: driver.applications.k40PhaseNoise.inputPy.egain.state.set(arg_0 = False, inputIx = repcap.InputIx.Default) \n
		Before this command can be used, the external preamplifier must be connected to the R&S FSW. See the preamplifier's
		documentation for details. When activated, the R&S FSW automatically compensates the magnitude and phase characteristics
		of the external preamplifier in the measurement results. Note that when an optional external preamplifier is activated,
		the internal preamplifier is automatically disabled, and vice versa. For R&S FSW85 models with two RF inputs, you must
		enable correction from the external preamplifier for each input individually. Correction cannot be enabled for both
		inputs at the same time. When deactivated, no compensation is performed even if an external preamplifier remains
		connected. \n
			:param arg_0: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(arg_0)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:EGAin:STATe {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<1|2>:EGAin[:STATe] \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.inputPy.egain.state.get(inputIx = repcap.InputIx.Default) \n
		Before this command can be used, the external preamplifier must be connected to the R&S FSW. See the preamplifier's
		documentation for details. When activated, the R&S FSW automatically compensates the magnitude and phase characteristics
		of the external preamplifier in the measurement results. Note that when an optional external preamplifier is activated,
		the internal preamplifier is automatically disabled, and vice versa. For R&S FSW85 models with two RF inputs, you must
		enable correction from the external preamplifier for each input individually. Correction cannot be enabled for both
		inputs at the same time. When deactivated, no compensation is performed even if an external preamplifier remains
		connected. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: arg_0: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:EGAin:STATe?')
		return Conversions.str_to_bool(response)
