from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 156 total commands, 15 Subgroups, 2 group commands
	Repeated Capability: LimitIx, default value after init: LimitIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_limitIx_get', 'repcap_limitIx_set', repcap.LimitIx.Nr1)

	def repcap_limitIx_set(self, limitIx: repcap.LimitIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to LimitIx.Default
		Default value after init: LimitIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(limitIx)

	def repcap_limitIx_get(self) -> repcap.LimitIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def acPower(self):
		"""acPower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_acPower'):
			from .AcPower import AcPower
			self._acPower = AcPower(self._core, self._cmd_group)
		return self._acPower

	@property
	def active(self):
		"""active commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_active'):
			from .Active import Active
			self._active = Active(self._core, self._cmd_group)
		return self._active

	@property
	def cc(self):
		"""cc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import Cc
			self._cc = Cc(self._core, self._cmd_group)
		return self._cc

	@property
	def clear(self):
		"""clear commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_clear'):
			from .Clear import Clear
			self._clear = Clear(self._core, self._cmd_group)
		return self._clear

	@property
	def comment(self):
		"""comment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_comment'):
			from .Comment import Comment
			self._comment = Comment(self._core, self._cmd_group)
		return self._comment

	@property
	def control(self):
		"""control commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_control'):
			from .Control import Control
			self._control = Control(self._core, self._cmd_group)
		return self._control

	@property
	def espectrum(self):
		"""espectrum commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_espectrum'):
			from .Espectrum import Espectrum
			self._espectrum = Espectrum(self._core, self._cmd_group)
		return self._espectrum

	@property
	def fail(self):
		"""fail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fail'):
			from .Fail import Fail
			self._fail = Fail(self._core, self._cmd_group)
		return self._fail

	@property
	def lower(self):
		"""lower commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_lower'):
			from .Lower import Lower
			self._lower = Lower(self._core, self._cmd_group)
		return self._lower

	@property
	def name(self):
		"""name commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_name'):
			from .Name import Name
			self._name = Name(self._core, self._cmd_group)
		return self._name

	@property
	def ooPower(self):
		"""ooPower commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ooPower'):
			from .OoPower import OoPower
			self._ooPower = OoPower(self._core, self._cmd_group)
		return self._ooPower

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	@property
	def upper(self):
		"""upper commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_upper'):
			from .Upper import Upper
			self._upper = Upper(self._core, self._cmd_group)
		return self._upper

	def copy(self, limit_line: int, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:COPY \n
		Snippet: driver.applications.k14Xnr5G.calculate.limit.copy(limit_line = 1, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param limit_line: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.decimal_value_to_str(limit_line)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:COPY {param}')

	def delete(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:DELete \n
		Snippet: driver.applications.k14Xnr5G.calculate.limit.delete(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:DELete')

	def delete_with_opc(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		"""SCPI: CALCulate<n>:LIMit<li>:DELete \n
		Snippet: driver.applications.k14Xnr5G.calculate.limit.delete_with_opc(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:DELete', opc_timeout_ms)

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
