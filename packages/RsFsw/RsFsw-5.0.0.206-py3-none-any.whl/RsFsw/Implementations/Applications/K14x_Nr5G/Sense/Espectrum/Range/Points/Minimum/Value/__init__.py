from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	@property
	def dummy(self):
		"""dummy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dummy'):
			from .Dummy import Dummy
			self._dummy = Dummy(self._core, self._cmd_group)
		return self._dummy

	def set(self, sweep_point: float, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:POINts:MINimum[:VALue] \n
		Snippet: driver.applications.k14Xnr5G.sense.espectrum.range.points.minimum.value.set(sweep_point = 1.0, subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		No command help available \n
			:param sweep_point: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(sweep_point)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:POINts:MINimum:VALue {param}')

	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:POINts:MINimum[:VALue] \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.espectrum.range.points.minimum.value.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		No command help available \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: sweep_point: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:POINts:MINimum:VALue?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Value':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Value(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
