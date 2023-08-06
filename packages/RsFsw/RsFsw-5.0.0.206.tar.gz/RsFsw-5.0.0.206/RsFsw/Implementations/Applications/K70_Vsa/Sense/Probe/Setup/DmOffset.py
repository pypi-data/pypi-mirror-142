from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmOffset:
	"""DmOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmOffset", core, parent)

	def set(self, dm_offset: float, probe=repcap.Probe.Default) -> None:
		"""SCPI: [SENSe]:PROBe<pb>:SETup:DMOFfset \n
		Snippet: driver.applications.k70Vsa.sense.probe.setup.dmOffset.set(dm_offset = 1.0, probe = repcap.Probe.Default) \n
		Sets the DM-mode offset. The setting is only available if a modular probe in DM-mode is connected to the R&S FSW. If the
		probe is disconnected, the DM-mode offset of the probe is reset to 0.0 V. Note that if the offset for DM-mode or CM-mode
		is changed, the offsets for the P-mode and N-mode are adapted accordingly, and vice versa. For details see 'MultiMode
		Function and Offset Compensation for Modular RF Probes'. \n
			:param dm_offset: Voltage offset between the positive and negative input terminal Unit: V
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
		"""
		param = Conversions.decimal_value_to_str(dm_offset)
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		self._core.io.write(f'SENSe:PROBe{probe_cmd_val}:SETup:DMOFfset {param}')

	def get(self, probe=repcap.Probe.Default) -> float:
		"""SCPI: [SENSe]:PROBe<pb>:SETup:DMOFfset \n
		Snippet: value: float = driver.applications.k70Vsa.sense.probe.setup.dmOffset.get(probe = repcap.Probe.Default) \n
		Sets the DM-mode offset. The setting is only available if a modular probe in DM-mode is connected to the R&S FSW. If the
		probe is disconnected, the DM-mode offset of the probe is reset to 0.0 V. Note that if the offset for DM-mode or CM-mode
		is changed, the offsets for the P-mode and N-mode are adapted accordingly, and vice versa. For details see 'MultiMode
		Function and Offset Compensation for Modular RF Probes'. \n
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
			:return: dm_offset: Voltage offset between the positive and negative input terminal Unit: V"""
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		response = self._core.io.query_str(f'SENSe:PROBe{probe_cmd_val}:SETup:DMOFfset?')
		return Conversions.str_to_float(response)
