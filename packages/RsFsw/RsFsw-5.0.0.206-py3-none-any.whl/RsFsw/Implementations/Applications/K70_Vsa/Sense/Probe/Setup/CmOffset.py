from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CmOffset:
	"""CmOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmOffset", core, parent)

	def set(self, cm_offset: float, probe=repcap.Probe.Default) -> None:
		"""SCPI: [SENSe]:PROBe<p>:SETup:CMOFfset \n
		Snippet: driver.applications.k70Vsa.sense.probe.setup.cmOffset.set(cm_offset = 1.0, probe = repcap.Probe.Default) \n
		Sets the common mode offset. The setting is only available if a differential probe in CM-mode is connected to the R&S FSW.
		If the probe is disconnected, the common mode offset of the probe is reset to 0.0 V. Note that if the offset for DM-mode
		or CM-mode is changed, the offsets for the P-mode and N-mode are adapted accordingly, and vice versa. For details see
		'Common Mode Offset (for Differential Probes) ' or 'MultiMode Function and Offset Compensation for Modular RF Probes'. \n
			:param cm_offset: Offset of the mean voltage between the positive and negative input terminal vs. ground Range: -16 V to +16 V, Unit: V
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
		"""
		param = Conversions.decimal_value_to_str(cm_offset)
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		self._core.io.write(f'SENSe:PROBe{probe_cmd_val}:SETup:CMOFfset {param}')

	def get(self, probe=repcap.Probe.Default) -> float:
		"""SCPI: [SENSe]:PROBe<p>:SETup:CMOFfset \n
		Snippet: value: float = driver.applications.k70Vsa.sense.probe.setup.cmOffset.get(probe = repcap.Probe.Default) \n
		Sets the common mode offset. The setting is only available if a differential probe in CM-mode is connected to the R&S FSW.
		If the probe is disconnected, the common mode offset of the probe is reset to 0.0 V. Note that if the offset for DM-mode
		or CM-mode is changed, the offsets for the P-mode and N-mode are adapted accordingly, and vice versa. For details see
		'Common Mode Offset (for Differential Probes) ' or 'MultiMode Function and Offset Compensation for Modular RF Probes'. \n
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
			:return: cm_offset: Offset of the mean voltage between the positive and negative input terminal vs. ground Range: -16 V to +16 V, Unit: V"""
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		response = self._core.io.query_str(f'SENSe:PROBe{probe_cmd_val}:SETup:CMOFfset?')
		return Conversions.str_to_float(response)
