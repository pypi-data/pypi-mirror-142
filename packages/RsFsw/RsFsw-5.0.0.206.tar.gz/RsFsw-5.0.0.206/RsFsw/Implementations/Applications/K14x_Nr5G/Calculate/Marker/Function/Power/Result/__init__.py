from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def details(self):
		"""details commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_details'):
			from .Details import Details
			self._details = Details(self._core, self._cmd_group)
		return self._details

	@property
	def phz(self):
		"""phz commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phz'):
			from .Phz import Phz
			self._phz = Phz(self._core, self._cmd_group)
		return self._phz

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	def set(self, measurement: enums.MarkerFunctionA, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer:RESult \n
		Snippet: driver.applications.k14Xnr5G.calculate.marker.function.power.result.set(measurement = enums.MarkerFunctionA.ACPower, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		No command help available \n
			:param measurement: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.enum_scalar_to_str(measurement, enums.MarkerFunctionA)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer:RESult {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> enums.MarkerFunctionA:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer:RESult \n
		Snippet: value: enums.MarkerFunctionA = driver.applications.k14Xnr5G.calculate.marker.function.power.result.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: measurement: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer:RESult?')
		return Conversions.str_to_scalar_enum(response, enums.MarkerFunctionA)

	def clone(self) -> 'Result':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Result(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
