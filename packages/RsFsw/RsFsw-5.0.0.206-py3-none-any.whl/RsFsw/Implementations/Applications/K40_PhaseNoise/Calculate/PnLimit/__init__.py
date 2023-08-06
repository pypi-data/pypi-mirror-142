from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PnLimit:
	"""PnLimit commands group definition. 8 total commands, 7 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pnLimit", core, parent)

	@property
	def fail(self):
		"""fail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fail'):
			from .Fail import Fail
			self._fail = Fail(self._core, self._cmd_group)
		return self._fail

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def fc(self):
		"""fc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fc'):
			from .Fc import Fc
			self._fc = Fc(self._core, self._cmd_group)
		return self._fc

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	@property
	def noise(self):
		"""noise commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noise'):
			from .Noise import Noise
			self._noise = Noise(self._core, self._cmd_group)
		return self._noise

	@property
	def slope(self):
		"""slope commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slope'):
			from .Slope import Slope
			self._slope = Slope(self._core, self._cmd_group)
		return self._slope

	@property
	def trace(self):
		"""trace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	def copy(self, window=repcap.Window.Default, targetLimitLine=repcap.TargetLimitLine.Nr1) -> None:
		"""SCPI: CALCulate<n>:PNLimit:COPY<k> \n
		Snippet: driver.applications.k40PhaseNoise.calculate.pnLimit.copy(window = repcap.Window.Default, targetLimitLine = repcap.TargetLimitLine.Nr1) \n
		Creates a new user limit line from the data of a phase noise limit line. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param targetLimitLine: optional repeated capability selector. Default value: Nr1
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		targetLimitLine_cmd_val = self._cmd_group.get_repcap_cmd_value(targetLimitLine, repcap.TargetLimitLine)
		self._core.io.write(f'CALCulate{window_cmd_val}:PNLimit:COPY{targetLimitLine_cmd_val}')

	def copy_with_opc(self, window=repcap.Window.Default, targetLimitLine=repcap.TargetLimitLine.Nr1, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		targetLimitLine_cmd_val = self._cmd_group.get_repcap_cmd_value(targetLimitLine, repcap.TargetLimitLine)
		"""SCPI: CALCulate<n>:PNLimit:COPY<k> \n
		Snippet: driver.applications.k40PhaseNoise.calculate.pnLimit.copy_with_opc(window = repcap.Window.Default, targetLimitLine = repcap.TargetLimitLine.Nr1) \n
		Creates a new user limit line from the data of a phase noise limit line. \n
		Same as copy, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param targetLimitLine: optional repeated capability selector. Default value: Nr1
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:PNLimit:COPY{targetLimitLine_cmd_val}', opc_timeout_ms)

	def clone(self) -> 'PnLimit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PnLimit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
