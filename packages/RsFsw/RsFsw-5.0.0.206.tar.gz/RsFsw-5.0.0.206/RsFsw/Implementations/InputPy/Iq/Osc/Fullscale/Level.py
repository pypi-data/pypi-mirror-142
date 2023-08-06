from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, level: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:OSC:FULLscale[:LEVel] \n
		Snippet: driver.inputPy.iq.osc.fullscale.level.set(level = 1.0, inputIx = repcap.InputIx.Default) \n
		The full scale level defines the maximum power for baseband input possible without clipping the signal. For manual input,
		this setting corresponds to the setting on the oscilloscope. Thus, possible scaling values of the oscilloscope are
		allowed. \n
			:param level: Unit: V
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(level)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:OSC:FULLscale:LEVel {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<ip>:IQ:OSC:FULLscale[:LEVel] \n
		Snippet: value: float = driver.inputPy.iq.osc.fullscale.level.get(inputIx = repcap.InputIx.Default) \n
		The full scale level defines the maximum power for baseband input possible without clipping the signal. For manual input,
		this setting corresponds to the setting on the oscilloscope. Thus, possible scaling values of the oscilloscope are
		allowed. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: level: Unit: V"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:OSC:FULLscale:LEVel?')
		return Conversions.str_to_float(response)
