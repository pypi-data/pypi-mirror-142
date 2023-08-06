from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def set(self, result_type: enums.ResultTypeReference, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PREFerence:X \n
		Snippet: driver.applications.k18AmplifierEt.calculate.preference.x.set(result_type = enums.ResultTypeReference.PINPut, window = repcap.Window.Default) \n
		This command selects the type of information displayed on x-axis in the following result displays.
			INTRO_CMD_HELP: Thus, alignment need only be repeated if one of the following applies: \n
			- EVM vs Power
			- AM/PM
			- Gain Compression \n
			:param result_type: PINPut Shows the corresponding result against the input level. POUTput Shows the corresponding result against the output level.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(result_type, enums.ResultTypeReference)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PREFerence:X {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.ResultTypeReference:
		"""SCPI: CALCulate<n>:PREFerence:X \n
		Snippet: value: enums.ResultTypeReference = driver.applications.k18AmplifierEt.calculate.preference.x.get(window = repcap.Window.Default) \n
		This command selects the type of information displayed on x-axis in the following result displays.
			INTRO_CMD_HELP: Thus, alignment need only be repeated if one of the following applies: \n
			- EVM vs Power
			- AM/PM
			- Gain Compression \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: result_type: PINPut Shows the corresponding result against the input level. POUTput Shows the corresponding result against the output level."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PREFerence:X?')
		return Conversions.str_to_scalar_enum(response, enums.ResultTypeReference)
