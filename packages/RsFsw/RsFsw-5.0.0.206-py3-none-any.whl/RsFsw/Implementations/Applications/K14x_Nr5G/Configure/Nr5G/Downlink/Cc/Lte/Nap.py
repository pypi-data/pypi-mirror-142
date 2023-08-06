from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nap:
	"""Nap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nap", core, parent)

	def set(self, aps: enums.AntennaPorts, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:LTE:NAP \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.lte.nap.set(aps = enums.AntennaPorts.AP1, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the number of antenna ports for an LTE signal.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Lte.State.set) . \n
			:param aps: AP1 | AP2 | AP4 1-, 2-, or 4 antenna port configurations.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(aps, enums.AntennaPorts)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:LTE:NAP {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.AntennaPorts:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:LTE:NAP \n
		Snippet: value: enums.AntennaPorts = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.lte.nap.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the number of antenna ports for an LTE signal.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Lte.State.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: aps: AP1 | AP2 | AP4 1-, 2-, or 4 antenna port configurations."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:LTE:NAP?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaPorts)
