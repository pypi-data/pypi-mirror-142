from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, antenna: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: [SENSe][:LTE][:CC<cc>]:ANTenna:SELect \n
		Snippet: driver.applications.k10Xlte.sense.lte.cc.antenna.select.set(antenna = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		No command help available \n
			:param antenna: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(antenna)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'SENSe:LTE:CC{carrierComponent_cmd_val}:ANTenna:SELect {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: [SENSe][:LTE][:CC<cc>]:ANTenna:SELect \n
		Snippet: value: float = driver.applications.k10Xlte.sense.lte.cc.antenna.select.get(carrierComponent = repcap.CarrierComponent.Default) \n
		No command help available \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: antenna: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'SENSe:LTE:CC{carrierComponent_cmd_val}:ANTenna:SELect?')
		return Conversions.str_to_float(response)
