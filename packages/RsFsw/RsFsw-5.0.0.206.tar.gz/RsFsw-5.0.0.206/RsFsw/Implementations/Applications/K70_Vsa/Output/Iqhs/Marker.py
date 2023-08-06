from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Marker:
	"""Marker commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("marker", core, parent)

	def set(self, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<up>:IQHS:MARKer \n
		Snippet: driver.applications.k70Vsa.output.iqhs.marker.set(outputConnector = repcap.OutputConnector.Default) \n
		Inserts marker information to the data stream during a running I/Q data output recording. Useful to mark a specific event
		during the measurement that you detect in the result window, for example. Then you can search for the marker information
		in the output data to analyze the effects at that time. For details on Digital I/Q 40G Streaming Output (R&S
		FSW-B517/-B1017) , see 'Digital I/Q 40G Streaming Output'. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:IQHS:MARKer')

	def set_with_opc(self, outputConnector=repcap.OutputConnector.Default, opc_timeout_ms: int = -1) -> None:
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		"""SCPI: OUTPut<up>:IQHS:MARKer \n
		Snippet: driver.applications.k70Vsa.output.iqhs.marker.set_with_opc(outputConnector = repcap.OutputConnector.Default) \n
		Inserts marker information to the data stream during a running I/Q data output recording. Useful to mark a specific event
		during the measurement that you detect in the result window, for example. Then you can search for the marker information
		in the output data to analyze the effects at that time. For details on Digital I/Q 40G Streaming Output (R&S
		FSW-B517/-B1017) , see 'Digital I/Q 40G Streaming Output'. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'OUTPut{outputConnector_cmd_val}:IQHS:MARKer', opc_timeout_ms)
