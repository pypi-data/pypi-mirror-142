from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeShift:
	"""DeShift commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("deShift", core, parent)

	def set(self, shift: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUCCh:DESHift \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.pucch.deShift.set(shift = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the delta shift of the PUCCH. \n
			:param shift: numeric value Range: 1 to 3
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(shift)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUCCh:DESHift {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUCCh:DESHift \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.pucch.deShift.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the delta shift of the PUCCH. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: shift: numeric value Range: 1 to 3"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUCCh:DESHift?')
		return Conversions.str_to_float(response)
