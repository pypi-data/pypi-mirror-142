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
		Snippet: driver.applications.k30NoiseFigure.sense.probe.setup.pmode.set(mode = enums.ProbeMode.CM, probe = repcap.Probe.Default) \n
		No command help available \n
			:param mode: No help available
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ProbeMode)
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		self._core.io.write(f'SENSe:PROBe{probe_cmd_val}:SETup:PMODe {param}')

	# noinspection PyTypeChecker
	def get(self, probe=repcap.Probe.Default) -> enums.ProbeMode:
		"""SCPI: [SENSe]:PROBe<pb>:SETup:PMODe \n
		Snippet: value: enums.ProbeMode = driver.applications.k30NoiseFigure.sense.probe.setup.pmode.get(probe = repcap.Probe.Default) \n
		No command help available \n
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
			:return: mode: No help available"""
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		response = self._core.io.query_str(f'SENSe:PROBe{probe_cmd_val}:SETup:PMODe?')
		return Conversions.str_to_scalar_enum(response, enums.ProbeMode)
