from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AttRatio:
	"""AttRatio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attRatio", core, parent)

	def set(self, attenuation_ratio: float, probe=repcap.Probe.Default) -> None:
		"""SCPI: [SENSe]:PROBe<pb>:SETup:ATTRatio \n
		Snippet: driver.applications.k70Vsa.sense.probe.setup.attRatio.set(attenuation_ratio = 1.0, probe = repcap.Probe.Default) \n
		Defines the attenuation applied to the input at the probe. This setting is only available for modular probes. \n
			:param attenuation_ratio: 10 Attenuation by 20 dB (ratio= 10:1) 2 Attenuation by 6 dB (ratio= 2:1) Unit: DB
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
		"""
		param = Conversions.decimal_value_to_str(attenuation_ratio)
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		self._core.io.write(f'SENSe:PROBe{probe_cmd_val}:SETup:ATTRatio {param}')

	def get(self, probe=repcap.Probe.Default) -> float:
		"""SCPI: [SENSe]:PROBe<pb>:SETup:ATTRatio \n
		Snippet: value: float = driver.applications.k70Vsa.sense.probe.setup.attRatio.get(probe = repcap.Probe.Default) \n
		Defines the attenuation applied to the input at the probe. This setting is only available for modular probes. \n
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
			:return: attenuation_ratio: 10 Attenuation by 20 dB (ratio= 10:1) 2 Attenuation by 6 dB (ratio= 2:1) Unit: DB"""
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		response = self._core.io.query_str(f'SENSe:PROBe{probe_cmd_val}:SETup:ATTRatio?')
		return Conversions.str_to_float(response)
