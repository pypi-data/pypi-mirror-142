from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CbIndex:
	"""CbIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbIndex", core, parent)

	def set(self, code_book_index: float, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SUBFrame<sf>:ALLoc<al>:PRECoding:CBINdex \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.subframe.alloc.precoding.cbIndex.set(code_book_index = 1.0, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, allocation = repcap.Allocation.Default) \n
		This command selects the codebook index for an allocation with spatial multiplexing precoding scheme. \n
			:param code_book_index: 0...15
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(code_book_index)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc{allocation_cmd_val}:PRECoding:CBINdex {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, allocation=repcap.Allocation.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SUBFrame<sf>:ALLoc<al>:PRECoding:CBINdex \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.subframe.alloc.precoding.cbIndex.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, allocation = repcap.Allocation.Default) \n
		This command selects the codebook index for an allocation with spatial multiplexing precoding scheme. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: code_book_index: 0...15"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc{allocation_cmd_val}:PRECoding:CBINdex?')
		return Conversions.str_to_float(response)
