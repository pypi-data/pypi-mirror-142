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

	def set(self, source: enums.Source, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<up>:IF[:SOURce] \n
		Snippet: driver.applications.k70Vsa.output.ifreq.source.set(source = enums.Source.AM, outputConnector = repcap.OutputConnector.Default) \n
		Defines the type of signal available at one of the output connectors of the R&S FSW. \n
			:param source: IF The measured IF value is available at the IF/VIDEO/DEMOD output connector. IF2 The measured IF value is available at the 'IF OUT 2 GHz/ IF OUT 5 GHz' output connector at a frequency of 2 GHz. This setting is only available if the 'IF OUT 2 GHz/ IF OUT 5 GHz' connector or the optional 2 GHz / 5 GHz bandwidth extension (R&S FSW-B2000/B5000) is available. It is automatically set if the optional 2 GHz / 5 GHz bandwidth extension (R&S FSW-B2000/B5000) is installed and active. For details see 'Basics on the 2 GHz Bandwidth Extension (R&S FSW-B2000 Option) '. VIDeo The displayed video signal (i.e. the filtered and detected IF signal, 200mV) is available at the IF/VIDEO/DEMOD output connector. This setting is required to provide demodulated audio frequencies at the output.
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.Source)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:IF:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, outputConnector=repcap.OutputConnector.Default) -> enums.Source:
		"""SCPI: OUTPut<up>:IF[:SOURce] \n
		Snippet: value: enums.Source = driver.applications.k70Vsa.output.ifreq.source.get(outputConnector = repcap.OutputConnector.Default) \n
		Defines the type of signal available at one of the output connectors of the R&S FSW. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: source: IF The measured IF value is available at the IF/VIDEO/DEMOD output connector. IF2 The measured IF value is available at the 'IF OUT 2 GHz/ IF OUT 5 GHz' output connector at a frequency of 2 GHz. This setting is only available if the 'IF OUT 2 GHz/ IF OUT 5 GHz' connector or the optional 2 GHz / 5 GHz bandwidth extension (R&S FSW-B2000/B5000) is available. It is automatically set if the optional 2 GHz / 5 GHz bandwidth extension (R&S FSW-B2000/B5000) is installed and active. For details see 'Basics on the 2 GHz Bandwidth Extension (R&S FSW-B2000 Option) '. VIDeo The displayed video signal (i.e. the filtered and detected IF signal, 200mV) is available at the IF/VIDEO/DEMOD output connector. This setting is required to provide demodulated audio frequencies at the output."""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:IF:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.Source)
