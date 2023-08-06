from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tx:
	"""Tx commands group definition. 3 total commands, 2 Subgroups, 1 group commands
	Repeated Capability: Channel, default value after init: Channel.Ch1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tx", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_channel_get', 'repcap_channel_set', repcap.Channel.Ch1)

	def repcap_channel_set(self, channel: repcap.Channel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Channel.Default
		Default value after init: Channel.Ch1"""
		self._cmd_group.set_repcap_enum_value(channel)

	def repcap_channel_get(self) -> repcap.Channel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def stream(self):
		"""stream commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stream'):
			from .Stream import Stream
			self._stream = Stream(self._core, self._cmd_group)
		return self._stream

	@property
	def timeShift(self):
		"""timeShift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_timeShift'):
			from .TimeShift import TimeShift
			self._timeShift = TimeShift(self._core, self._cmd_group)
		return self._timeShift

	def set(self, stsi: List[float], channel=repcap.Channel.Default) -> None:
		"""SCPI: CONFigure:WLAN:SMAPping:TX<ch> \n
		Snippet: driver.applications.k91Wlan.configure.wlan.smapping.tx.set(stsi = [1.1, 2.2, 3.3], channel = repcap.Channel.Default) \n
		This remote control command specifies the mapping for all streams (real & imaginary data pairs) and timeshift for a
		specified antenna. \n
			:param stsi: Imag part of the complex element of the STS-Stream
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Tx')
		"""
		param = Conversions.list_to_csv_str(stsi)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'CONFigure:WLAN:SMAPping:TX{channel_cmd_val} {param}')

	def get(self, channel=repcap.Channel.Default) -> List[float]:
		"""SCPI: CONFigure:WLAN:SMAPping:TX<ch> \n
		Snippet: value: List[float] = driver.applications.k91Wlan.configure.wlan.smapping.tx.get(channel = repcap.Channel.Default) \n
		This remote control command specifies the mapping for all streams (real & imaginary data pairs) and timeshift for a
		specified antenna. \n
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Tx')
			:return: stsi: Imag part of the complex element of the STS-Stream"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_bin_or_ascii_float_list(f'CONFigure:WLAN:SMAPping:TX{channel_cmd_val}?')
		return response

	def clone(self) -> 'Tx':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tx(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
