from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pclass:
	"""Pclass commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pclass", core, parent)

	def set(self, power_class: enums.PowerClassB, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PLC:PCLass \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.plc.pclass.set(power_class = enums.PowerClassB.PC1, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the power class to select the appropriate inband emission limits.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select FR2 deployment (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.DfRange.set) . \n
			:param power_class: PC1 | PC2 | PC3 | PC4
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(power_class, enums.PowerClassB)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PLC:PCLass {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.PowerClassB:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PLC:PCLass \n
		Snippet: value: enums.PowerClassB = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.plc.pclass.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the power class to select the appropriate inband emission limits.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select FR2 deployment (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.DfRange.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: power_class: PC1 | PC2 | PC3 | PC4"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PLC:PCLass?')
		return Conversions.str_to_scalar_enum(response, enums.PowerClassB)
