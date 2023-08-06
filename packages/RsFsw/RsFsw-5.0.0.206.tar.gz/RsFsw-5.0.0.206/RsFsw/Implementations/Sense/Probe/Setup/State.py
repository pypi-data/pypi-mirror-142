from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def get(self, probe=repcap.Probe.Default) -> float:
		"""SCPI: [SENSe]:PROBe<pb>:SETup:STATe \n
		Snippet: value: float = driver.sense.probe.setup.state.get(probe = repcap.Probe.Default) \n
		Queries if the probe at the specified connector is active (detected) or not active (not detected) . To switch the probe
		on, i.e. activate input from the connector, use INP:SEL:AIQ (see method RsFsw.Applications.K10x_Lte.InputPy.Select.set) . \n
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
			:return: state: DETected | NDETected"""
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		response = self._core.io.query_str(f'SENSe:PROBe{probe_cmd_val}:SETup:STATe?')
		return Conversions.str_to_float(response)
