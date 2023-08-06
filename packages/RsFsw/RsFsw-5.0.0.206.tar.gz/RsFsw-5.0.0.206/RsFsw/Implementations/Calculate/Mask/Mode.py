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

	def set(self, mode: enums.ReferenceMode, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MASK:MODE \n
		Snippet: driver.calculate.mask.mode.set(mode = enums.ReferenceMode.ABSolute, window = repcap.Window.Default) \n
		This command defines the scaling of the level axis for frequency masks. \n
			:param mode: ABSolute absolute scaling of the level axis. RELative relative scaling of the level axis.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ReferenceMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MASK:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.ReferenceMode:
		"""SCPI: CALCulate<n>:MASK:MODE \n
		Snippet: value: enums.ReferenceMode = driver.calculate.mask.mode.get(window = repcap.Window.Default) \n
		This command defines the scaling of the level axis for frequency masks. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: mode: ABSolute absolute scaling of the level axis. RELative relative scaling of the level axis."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MASK:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceMode)
