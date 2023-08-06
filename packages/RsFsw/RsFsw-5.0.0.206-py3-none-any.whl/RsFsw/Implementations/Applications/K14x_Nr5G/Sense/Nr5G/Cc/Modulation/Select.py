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

	def set(self, modulation: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: [SENSe]:NR5G[:CC<cc>]:MODulation:SELect \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.cc.modulation.select.set(modulation = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command filters the displayed results in the constellation diagram by a certain modulation type. \n
			:param modulation: ALL Shows the results for all modulation types. numeric value (integer only) Shows the results for a single modulation type. Modulation types are mapped to numeric values. For the code assignment, see 'Return value codes'.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(modulation)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'SENSe:NR5G:CC{carrierComponent_cmd_val}:MODulation:SELect {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: [SENSe]:NR5G[:CC<cc>]:MODulation:SELect \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.cc.modulation.select.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command filters the displayed results in the constellation diagram by a certain modulation type. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: modulation: ALL Shows the results for all modulation types. numeric value (integer only) Shows the results for a single modulation type. Modulation types are mapped to numeric values. For the code assignment, see 'Return value codes'."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'SENSe:NR5G:CC{carrierComponent_cmd_val}:MODulation:SELect?')
		return Conversions.str_to_float(response)
