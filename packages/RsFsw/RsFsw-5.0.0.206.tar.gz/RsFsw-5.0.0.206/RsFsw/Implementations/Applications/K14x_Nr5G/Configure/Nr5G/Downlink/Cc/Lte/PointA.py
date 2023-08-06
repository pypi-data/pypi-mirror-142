from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PointA:
	"""PointA commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pointA", core, parent)

	def set(self, offset: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:LTE:POINta \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.lte.pointA.set(offset = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines an LTE carrier offset relative to reference point A (in terms of resource blocks) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Lte.State.set) . \n
			:param offset: Component Carrier
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:LTE:POINta {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:LTE:POINta \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.lte.pointA.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines an LTE carrier offset relative to reference point A (in terms of resource blocks) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Lte.State.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: offset: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:LTE:POINta?')
		return Conversions.str_to_float(response)
