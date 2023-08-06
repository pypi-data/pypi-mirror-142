from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, format_py: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PRACh:FORMat \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.prach.formatPy.set(format_py = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PRACH format. \n
			:param format_py: 0 | 1 | 2 | 3 | A1 | A2 | A3 | B1 | B2 | B3 | B4 | C0 | C2
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(format_py)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PRACh:FORMat {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PRACh:FORMat \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.prach.formatPy.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PRACH format. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: format_py: 0 | 1 | 2 | 3 | A1 | A2 | A3 | B1 | B2 | B3 | B4 | C0 | C2"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PRACh:FORMat?')
		return Conversions.str_to_float(response)
