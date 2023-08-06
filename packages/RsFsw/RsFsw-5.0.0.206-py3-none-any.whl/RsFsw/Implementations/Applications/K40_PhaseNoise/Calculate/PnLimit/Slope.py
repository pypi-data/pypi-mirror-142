from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slope:
	"""Slope commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: LimitSegment, default value after init: LimitSegment.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slope", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_limitSegment_get', 'repcap_limitSegment_set', repcap.LimitSegment.Nr1)

	def repcap_limitSegment_set(self, limitSegment: repcap.LimitSegment) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to LimitSegment.Default
		Default value after init: LimitSegment.Nr1"""
		self._cmd_group.set_repcap_enum_value(limitSegment)

	def repcap_limitSegment_get(self) -> repcap.LimitSegment:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, slope: float, window=repcap.Window.Default, limitSegment=repcap.LimitSegment.Default) -> None:
		"""SCPI: CALCulate<n>:PNLimit:SLOPe<res> \n
		Snippet: driver.applications.k40PhaseNoise.calculate.pnLimit.slope.set(slope = 1.0, window = repcap.Window.Default, limitSegment = repcap.LimitSegment.Default) \n
		This command defines the slope for a phase noise limit line segment. \n
			:param slope: Level distance from the left border of the limit line segment to the previous one. Unit: dB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitSegment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slope')
		"""
		param = Conversions.decimal_value_to_str(slope)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitSegment_cmd_val = self._cmd_group.get_repcap_cmd_value(limitSegment, repcap.LimitSegment)
		self._core.io.write(f'CALCulate{window_cmd_val}:PNLimit:SLOPe{limitSegment_cmd_val} {param}')

	def get(self, window=repcap.Window.Default, limitSegment=repcap.LimitSegment.Default) -> float:
		"""SCPI: CALCulate<n>:PNLimit:SLOPe<res> \n
		Snippet: value: float = driver.applications.k40PhaseNoise.calculate.pnLimit.slope.get(window = repcap.Window.Default, limitSegment = repcap.LimitSegment.Default) \n
		This command defines the slope for a phase noise limit line segment. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitSegment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slope')
			:return: slope: Level distance from the left border of the limit line segment to the previous one. Unit: dB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitSegment_cmd_val = self._cmd_group.get_repcap_cmd_value(limitSegment, repcap.LimitSegment)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PNLimit:SLOPe{limitSegment_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Slope':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Slope(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
