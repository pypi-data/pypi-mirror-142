from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, coupling: enums.CouplingAmplitude) -> None:
		"""SCPI: CONFigure:WLAN:ANTMatrix:SOURce:AMPLitude:SOURce \n
		Snippet: driver.applications.k91Wlan.configure.wlan.antMatrix.source.amplitude.source.set(coupling = enums.CouplingAmplitude.AUTO) \n
		This remote control command determines whether the amplitude settings for the primary and secondary devices in a
		simultaneous MIMO setup are coupled or not. \n
			:param coupling: PRIMary | AUTO | OFF Coupling mode AUTO The secondary devices perform an auto-level at the same time as the primary. The amplitude settings are then determined automatically by each device according to the measured values. This feature requires that the WLAN 802.11 application R&S FSW-K91 (version 1.31 or higher) is installed on the secondary device. PRIMary Both the primary and all secondarys use the same amplitude settings, according to the settings at the primary. All settings on the secondary are ignored (including 'Reference Level Auto') . Note: if 'Reference Level Auto' is set at the primary, the primary channel performs an auto-level measurement and the resulting amplitude settings are transferred to the secondarys. OFF Both the primary and secondary devices use their own amplitude settings as defined prior to the measurement; the settings are not coupled.
		"""
		param = Conversions.enum_scalar_to_str(coupling, enums.CouplingAmplitude)
		self._core.io.write(f'CONFigure:WLAN:ANTMatrix:SOURce:AMPLitude:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CouplingAmplitude:
		"""SCPI: CONFigure:WLAN:ANTMatrix:SOURce:AMPLitude:SOURce \n
		Snippet: value: enums.CouplingAmplitude = driver.applications.k91Wlan.configure.wlan.antMatrix.source.amplitude.source.get() \n
		This remote control command determines whether the amplitude settings for the primary and secondary devices in a
		simultaneous MIMO setup are coupled or not. \n
			:return: coupling: PRIMary | AUTO | OFF Coupling mode AUTO The secondary devices perform an auto-level at the same time as the primary. The amplitude settings are then determined automatically by each device according to the measured values. This feature requires that the WLAN 802.11 application R&S FSW-K91 (version 1.31 or higher) is installed on the secondary device. PRIMary Both the primary and all secondarys use the same amplitude settings, according to the settings at the primary. All settings on the secondary are ignored (including 'Reference Level Auto') . Note: if 'Reference Level Auto' is set at the primary, the primary channel performs an auto-level measurement and the resulting amplitude settings are transferred to the secondarys. OFF Both the primary and secondary devices use their own amplitude settings as defined prior to the measurement; the settings are not coupled."""
		response = self._core.io.query_str(f'CONFigure:WLAN:ANTMatrix:SOURce:AMPLitude:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.CouplingAmplitude)
