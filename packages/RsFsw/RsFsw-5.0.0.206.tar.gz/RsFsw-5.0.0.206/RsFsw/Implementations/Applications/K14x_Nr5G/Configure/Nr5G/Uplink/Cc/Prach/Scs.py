from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scs:
	"""Scs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scs", core, parent)

	def set(self, subcarrier_spacing: enums.SubCarrSpacingPrach, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PRACh:SCS \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.prach.scs.set(subcarrier_spacing = enums.SubCarrSpacingPrach.SS1_25, carrierComponent = repcap.CarrierComponent.Default) \n
		This command select the subcarrier spacing of the PRACH. \n
			:param subcarrier_spacing: SS1_25 | SS5 | SS15 | SS30 | SS60 | SS120 The availability of subcarrier spacings depends on the selected deployment and PRACH format (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.DfRange.set and method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Prach.FormatPy.set) .
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(subcarrier_spacing, enums.SubCarrSpacingPrach)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PRACh:SCS {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.SubCarrSpacingPrach:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PRACh:SCS \n
		Snippet: value: enums.SubCarrSpacingPrach = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.prach.scs.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command select the subcarrier spacing of the PRACH. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: subcarrier_spacing: SS1_25 | SS5 | SS15 | SS30 | SS60 | SS120 The availability of subcarrier spacings depends on the selected deployment and PRACH format (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.DfRange.set and method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Prach.FormatPy.set) ."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PRACh:SCS?')
		return Conversions.str_to_scalar_enum(response, enums.SubCarrSpacingPrach)
