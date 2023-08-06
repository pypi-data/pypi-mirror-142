from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mreference:
	"""Mreference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mreference", core, parent)

	def set(self, arg_0: int, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:MREFerence \n
		Snippet: driver.applications.k30NoiseFigure.calculate.deltaMarker.mreference.set(arg_0 = 1, window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command selects a reference marker for a delta marker other than marker 1. The reference may be another marker or
		the fixed reference. \n
			:param arg_0: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:MREFerence {param}')

	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> int:
		"""SCPI: CALCulate<n>:DELTamarker<m>:MREFerence \n
		Snippet: value: int = driver.applications.k30NoiseFigure.calculate.deltaMarker.mreference.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command selects a reference marker for a delta marker other than marker 1. The reference may be another marker or
		the fixed reference. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:return: arg_0: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:MREFerence?')
		return Conversions.str_to_int(response)
