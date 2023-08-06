from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, slot: enums.CcSlot, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: [SENSe][:LTE][:CC<cc>]:SLOT:SELect \n
		Snippet: driver.applications.k10Xlte.sense.lte.cc.slot.select.set(slot = enums.CcSlot.ALL, carrierComponent = repcap.CarrierComponent.Default) \n
		This command filters the results in the constellation diagram by a particular slot. \n
			:param slot: S0 Slot 0 S1 Slot 1 ALL Both slots
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(slot, enums.CcSlot)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'SENSe:LTE:CC{carrierComponent_cmd_val}:SLOT:SELect {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.CcSlot:
		"""SCPI: [SENSe][:LTE][:CC<cc>]:SLOT:SELect \n
		Snippet: value: enums.CcSlot = driver.applications.k10Xlte.sense.lte.cc.slot.select.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command filters the results in the constellation diagram by a particular slot. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: slot: S0 Slot 0 S1 Slot 1 ALL Both slots"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'SENSe:LTE:CC{carrierComponent_cmd_val}:SLOT:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.CcSlot)
