from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NmOffset:
	"""NmOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nmOffset", core, parent)

	def set(self, nm_offset: float, probe=repcap.Probe.Default) -> None:
		"""SCPI: [SENSe]:PROBe<pb>:SETup:NMOFfset \n
		Snippet: driver.sense.probe.setup.nmOffset.set(nm_offset = 1.0, probe = repcap.Probe.Default) \n
		Sets the N-mode offset. The setting is only available if a modular probe in N-mode is connected to the R&S FSW.
		The maximum voltage difference between the positive and negative input terminals is 16 V. If the probe is disconnected,
		the N-mode offset of the probe is reset to 0.0 V. Note that if the offset for DM-mode or CM-mode is changed, the offsets
		for the P-mode and N-mode are adapted accordingly, and vice versa. For details see 'Multimode function and offset
		compensation for modular RF probes'. \n
			:param nm_offset: The voltage offset between the negative input terminal and ground. Unit: V
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
		"""
		param = Conversions.decimal_value_to_str(nm_offset)
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		self._core.io.write(f'SENSe:PROBe{probe_cmd_val}:SETup:NMOFfset {param}')

	def get(self, probe=repcap.Probe.Default) -> float:
		"""SCPI: [SENSe]:PROBe<pb>:SETup:NMOFfset \n
		Snippet: value: float = driver.sense.probe.setup.nmOffset.get(probe = repcap.Probe.Default) \n
		Sets the N-mode offset. The setting is only available if a modular probe in N-mode is connected to the R&S FSW.
		The maximum voltage difference between the positive and negative input terminals is 16 V. If the probe is disconnected,
		the N-mode offset of the probe is reset to 0.0 V. Note that if the offset for DM-mode or CM-mode is changed, the offsets
		for the P-mode and N-mode are adapted accordingly, and vice versa. For details see 'Multimode function and offset
		compensation for modular RF probes'. \n
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
			:return: nm_offset: The voltage offset between the negative input terminal and ground. Unit: V"""
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		response = self._core.io.query_str(f'SENSe:PROBe{probe_cmd_val}:SETup:NMOFfset?')
		return Conversions.str_to_float(response)
