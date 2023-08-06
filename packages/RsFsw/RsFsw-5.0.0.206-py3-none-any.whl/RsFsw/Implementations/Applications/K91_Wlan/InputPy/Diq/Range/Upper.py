from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upper:
	"""Upper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	def set(self, level: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<Undef>:DIQ:RANGe[:UPPer] \n
		Snippet: driver.applications.k91Wlan.inputPy.diq.range.upper.set(level = 1.0, inputIx = repcap.InputIx.Default) \n
		Defines or queries the 'Full Scale Level', i.e. the level that corresponds to an I/Q sample with the magnitude '1'. This
		command is only available if the optional Digital Baseband Interface is installed. \n
			:param level: Range: 1 μV to 7.071 V, Unit: DBM
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(level)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:DIQ:RANGe:UPPer {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<Undef>:DIQ:RANGe[:UPPer] \n
		Snippet: value: float = driver.applications.k91Wlan.inputPy.diq.range.upper.get(inputIx = repcap.InputIx.Default) \n
		Defines or queries the 'Full Scale Level', i.e. the level that corresponds to an I/Q sample with the magnitude '1'. This
		command is only available if the optional Digital Baseband Interface is installed. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: level: Range: 1 μV to 7.071 V, Unit: DBM"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:DIQ:RANGe:UPPer?')
		return Conversions.str_to_float(response)
