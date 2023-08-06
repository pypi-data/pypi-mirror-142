from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Function:
	"""Function commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("function", core, parent)

	def set(self, function: enums.FunctionA, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:LIMit<li>:RELative:STARt:FUNCtion \n
		Snippet: driver.sense.espectrum.range.limit.relative.start.function.set(function = enums.FunctionA.MAX, subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param function: OFF | MAX Defines the function to be used to determine the relative limit line start value MAX The maximum of the relative and the absolute level is used as the limit start value. Use the [SENSe:]ESPectrumsb:RANGeri:LIMitli:RELative:STARt and [SENSe:]ESPectrumsb:RANGeri:LIMitli:RELative:STARt:ABS commands to define these values. OFF No function is used, the relative limit line is defined by a fixed relative start value. Use the [SENSe:]ESPectrumsb:RANGeri:LIMitli:RELative:STARtcommand to define this value.
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.enum_scalar_to_str(function, enums.FunctionA)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:LIMit{limitIx_cmd_val}:RELative:STARt:FUNCtion {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default, limitIx=repcap.LimitIx.Default) -> enums.FunctionA:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:LIMit<li>:RELative:STARt:FUNCtion \n
		Snippet: value: enums.FunctionA = driver.sense.espectrum.range.limit.relative.start.function.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: function: OFF | MAX Defines the function to be used to determine the relative limit line start value MAX The maximum of the relative and the absolute level is used as the limit start value. Use the [SENSe:]ESPectrumsb:RANGeri:LIMitli:RELative:STARt and [SENSe:]ESPectrumsb:RANGeri:LIMitli:RELative:STARt:ABS commands to define these values. OFF No function is used, the relative limit line is defined by a fixed relative start value. Use the [SENSe:]ESPectrumsb:RANGeri:LIMitli:RELative:STARtcommand to define this value."""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:LIMit{limitIx_cmd_val}:RELative:STARt:FUNCtion?')
		return Conversions.str_to_scalar_enum(response, enums.FunctionA)
