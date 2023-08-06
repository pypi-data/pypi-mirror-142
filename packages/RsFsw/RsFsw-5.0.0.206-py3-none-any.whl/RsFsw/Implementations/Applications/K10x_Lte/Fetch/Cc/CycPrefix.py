from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CycPrefix:
	"""CycPrefix commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cycPrefix", core, parent)

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.CycPrefixType:
		"""SCPI: FETCh[:CC<cc>]:CYCPrefix \n
		Snippet: value: enums.CycPrefixType = driver.applications.k10Xlte.fetch.cc.cycPrefix.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command queries the cyclic prefix type that has been detected. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: prefix_type: The command returns -1 if no valid result has been detected yet. NORM Normal cyclic prefix length detected EXT Extended cyclic prefix length detected"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'FETCh:CC{carrierComponent_cmd_val}:CYCPrefix?')
		return Conversions.str_to_scalar_enum(response, enums.CycPrefixType)
