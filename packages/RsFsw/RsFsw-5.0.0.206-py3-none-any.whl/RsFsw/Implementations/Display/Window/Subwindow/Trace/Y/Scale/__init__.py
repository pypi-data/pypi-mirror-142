from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scale:
	"""Scale commands group definition. 8 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scale", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def refLevel(self):
		"""refLevel commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_refLevel'):
			from .RefLevel import RefLevel
			self._refLevel = RefLevel(self._core, self._cmd_group)
		return self._refLevel

	@property
	def rvalue(self):
		"""rvalue commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rvalue'):
			from .Rvalue import Rvalue
			self._rvalue = Rvalue(self._core, self._cmd_group)
		return self._rvalue

	@property
	def refPosition(self):
		"""refPosition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_refPosition'):
			from .RefPosition import RefPosition
			self._refPosition = RefPosition(self._core, self._cmd_group)
		return self._refPosition

	@property
	def pdivision(self):
		"""pdivision commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdivision'):
			from .Pdivision import Pdivision
			self._pdivision = Pdivision(self._core, self._cmd_group)
		return self._pdivision

	def set(self, range_py: float, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:TRACe<t>:Y[:SCALe] \n
		Snippet: driver.display.window.subwindow.trace.y.scale.set(range_py = 1.0, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, trace = repcap.Trace.Default) \n
		No command help available \n
			:param range_py: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.decimal_value_to_str(range_py)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe {param}')

	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, trace=repcap.Trace.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:TRACe<t>:Y[:SCALe] \n
		Snippet: value: float = driver.display.window.subwindow.trace.y.scale.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, trace = repcap.Trace.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: range_py: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Scale':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scale(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
