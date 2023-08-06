from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Protection:
	"""Protection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("protection", core, parent)

	def reset(self, device_name: str = None, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:ATTenuation:PROTection:RESet \n
		Snippet: driver.inputPy.attenuation.protection.reset(device_name = '1', inputIx = repcap.InputIx.Default) \n
		This command resets the attenuator and reconnects the RF input with the input mixer for the R&S FSW after an overload
		condition occurred and the protection mechanism intervened. The error status bit (bit 3 in the method RsFsw.Status.
		Questionable.Power.Event.get_ status register) and the INPUT OVLD message in the status bar are cleared. (See method
		RsFsw.Status.Questionable.Power.Event.get_ and 'STATus:QUEStionable:POWer register') . The command works only if the
		overload condition has been eliminated first. For details on the protection mechanism see 'RF Input Protection'. \n
			:param device_name: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = ''
		if device_name:
			param = Conversions.value_to_quoted_str(device_name)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:ATTenuation:PROTection:RESet {param}'.strip())
