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

	def set(self, order_by: enums.ReferenceMode, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:MODE \n
		Snippet: driver.applications.k18AmplifierEt.calculate.deltaMarker.mode.set(order_by = enums.ReferenceMode.ABSolute, window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		No command help available \n
			:param order_by: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		param = Conversions.enum_scalar_to_str(order_by, enums.ReferenceMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> enums.ReferenceMode:
		"""SCPI: CALCulate<n>:DELTamarker<m>:MODE \n
		Snippet: value: enums.ReferenceMode = driver.applications.k18AmplifierEt.calculate.deltaMarker.mode.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:return: order_by: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceMode)
