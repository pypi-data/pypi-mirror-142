from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pmode:
	"""Pmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmode", core, parent)

	def set(self, mode: enums.ProbeMode, probe=repcap.Probe.Default) -> None:
		"""SCPI: [SENSe]:PROBe<pb>:SETup:PMODe \n
		Snippet: driver.applications.k70Vsa.sense.probe.setup.pmode.set(mode = enums.ProbeMode.CM, probe = repcap.Probe.Default) \n
		Determines the mode of a multi-mode modular probe. For details see 'MultiMode Function and Offset Compensation for
		Modular RF Probes'. \n
			:param mode: CM | DM | PM | NM DM Voltage between the positive and negative input terminal CM Mean voltage between the positive and negative input terminal vs. ground PM Voltage between the positive input terminal and ground NM Voltage between the negative input terminal and ground
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ProbeMode)
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		self._core.io.write(f'SENSe:PROBe{probe_cmd_val}:SETup:PMODe {param}')

	# noinspection PyTypeChecker
	def get(self, probe=repcap.Probe.Default) -> enums.ProbeMode:
		"""SCPI: [SENSe]:PROBe<pb>:SETup:PMODe \n
		Snippet: value: enums.ProbeMode = driver.applications.k70Vsa.sense.probe.setup.pmode.get(probe = repcap.Probe.Default) \n
		Determines the mode of a multi-mode modular probe. For details see 'MultiMode Function and Offset Compensation for
		Modular RF Probes'. \n
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
			:return: mode: CM | DM | PM | NM DM Voltage between the positive and negative input terminal CM Mean voltage between the positive and negative input terminal vs. ground PM Voltage between the positive input terminal and ground NM Voltage between the negative input terminal and ground"""
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		response = self._core.io.query_str(f'SENSe:PROBe{probe_cmd_val}:SETup:PMODe?')
		return Conversions.str_to_scalar_enum(response, enums.ProbeMode)
