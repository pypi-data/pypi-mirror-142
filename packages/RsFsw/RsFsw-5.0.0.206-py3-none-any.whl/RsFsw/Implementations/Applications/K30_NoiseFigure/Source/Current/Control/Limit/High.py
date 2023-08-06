from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class High:
	"""High commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("high", core, parent)

	def get(self, source=repcap.Source.Default) -> float:
		"""SCPI: SOURce:CURRent:CONTrol<i>:LIMit:HIGH \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.current.control.limit.high.get(source = repcap.Source.Default) \n
		No command help available \n
			:param source: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Control')
			:return: current: No help available"""
		source_cmd_val = self._cmd_group.get_repcap_cmd_value(source, repcap.Source)
		response = self._core.io.query_str(f'SOURce:CURRent:CONTrol{source_cmd_val}:LIMit:HIGH?')
		return Conversions.str_to_float(response)
