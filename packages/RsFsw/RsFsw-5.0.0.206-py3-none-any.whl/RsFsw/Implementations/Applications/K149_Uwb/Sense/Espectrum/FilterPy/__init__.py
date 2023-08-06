from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 4 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	@property
	def rrc(self):
		"""rrc commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_rrc'):
			from .Rrc import Rrc
			self._rrc = Rrc(self._core, self._cmd_group)
		return self._rrc

	def set(self, state: bool, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:FILTer \n
		Snippet: driver.applications.k149Uwb.sense.espectrum.filterPy.set(state = False, subBlock = repcap.SubBlock.Default) \n
		No command help available \n
			:param state: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.bool_to_str(state)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:FILTer {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> bool:
		"""SCPI: [SENSe]:ESPectrum<sb>:FILTer \n
		Snippet: value: bool = driver.applications.k149Uwb.sense.espectrum.filterPy.get(subBlock = repcap.SubBlock.Default) \n
		No command help available \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: state: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:FILTer?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
