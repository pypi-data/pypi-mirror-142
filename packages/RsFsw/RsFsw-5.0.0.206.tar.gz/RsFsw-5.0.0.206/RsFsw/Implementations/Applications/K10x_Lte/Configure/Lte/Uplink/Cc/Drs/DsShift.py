from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DsShift:
	"""DsShift commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dsShift", core, parent)

	def set(self, shift: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:DRS:DSSHift \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.drs.dsShift.set(shift = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the delta sequence shift of the uplink signal. \n
			:param shift: numeric value (integer only)
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(shift)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:DRS:DSSHift {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:DRS:DSSHift \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.drs.dsShift.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the delta sequence shift of the uplink signal. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: shift: numeric value (integer only)"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:DRS:DSSHift?')
		return Conversions.str_to_float(response)
