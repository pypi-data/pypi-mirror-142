from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trp:
	"""Trp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trp", core, parent)

	def set(self, power: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:PLC:TRP \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.plc.trp.set(power = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the base station output power for limit selection (Prated, c, TRP) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select FR2 deployment (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.DfRange.set) . \n
			:param power: Unit: dBm
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(power)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:PLC:TRP {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:PLC:TRP \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.plc.trp.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the base station output power for limit selection (Prated, c, TRP) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select FR2 deployment (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.DfRange.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: power: Unit: dBm"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:PLC:TRP?')
		return Conversions.str_to_float(response)
