from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Abs:
	"""Abs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("abs", core, parent)

	def set(self, level: float, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:LIMit<li>:RELative:STARt:ABS \n
		Snippet: driver.sense.espectrum.range.limit.relative.start.abs.set(level = 1.0, subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default, limitIx = repcap.LimitIx.Default) \n
		This command defines an absolute limit for the MAX function of the relative limit for a SEM range. For more information
		see 'Relative limit line functions'. \n
			:param level: Absolute limit at the start frequency of a SEM range to be used in addition to the relative limit if the MAX function is enabled (see [SENSe:]ESPectrumsb:RANGeri:LIMitli:RELative:STARt:FUNCtion) . Range: -400 to 400, Unit: dBm
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.decimal_value_to_str(level)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:LIMit{limitIx_cmd_val}:RELative:STARt:ABS {param}')

	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default, limitIx=repcap.LimitIx.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:LIMit<li>:RELative:STARt:ABS \n
		Snippet: value: float = driver.sense.espectrum.range.limit.relative.start.abs.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default, limitIx = repcap.LimitIx.Default) \n
		This command defines an absolute limit for the MAX function of the relative limit for a SEM range. For more information
		see 'Relative limit line functions'. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: level: Absolute limit at the start frequency of a SEM range to be used in addition to the relative limit if the MAX function is enabled (see [SENSe:]ESPectrumsb:RANGeri:LIMitli:RELative:STARt:FUNCtion) . Range: -400 to 400, Unit: dBm"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:LIMit{limitIx_cmd_val}:RELative:STARt:ABS?')
		return Conversions.str_to_float(response)
