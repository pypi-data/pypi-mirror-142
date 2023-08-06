from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pmode:
	"""Pmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmode", core, parent)

	def set(self, mode: enums.LogicalFnc, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:PMODe \n
		Snippet: driver.calculate.limit.acPower.pmode.set(mode = enums.LogicalFnc.AND, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param mode: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.LogicalFnc)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:PMODe {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> enums.LogicalFnc:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:PMODe \n
		Snippet: value: enums.LogicalFnc = driver.calculate.limit.acPower.pmode.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: mode: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:PMODe?')
		return Conversions.str_to_scalar_enum(response, enums.LogicalFnc)
