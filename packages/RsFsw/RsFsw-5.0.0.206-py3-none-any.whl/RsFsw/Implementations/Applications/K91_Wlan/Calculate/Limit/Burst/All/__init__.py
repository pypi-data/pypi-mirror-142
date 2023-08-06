from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_result'):
			from .Result import Result
			self._result = Result(self._core, self._cmd_group)
		return self._result

	def set(self, limits: List[float], window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:BURSt:ALL \n
		Snippet: driver.applications.k91Wlan.calculate.limit.burst.all.set(limits = [1.1, 2.2, 3.3], window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command sets or returns the limit values for the parameters determined by the default WLAN measurement all in one
		step. For details see 'Modulation accuracy, flatness and tolerance parameters'. To define individual limit values use the
		individual CALCulate<n>:LIMit<k>:BURSt... commands. Note that the units for the EVM and gain imbalance parameters must be
		defined in advance using the following commands:
			INTRO_CMD_HELP: The .csv file has the following structure: \n
			- method RsFsw.Applications.K10x_Lte.Unit.Evm.set
			- method RsFsw.Applications.K91_Wlan.Unit.Gimbalance.set \n
			:param limits: The parameters are input or output as a list of (ASCII) values separated by ',' in the following order: average CF error, max CF error, average symbol clock error, max symbol clock error, average I/Q offset, maximum I/Q offset, average EVM all carriers, max EVM all carriers, average EVM data carriers, max EVM data carriers average EVM pilots, max EVM pilots
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.list_to_csv_str(limits)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:BURSt:ALL {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> List[float]:
		"""SCPI: CALCulate<n>:LIMit<li>:BURSt:ALL \n
		Snippet: value: List[float] = driver.applications.k91Wlan.calculate.limit.burst.all.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command sets or returns the limit values for the parameters determined by the default WLAN measurement all in one
		step. For details see 'Modulation accuracy, flatness and tolerance parameters'. To define individual limit values use the
		individual CALCulate<n>:LIMit<k>:BURSt... commands. Note that the units for the EVM and gain imbalance parameters must be
		defined in advance using the following commands:
			INTRO_CMD_HELP: The .csv file has the following structure: \n
			- method RsFsw.Applications.K10x_Lte.Unit.Evm.set
			- method RsFsw.Applications.K91_Wlan.Unit.Gimbalance.set \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: limits: The parameters are input or output as a list of (ASCII) values separated by ',' in the following order: average CF error, max CF error, average symbol clock error, max symbol clock error, average I/Q offset, maximum I/Q offset, average EVM all carriers, max EVM all carriers, average EVM data carriers, max EVM data carriers average EVM pilots, max EVM pilots"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_bin_or_ascii_float_list(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:BURSt:ALL?')
		return response

	def clone(self) -> 'All':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = All(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
