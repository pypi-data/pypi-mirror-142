from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	@property
	def function(self):
		"""function commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_function'):
			from .Function import Function
			self._function = Function(self._core, self._cmd_group)
		return self._function

	@property
	def abs(self):
		"""abs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_abs'):
			from .Abs import Abs
			self._abs = Abs(self._core, self._cmd_group)
		return self._abs

	def set(self, level: float, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:LIMit<li>:RELative:STOP \n
		Snippet: driver.sense.espectrum.range.limit.relative.stop.set(level = 1.0, subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default, limitIx = repcap.LimitIx.Default) \n
		This command defines a relative limit for a SEM range. Unlike manual operation, you can define a relative limit anytime
		and regardless of the limit check mode. \n
			:param level: Relative limit at the stop frequency of a SEM range. Range: -400 to 400, Unit: dBc
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.decimal_value_to_str(level)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:LIMit{limitIx_cmd_val}:RELative:STOP {param}')

	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default, limitIx=repcap.LimitIx.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:LIMit<li>:RELative:STOP \n
		Snippet: value: float = driver.sense.espectrum.range.limit.relative.stop.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default, limitIx = repcap.LimitIx.Default) \n
		This command defines a relative limit for a SEM range. Unlike manual operation, you can define a relative limit anytime
		and regardless of the limit check mode. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: level: Relative limit at the stop frequency of a SEM range. Range: -400 to 400, Unit: dBc"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:LIMit{limitIx_cmd_val}:RELative:STOP?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Stop':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Stop(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
