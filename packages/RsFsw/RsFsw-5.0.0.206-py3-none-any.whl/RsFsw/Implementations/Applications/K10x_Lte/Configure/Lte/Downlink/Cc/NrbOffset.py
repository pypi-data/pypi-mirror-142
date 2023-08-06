from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrbOffset:
	"""NrbOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nrbOffset", core, parent)

	def set(self, arg_0: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:NRBoffset \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.nrbOffset.set(arg_0 = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines an the location of the NB-IoT signal within the LTE carrier as a resource block offset.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on exclusion of inband NB-IoT (method RsFsw.Applications.K10x_Lte.Configure.Lte.Downlink.Cc.EiNbIot.State.set) . \n
			:param arg_0: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:NRBoffset {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:NRBoffset \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.nrbOffset.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines an the location of the NB-IoT signal within the LTE carrier as a resource block offset.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on exclusion of inband NB-IoT (method RsFsw.Applications.K10x_Lte.Configure.Lte.Downlink.Cc.EiNbIot.State.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: arg_0: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:NRBoffset?')
		return Conversions.str_to_float(response)
