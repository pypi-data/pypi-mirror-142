from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def get(self, carrierComponent=repcap.CarrierComponent.Default, antenna=repcap.Antenna.Default) -> float:
		"""SCPI: FETCh:TAERror[:CC<cc>]:ANTenna<ant>[:AVERage] \n
		Snippet: value: float = driver.applications.k10Xlte.fetch.taError.cc.antenna.average.get(carrierComponent = repcap.CarrierComponent.Default, antenna = repcap.Antenna.Default) \n
		This command queries the time alignment error. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: tae: Minimum, maximum or average time alignment error, depending on the last command syntax element. Unit: s"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'FETCh:TAERror:CC{carrierComponent_cmd_val}:ANTenna{antenna_cmd_val}:AVERage?')
		return Conversions.str_to_float(response)
