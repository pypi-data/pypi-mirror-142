from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, level: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<Undef>:GAIN[:VALue] \n
		Snippet: driver.applications.k9X11Ad.inputPy.gain.value.set(level = 1.0, inputIx = repcap.InputIx.Default) \n
		This command selects the gain if the preamplifier is activated (INP:GAIN:STAT ON, see method RsFsw.Applications.K10x_Lte.
		InputPy.Gain.State.set) . The command requires the additional preamplifier hardware option. \n
			:param level: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(level)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:GAIN:VALue {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<Undef>:GAIN[:VALue] \n
		Snippet: value: float = driver.applications.k9X11Ad.inputPy.gain.value.get(inputIx = repcap.InputIx.Default) \n
		This command selects the gain if the preamplifier is activated (INP:GAIN:STAT ON, see method RsFsw.Applications.K10x_Lte.
		InputPy.Gain.State.set) . The command requires the additional preamplifier hardware option. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: level: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:GAIN:VALue?')
		return Conversions.str_to_float(response)
