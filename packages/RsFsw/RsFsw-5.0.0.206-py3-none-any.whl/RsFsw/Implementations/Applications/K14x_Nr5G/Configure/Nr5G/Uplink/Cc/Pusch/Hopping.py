from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hopping:
	"""Hopping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hopping", core, parent)

	def set(self, mode: enums.HoppingMode, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PUSCh:HOPPing \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.pusch.hopping.set(mode = enums.HoppingMode.GROup, carrierComponent = repcap.CarrierComponent.Default) \n
		This command Selects a hopping mode for the PUSCH DMRS sequence. \n
			:param mode: GROup Selects group hopping. NONE Selects no hopping. SEQuence Selects sequence hopping.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.HoppingMode)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PUSCh:HOPPing {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.HoppingMode:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PUSCh:HOPPing \n
		Snippet: value: enums.HoppingMode = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.pusch.hopping.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command Selects a hopping mode for the PUSCH DMRS sequence. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: mode: GROup Selects group hopping. NONE Selects no hopping. SEQuence Selects sequence hopping."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PUSCh:HOPPing?')
		return Conversions.str_to_scalar_enum(response, enums.HoppingMode)
