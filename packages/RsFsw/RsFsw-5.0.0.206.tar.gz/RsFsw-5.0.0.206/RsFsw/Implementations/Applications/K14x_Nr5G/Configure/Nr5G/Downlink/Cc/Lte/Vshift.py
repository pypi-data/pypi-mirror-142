from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vshift:
	"""Vshift commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vshift", core, parent)

	def set(self, value: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:LTE:VSHift \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.lte.vshift.set(value = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the vShift parameter for an LTE signal.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Lte.State.set) . \n
			:param value: Component Carrier
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(value)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:LTE:VSHift {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:LTE:VSHift \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.lte.vshift.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the vShift parameter for an LTE signal.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Lte.State.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: value: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:LTE:VSHift?')
		return Conversions.str_to_float(response)
