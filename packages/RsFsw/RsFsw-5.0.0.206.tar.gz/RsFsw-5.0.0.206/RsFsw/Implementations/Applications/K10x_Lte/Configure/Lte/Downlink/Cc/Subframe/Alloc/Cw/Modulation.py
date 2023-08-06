from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	def set(self, modulation: enums.ModulationDl, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, allocation=repcap.Allocation.Default, codeword=repcap.Codeword.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SUBFrame<sf>:ALLoc<al>[:CW<cw>]:MODulation \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.subframe.alloc.cw.modulation.set(modulation = enums.ModulationDl.Q1K, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, allocation = repcap.Allocation.Default, codeword = repcap.Codeword.Default) \n
		This command selects the modulation of an allocation in a downlink subframe. \n
			:param modulation: QPSK QPSK modulation QAM16 16QAM modulation QAM64 64QAM modulation QAM256 256QAM modulation Q1K 1024QAM modulation
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param codeword: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cw')
		"""
		param = Conversions.enum_scalar_to_str(modulation, enums.ModulationDl)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		codeword_cmd_val = self._cmd_group.get_repcap_cmd_value(codeword, repcap.Codeword)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc{allocation_cmd_val}:CW{codeword_cmd_val}:MODulation {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, allocation=repcap.Allocation.Default, codeword=repcap.Codeword.Default) -> enums.ModulationDl:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SUBFrame<sf>:ALLoc<al>[:CW<cw>]:MODulation \n
		Snippet: value: enums.ModulationDl = driver.applications.k10Xlte.configure.lte.downlink.cc.subframe.alloc.cw.modulation.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, allocation = repcap.Allocation.Default, codeword = repcap.Codeword.Default) \n
		This command selects the modulation of an allocation in a downlink subframe. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param codeword: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cw')
			:return: modulation: QPSK QPSK modulation QAM16 16QAM modulation QAM64 64QAM modulation QAM256 256QAM modulation Q1K 1024QAM modulation"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		codeword_cmd_val = self._cmd_group.get_repcap_cmd_value(codeword, repcap.Codeword)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc{allocation_cmd_val}:CW{codeword_cmd_val}:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationDl)
