from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Oband:
	"""Oband commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oband", core, parent)

	def set(self, no_of_subbands: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: [SENSe][:LTE][:CC<cc>]:SFLatness:OBANd \n
		Snippet: driver.applications.k10Xlte.sense.lte.cc.sflatness.oband.set(no_of_subbands = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the operating band for spectrum flatness measurements. \n
			:param no_of_subbands: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(no_of_subbands)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'SENSe:LTE:CC{carrierComponent_cmd_val}:SFLatness:OBANd {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: [SENSe][:LTE][:CC<cc>]:SFLatness:OBANd \n
		Snippet: value: float = driver.applications.k10Xlte.sense.lte.cc.sflatness.oband.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the operating band for spectrum flatness measurements. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: no_of_subbands: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'SENSe:LTE:CC{carrierComponent_cmd_val}:SFLatness:OBANd?')
		return Conversions.str_to_float(response)
