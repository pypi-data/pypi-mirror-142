from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.AverageModeA, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MATH:MODE \n
		Snippet: driver.calculate.math.mode.set(mode = enums.AverageModeA.LINear, window = repcap.Window.Default) \n
		This command selects the way the R&S FSW calculates trace mathematics. \n
			:param mode: For more information on the way each mode works see Trace Math Mode. LINear Linear calculation. LOGarithmic Logarithmic calculation. POWer Linear power calculation.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AverageModeA)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MATH:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.AverageModeA:
		"""SCPI: CALCulate<n>:MATH:MODE \n
		Snippet: value: enums.AverageModeA = driver.calculate.math.mode.get(window = repcap.Window.Default) \n
		This command selects the way the R&S FSW calculates trace mathematics. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: mode: For more information on the way each mode works see Trace Math Mode. LINear Linear calculation. LOGarithmic Logarithmic calculation. POWer Linear power calculation."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MATH:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AverageModeA)
