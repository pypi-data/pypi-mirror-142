from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preset:
	"""Preset commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preset", core, parent)

	@property
	def restore(self):
		"""restore commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_restore'):
			from .Restore import Restore
			self._restore = Restore(self._core, self._cmd_group)
		return self._restore

	@property
	def standard(self):
		"""standard commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_standard'):
			from .Standard import Standard
			self._standard = Standard(self._core, self._cmd_group)
		return self._standard

	@property
	def store(self):
		"""store commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_store'):
			from .Store import Store
			self._store = Store(self._core, self._cmd_group)
		return self._store

	def set(self, table_high: str, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:PRESet \n
		Snippet: driver.applications.k149Uwb.sense.espectrum.preset.set(table_high = '1', subBlock = repcap.SubBlock.Default) \n
		No command help available \n
			:param table_high: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.value_to_quoted_str(table_high)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:PRESet {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> str:
		"""SCPI: [SENSe]:ESPectrum<sb>:PRESet \n
		Snippet: value: str = driver.applications.k149Uwb.sense.espectrum.preset.get(subBlock = repcap.SubBlock.Default) \n
		No command help available \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: table_high: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:PRESet?')
		return trim_str_response(response)

	def clone(self) -> 'Preset':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Preset(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
