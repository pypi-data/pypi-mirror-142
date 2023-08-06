from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coupling:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)

	def set(self, state: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:DIQ:RANGe:COUPling \n
		Snippet: driver.inputPy.diq.range.coupling.set(state = False, inputIx = repcap.InputIx.Default) \n
		If enabled, the reference level for digital input is adjusted to the full scale level automatically if the full scale
		level changes. This command is only available if the optional Digital Baseband Interface is installed. \n
			:param state: ON | OFF | 1 | 0
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:DIQ:RANGe:COUPling {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<ip>:DIQ:RANGe:COUPling \n
		Snippet: value: bool = driver.inputPy.diq.range.coupling.get(inputIx = repcap.InputIx.Default) \n
		If enabled, the reference level for digital input is adjusted to the full scale level automatically if the full scale
		level changes. This command is only available if the optional Digital Baseband Interface is installed. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: state: ON | OFF | 1 | 0"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:DIQ:RANGe:COUPling?')
		return Conversions.str_to_bool(response)
