from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cont:
	"""Cont commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cont", core, parent)

	def set(self, allocation_content: enums.AllocationContent, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc:CONT \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.cont.set(allocation_content = enums.AllocationContent.NONE, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		This command allocates a PUCCH or PUSCH to an uplink allocation. \n
			:param allocation_content: NONE Turns off the PUSCH and the PUCCH. PUCCh Turns on the PUCCH. PUSCh Turns on the PUSCH. PSCC Turns on the PUCCH as well as the PUSCH.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
		"""
		param = Conversions.enum_scalar_to_str(allocation_content, enums.AllocationContent)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:CONT {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> enums.AllocationContent:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc:CONT \n
		Snippet: value: enums.AllocationContent = driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.cont.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		This command allocates a PUCCH or PUSCH to an uplink allocation. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:return: allocation_content: NONE Turns off the PUSCH and the PUCCH. PUCCh Turns on the PUCCH. PUSCh Turns on the PUSCH. PSCC Turns on the PUCCH as well as the PUSCH."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:CONT?')
		return Conversions.str_to_scalar_enum(response, enums.AllocationContent)
