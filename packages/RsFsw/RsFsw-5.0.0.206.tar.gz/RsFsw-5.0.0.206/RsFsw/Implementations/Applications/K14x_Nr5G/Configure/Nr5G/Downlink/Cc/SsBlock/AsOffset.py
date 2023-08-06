from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AsOffset:
	"""AsOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("asOffset", core, parent)

	def set(self, offset: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:ASOFfset \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.asOffset.set(offset = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines a frequency offset for the synchronization signal block.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select manual configuration mode for SS (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.SsBlock.Detection.set) . \n
			:param offset: numeric value (integer only) Offset in terms of subcarrier, relative to the first subcarrier of a resource block. Range: 0 to 11
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:ASOFfset {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:ASOFfset \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.asOffset.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines a frequency offset for the synchronization signal block.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select manual configuration mode for SS (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.SsBlock.Detection.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: offset: numeric value (integer only) Offset in terms of subcarrier, relative to the first subcarrier of a resource block. Range: 0 to 11"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:ASOFfset?')
		return Conversions.str_to_float(response)
