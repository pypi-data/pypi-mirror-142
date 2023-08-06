from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rap:
	"""Rap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rap", core, parent)

	def set(self, port: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: [SENSe]:NR5G[:CC<cc>]:RAP \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.cc.rap.set(port = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the reference antenna port for relative beamforming results. \n
			:param port: Value corresponds to the antenna port.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(port)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'SENSe:NR5G:CC{carrierComponent_cmd_val}:RAP {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: [SENSe]:NR5G[:CC<cc>]:RAP \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.cc.rap.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the reference antenna port for relative beamforming results. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: port: Value corresponds to the antenna port."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'SENSe:NR5G:CC{carrierComponent_cmd_val}:RAP?')
		return Conversions.str_to_float(response)
