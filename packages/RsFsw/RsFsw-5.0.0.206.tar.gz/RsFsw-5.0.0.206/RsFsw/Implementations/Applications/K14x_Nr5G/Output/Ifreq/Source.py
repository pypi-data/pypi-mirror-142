from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.IfSource, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<xxx>:IF[:SOURce] \n
		Snippet: driver.applications.k14Xnr5G.output.ifreq.source.set(source = enums.IfSource.HVIDeo, outputConnector = repcap.OutputConnector.Default) \n
		No command help available \n
			:param source: No help available
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.IfSource)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:IF:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, outputConnector=repcap.OutputConnector.Default) -> enums.IfSource:
		"""SCPI: OUTPut<xxx>:IF[:SOURce] \n
		Snippet: value: enums.IfSource = driver.applications.k14Xnr5G.output.ifreq.source.get(outputConnector = repcap.OutputConnector.Default) \n
		No command help available \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: source: No help available"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:IF:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.IfSource)
