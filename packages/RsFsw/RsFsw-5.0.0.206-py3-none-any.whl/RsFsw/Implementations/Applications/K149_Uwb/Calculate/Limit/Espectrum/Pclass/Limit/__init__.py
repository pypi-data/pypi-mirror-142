from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, mode: enums.LimitState, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, powerClass=repcap.PowerClass.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:PCLass<pc>:LIMit \n
		Snippet: driver.applications.k149Uwb.calculate.limit.espectrum.pclass.limit.set(mode = enums.LimitState.ABSolute, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, powerClass = repcap.PowerClass.Default) \n
		No command help available \n
			:param mode: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.LimitState)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:PCLass{powerClass_cmd_val}:LIMit {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, powerClass=repcap.PowerClass.Default) -> enums.LimitState:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:PCLass<pc>:LIMit \n
		Snippet: value: enums.LimitState = driver.applications.k149Uwb.calculate.limit.espectrum.pclass.limit.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, powerClass = repcap.PowerClass.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
			:return: mode: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:PCLass{powerClass_cmd_val}:LIMit?')
		return Conversions.str_to_scalar_enum(response, enums.LimitState)

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
