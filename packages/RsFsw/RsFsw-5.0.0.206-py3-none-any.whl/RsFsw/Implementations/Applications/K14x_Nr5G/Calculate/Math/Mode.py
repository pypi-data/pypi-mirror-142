from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.AverageModeA, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MATH:MODE \n
		Snippet: driver.applications.k14Xnr5G.calculate.math.mode.set(mode = enums.AverageModeA.LINear, window = repcap.Window.Default) \n
		No command help available \n
			:param mode: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AverageModeA)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MATH:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.AverageModeA:
		"""SCPI: CALCulate<n>:MATH:MODE \n
		Snippet: value: enums.AverageModeA = driver.applications.k14Xnr5G.calculate.math.mode.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: mode: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MATH:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AverageModeA)
