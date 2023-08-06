from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rset:
	"""Rset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rset", core, parent)

	def set(self, type_py: enums.RestrictedPrachSet, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PRACh:RSET \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.prach.rset.set(type_py = enums.RestrictedPrachSet.A, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the restricted set for the PRACH. \n
			:param type_py: NONE | A | B Restricted sets Type A and Type B are only supported by PRACH formats 0 to 3 (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Prach.FormatPy.set) .
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.RestrictedPrachSet)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PRACh:RSET {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.RestrictedPrachSet:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PRACh:RSET \n
		Snippet: value: enums.RestrictedPrachSet = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.prach.rset.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the restricted set for the PRACH. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: type_py: NONE | A | B Restricted sets Type A and Type B are only supported by PRACH formats 0 to 3 (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Prach.FormatPy.set) ."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PRACh:RSET?')
		return Conversions.str_to_scalar_enum(response, enums.RestrictedPrachSet)
