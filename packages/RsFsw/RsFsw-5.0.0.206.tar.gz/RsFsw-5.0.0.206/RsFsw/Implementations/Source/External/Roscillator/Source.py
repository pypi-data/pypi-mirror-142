from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.ReferenceSourceB, externalRosc=repcap.ExternalRosc.Nr1) -> None:
		"""SCPI: SOURce:EXTernal<ext>:ROSCillator[:SOURce] \n
		Snippet: driver.source.external.roscillator.source.set(source = enums.ReferenceSourceB.EAUTo, externalRosc = repcap.ExternalRosc.Nr1) \n
		This command controls selection of the reference oscillator for the external generator. This command is only valid if
		External Generator Control (R&S FSW-B10) is installed. If the external reference oscillator is selected, the reference
		signal must be connected to the rear panel of the instrument. \n
			:param source: INTernal Uses the internal reference. EXTernal Uses the external reference; if none is available, an error flag is displayed in the status bar.
			:param externalRosc: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ReferenceSourceB)
		externalRosc_cmd_val = self._cmd_group.get_repcap_cmd_value(externalRosc, repcap.ExternalRosc)
		self._core.io.write(f'SOURce:EXTernal{externalRosc_cmd_val}:ROSCillator:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, externalRosc=repcap.ExternalRosc.Nr1) -> enums.ReferenceSourceB:
		"""SCPI: SOURce:EXTernal<ext>:ROSCillator[:SOURce] \n
		Snippet: value: enums.ReferenceSourceB = driver.source.external.roscillator.source.get(externalRosc = repcap.ExternalRosc.Nr1) \n
		This command controls selection of the reference oscillator for the external generator. This command is only valid if
		External Generator Control (R&S FSW-B10) is installed. If the external reference oscillator is selected, the reference
		signal must be connected to the rear panel of the instrument. \n
			:param externalRosc: optional repeated capability selector. Default value: Nr1
			:return: source: INTernal Uses the internal reference. EXTernal Uses the external reference; if none is available, an error flag is displayed in the status bar."""
		externalRosc_cmd_val = self._cmd_group.get_repcap_cmd_value(externalRosc, repcap.ExternalRosc)
		response = self._core.io.query_str(f'SOURce:EXTernal{externalRosc_cmd_val}:ROSCillator:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceSourceB)
