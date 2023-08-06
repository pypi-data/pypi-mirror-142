from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: FETCh:FEPPm[:CC<cc>]:MINimum \n
		Snippet: value: float = driver.applications.k10Xlte.fetch.fePpm.cc.minimum.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command queries the carrier frequency error. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: frequency_error: Average, minimum or maximum frequency error, depending on the command syntax. Unit: ppm"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'FETCh:FEPPm:CC{carrierComponent_cmd_val}:MINimum?')
		return Conversions.str_to_float(response)
