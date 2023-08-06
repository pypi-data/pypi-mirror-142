from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pmeter:
	"""Pmeter commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: PowerMeter, default value after init: PowerMeter.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmeter", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_powerMeter_get', 'repcap_powerMeter_set', repcap.PowerMeter.Nr1)

	def repcap_powerMeter_set(self, powerMeter: repcap.PowerMeter) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PowerMeter.Default
		Default value after init: PowerMeter.Nr1"""
		self._cmd_group.set_repcap_enum_value(powerMeter)

	def repcap_powerMeter_get(self) -> repcap.PowerMeter:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def get(self, powerMeter=repcap.PowerMeter.Default) -> List[float]:
		"""SCPI: READ:PMETer<p> \n
		Snippet: value: List[float] = driver.applications.k50Spurious.read.pmeter.get(powerMeter = repcap.PowerMeter.Default) \n
		This command initiates a power sensor measurement and queries the results. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: result: No help available"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_bin_or_ascii_float_list(f'READ:PMETer{powerMeter_cmd_val}?')
		return response

	def clone(self) -> 'Pmeter':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pmeter(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
