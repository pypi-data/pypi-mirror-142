from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	@property
	def abs(self):
		"""abs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_abs'):
			from .Abs import Abs
			self._abs = Abs(self._core, self._cmd_group)
		return self._abs

	@property
	def function(self):
		"""function commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_function'):
			from .Function import Function
			self._function = Function(self._core, self._cmd_group)
		return self._function

	def set(self, limit: float, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:LIMit:RELative:STOP \n
		Snippet: driver.applications.k14Xnr5G.sense.espectrum.range.limit.relative.stop.set(limit = 1.0, subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		No command help available \n
			:param limit: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(limit)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:LIMit:RELative:STOP {param}')

	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:LIMit:RELative:STOP \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.espectrum.range.limit.relative.stop.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		No command help available \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: limit: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:LIMit:RELative:STOP?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Stop':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Stop(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
