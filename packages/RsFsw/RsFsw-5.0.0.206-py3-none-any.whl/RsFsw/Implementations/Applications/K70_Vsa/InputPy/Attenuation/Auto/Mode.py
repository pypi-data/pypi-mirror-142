from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, att_mode: enums.AttenuatorMode, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:ATTenuation:AUTO:MODE \n
		Snippet: driver.applications.k70Vsa.inputPy.attenuation.auto.mode.set(att_mode = enums.AttenuatorMode.LDIStortion, inputIx = repcap.InputIx.Default) \n
		Selects the priority for signal processing after the RF attenuation has been applied. \n
			:param att_mode: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(att_mode, enums.AttenuatorMode)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:ATTenuation:AUTO:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.AttenuatorMode:
		"""SCPI: INPut<ip>:ATTenuation:AUTO:MODE \n
		Snippet: value: enums.AttenuatorMode = driver.applications.k70Vsa.inputPy.attenuation.auto.mode.get(inputIx = repcap.InputIx.Default) \n
		Selects the priority for signal processing after the RF attenuation has been applied. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: att_mode: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:ATTenuation:AUTO:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AttenuatorMode)
