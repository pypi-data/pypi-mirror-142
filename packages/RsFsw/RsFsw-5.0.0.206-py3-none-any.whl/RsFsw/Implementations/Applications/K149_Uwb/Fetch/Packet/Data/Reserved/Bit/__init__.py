from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bit:
	"""Bit commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bit", core, parent)

	@property
	def apackets(self):
		"""apackets commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apackets'):
			from .Apackets import Apackets
			self._apackets = Apackets(self._core, self._cmd_group)
		return self._apackets

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: FETCh<n>:PACKet:DATA:REServed:BIT \n
		Snippet: value: str = driver.applications.k149Uwb.fetch.packet.data.reserved.bit.get(window = repcap.Window.Default) \n
		Returns whether the value of SFD is the same (IDEN) or not (MIX) for all packets. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fetch')
			:return: result: Window"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'FETCh{window_cmd_val}:PACKet:DATA:REServed:BIT?')
		return trim_str_response(response)

	def clone(self) -> 'Bit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
