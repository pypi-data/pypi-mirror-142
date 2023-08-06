from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ClMapping:
	"""ClMapping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clMapping", core, parent)

	def set(self, mapping: enums.LayerMappingUl, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc:PRECoding:CLMapping \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.precoding.clMapping.set(mapping = enums.LayerMappingUl.LC11, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		This command selects the codeword to layer mapping for a PUSCH allocation. \n
			:param mapping: LC11 | LC21 | LC22
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
		"""
		param = Conversions.enum_scalar_to_str(mapping, enums.LayerMappingUl)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:PRECoding:CLMapping {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> enums.LayerMappingUl:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc:PRECoding:CLMapping \n
		Snippet: value: enums.LayerMappingUl = driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.precoding.clMapping.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		This command selects the codeword to layer mapping for a PUSCH allocation. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:return: mapping: LC11 | LC21 | LC22"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:PRECoding:CLMapping?')
		return Conversions.str_to_scalar_enum(response, enums.LayerMappingUl)
