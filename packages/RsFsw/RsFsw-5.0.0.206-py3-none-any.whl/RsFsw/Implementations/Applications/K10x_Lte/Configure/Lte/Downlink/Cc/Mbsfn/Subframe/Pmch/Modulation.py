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

	def set(self, modulation: enums.ModulationDl, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:MBSFn:SUBFrame<sf>:PMCH:MODulation \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.mbsfn.subframe.pmch.modulation.set(modulation = enums.ModulationDl.Q1K, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		This command selects the modulation type for an MBSFN subframe. \n
			:param modulation: QPSK | QAM16 | QAM64 | QAM256 | Q1K
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
		"""
		param = Conversions.enum_scalar_to_str(modulation, enums.ModulationDl)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:MBSFn:SUBFrame{subframe_cmd_val}:PMCH:MODulation {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> enums.ModulationDl:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:MBSFn:SUBFrame<sf>:PMCH:MODulation \n
		Snippet: value: enums.ModulationDl = driver.applications.k10Xlte.configure.lte.downlink.cc.mbsfn.subframe.pmch.modulation.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		This command selects the modulation type for an MBSFN subframe. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:return: modulation: QPSK | QAM16 | QAM64 | QAM256 | Q1K"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:MBSFn:SUBFrame{subframe_cmd_val}:PMCH:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationDl)
