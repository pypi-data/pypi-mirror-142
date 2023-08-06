from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dstyle:
	"""Dstyle commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dstyle", core, parent)

	def set(self, type_py: enums.DotStyle, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:DSTYle \n
		Snippet: driver.applications.k6Pulse.calculate.trend.dstyle.set(type_py = enums.DotStyle.AUTO, window = repcap.Window.Default) \n
		No command help available \n
			:param type_py: AUTO | DOTS | LINes | DLINes
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.DotStyle)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:DSTYle {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.DotStyle:
		"""SCPI: CALCulate<n>:TRENd:DSTYle \n
		Snippet: value: enums.DotStyle = driver.applications.k6Pulse.calculate.trend.dstyle.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: type_py: AUTO | DOTS | LINes | DLINes"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TRENd:DSTYle?')
		return Conversions.str_to_scalar_enum(response, enums.DotStyle)
