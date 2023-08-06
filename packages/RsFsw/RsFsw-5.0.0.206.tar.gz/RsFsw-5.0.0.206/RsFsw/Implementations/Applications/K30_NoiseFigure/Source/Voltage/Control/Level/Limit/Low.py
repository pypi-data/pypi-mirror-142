from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Low:
	"""Low commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("low", core, parent)

	def set(self, voltage: float, source=repcap.Source.Default) -> None:
		"""SCPI: SOURce:VOLTage:CONTrol<i>:LEVel:LIMit:LOW \n
		Snippet: driver.applications.k30NoiseFigure.source.voltage.control.level.limit.low.set(voltage = 1.0, source = repcap.Source.Default) \n
		No command help available \n
			:param voltage: No help available
			:param source: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Control')
		"""
		param = Conversions.decimal_value_to_str(voltage)
		source_cmd_val = self._cmd_group.get_repcap_cmd_value(source, repcap.Source)
		self._core.io.write(f'SOURce:VOLTage:CONTrol{source_cmd_val}:LEVel:LIMit:LOW {param}')

	def get(self, source=repcap.Source.Default) -> float:
		"""SCPI: SOURce:VOLTage:CONTrol<i>:LEVel:LIMit:LOW \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.voltage.control.level.limit.low.get(source = repcap.Source.Default) \n
		No command help available \n
			:param source: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Control')
			:return: voltage: No help available"""
		source_cmd_val = self._cmd_group.get_repcap_cmd_value(source, repcap.Source)
		response = self._core.io.query_str(f'SOURce:VOLTage:CONTrol{source_cmd_val}:LEVel:LIMit:LOW?')
		return Conversions.str_to_float(response)
