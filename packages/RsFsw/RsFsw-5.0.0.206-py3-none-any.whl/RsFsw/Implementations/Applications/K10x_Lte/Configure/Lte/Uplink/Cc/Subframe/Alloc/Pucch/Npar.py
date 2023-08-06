from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Npar:
	"""Npar commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npar", core, parent)

	def set(self, configuration: float, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc:PUCCh:NPAR \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.pucch.npar.set(configuration = 1.0, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		This command defines N_PUCCH on a subframe basis. The command is available if method RsFsw.Applications.K10x_Lte.
		Configure.Lte.Uplink.Cc.Pucch.Npar.set is turned on. \n
			:param configuration: numeric value
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
		"""
		param = Conversions.decimal_value_to_str(configuration)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:PUCCh:NPAR {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc:PUCCh:NPAR \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.pucch.npar.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		This command defines N_PUCCH on a subframe basis. The command is available if method RsFsw.Applications.K10x_Lte.
		Configure.Lte.Uplink.Cc.Pucch.Npar.set is turned on. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:return: configuration: numeric value"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:PUCCh:NPAR?')
		return Conversions.str_to_float(response)
