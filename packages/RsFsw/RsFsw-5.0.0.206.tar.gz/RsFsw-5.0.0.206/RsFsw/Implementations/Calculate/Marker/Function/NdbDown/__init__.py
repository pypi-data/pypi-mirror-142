from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NdbDown:
	"""NdbDown commands group definition. 6 total commands, 5 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ndbDown", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_result'):
			from .Result import Result
			self._result = Result(self._core, self._cmd_group)
		return self._result

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def qfactor(self):
		"""qfactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qfactor'):
			from .Qfactor import Qfactor
			self._qfactor = Qfactor(self._core, self._cmd_group)
		return self._qfactor

	def set(self, distance: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:NDBDown \n
		Snippet: driver.calculate.marker.function.ndbDown.set(distance = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines the distance of the n dB down markers to the reference marker. \n
			:param distance: Distance of the temporary markers to the reference marker in dB. For a positive offset, the markers T1 and T2 are placed below the active reference point. For a negative offset (for example for notch filter measurements) , the markers T1 and T2 are placed above the active reference point. Unit: DB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(distance)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:NDBDown {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:NDBDown \n
		Snippet: value: float = driver.calculate.marker.function.ndbDown.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines the distance of the n dB down markers to the reference marker. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: distance: Distance of the temporary markers to the reference marker in dB. For a positive offset, the markers T1 and T2 are placed below the active reference point. For a negative offset (for example for notch filter measurements) , the markers T1 and T2 are placed above the active reference point. Unit: DB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:NDBDown?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'NdbDown':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NdbDown(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
