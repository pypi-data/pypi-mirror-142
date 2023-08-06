from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Detection:
	"""Detection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("detection", core, parent)

	def set(self, detection: enums.AutoManualMode, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PLC:DETection \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.plc.detection.set(detection = enums.AutoManualMode.AUTO, carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns automatic detection of the cell ID on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on auto demodulation (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Detection.set) .
			- Turn on transform precoding (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Tprecoding.set) . \n
			:param detection: AUTO Auto detection of cell ID. MANual Manual entry of cell ID (method RsFsw.Applications.K10x_Lte.Configure.Lte.Uplink.Cc.Plc.Cid.set) .
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(detection, enums.AutoManualMode)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PLC:DETection {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.AutoManualMode:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PLC:DETection \n
		Snippet: value: enums.AutoManualMode = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.plc.detection.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns automatic detection of the cell ID on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on auto demodulation (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Detection.set) .
			- Turn on transform precoding (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Tprecoding.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: detection: AUTO Auto detection of cell ID. MANual Manual entry of cell ID (method RsFsw.Applications.K10x_Lte.Configure.Lte.Uplink.Cc.Plc.Cid.set) ."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PLC:DETection?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
