from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RwConfig:
	"""RwConfig commands group definition. 5 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rwConfig", core, parent)

	@property
	def configure(self):
		"""configure commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_configure'):
			from .Configure import Configure
			self._configure = Configure(self._core, self._cmd_group)
		return self._configure

	@property
	def group(self):
		"""group commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_group'):
			from .Group import Group
			self._group = Group(self._core, self._cmd_group)
		return self._group

	@property
	def link(self):
		"""link commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_link'):
			from .Link import Link
			self._link = Link(self._core, self._cmd_group)
		return self._link

	@property
	def packet(self):
		"""packet commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_packet'):
			from .Packet import Packet
			self._packet = Packet(self._core, self._cmd_group)
		return self._packet

	def set(self, config: enums.ConfigMode, window=repcap.Window.Default) -> None:
		"""SCPI: SENSe[:WINDow<n>]:DISPlay:RWConfig \n
		Snippet: driver.applications.k149Uwb.sense.window.display.rwConfig.set(config = enums.ConfigMode.DEFault, window = repcap.Window.Default) \n
		Sets the result config configuration to default or user. \n
			:param config: DEFault | USER
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.enum_scalar_to_str(config, enums.ConfigMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:DISPlay:RWConfig {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.ConfigMode:
		"""SCPI: SENSe[:WINDow<n>]:DISPlay:RWConfig \n
		Snippet: value: enums.ConfigMode = driver.applications.k149Uwb.sense.window.display.rwConfig.get(window = repcap.Window.Default) \n
		Sets the result config configuration to default or user. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: config: DEFault | USER"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:DISPlay:RWConfig?')
		return Conversions.str_to_scalar_enum(response, enums.ConfigMode)

	def clone(self) -> 'RwConfig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RwConfig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
