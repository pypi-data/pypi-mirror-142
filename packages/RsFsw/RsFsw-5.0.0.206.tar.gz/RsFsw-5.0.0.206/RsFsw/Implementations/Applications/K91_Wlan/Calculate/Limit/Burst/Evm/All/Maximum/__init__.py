from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_result'):
			from .Result import Result
			self._result = Result(self._core, self._cmd_group)
		return self._result

	def set(self, limit: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:BURSt:EVM:ALL:MAXimum \n
		Snippet: driver.applications.k91Wlan.calculate.limit.burst.evm.all.maximum.set(limit = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command sets or queries the average or maximum error vector magnitude limit for all carriers as determined by the
		default WLAN measurement. For details see 'Modulation accuracy, flatness and tolerance parameters'. \n
			:param limit: numeric value in dB The unit for the EVM parameters can be changed in advance using method RsFsw.Applications.K10x_Lte.Unit.Evm.set. Unit: DB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.decimal_value_to_str(limit)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:BURSt:EVM:ALL:MAXimum {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit<li>:BURSt:EVM:ALL:MAXimum \n
		Snippet: value: float = driver.applications.k91Wlan.calculate.limit.burst.evm.all.maximum.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command sets or queries the average or maximum error vector magnitude limit for all carriers as determined by the
		default WLAN measurement. For details see 'Modulation accuracy, flatness and tolerance parameters'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: limit: numeric value in dB The unit for the EVM parameters can be changed in advance using method RsFsw.Applications.K10x_Lte.Unit.Evm.set. Unit: DB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:BURSt:EVM:ALL:MAXimum?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Maximum':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Maximum(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
