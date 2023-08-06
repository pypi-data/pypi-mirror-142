from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, coupling: enums.CouplingRlevel) -> None:
		"""SCPI: CONFigure:WLAN:ANTMatrix:SOURce:RLEVel:OFFSet \n
		Snippet: driver.applications.k91Wlan.configure.wlan.antMatrix.source.refLevel.offset.set(coupling = enums.CouplingRlevel.MANual) \n
		This remote control command determines whether the reference level for the primary and secondary devices in a
		simultaneous MIMO setup are coupled or not. \n
			:param coupling: PRIMary | MANual Coupling mode PRIMary The secondary analyzers' reference levels are set to match that of the primary. MANual The secondary analyzers' reference levels are specified individually (see method RsFsw.Applications.K91_Wlan.Configure.Wlan.AntMatrix.Source.RefLevel.Offset.set) and are not coupled to the reference level offset of the primary analyzer.
		"""
		param = Conversions.enum_scalar_to_str(coupling, enums.CouplingRlevel)
		self._core.io.write(f'CONFigure:WLAN:ANTMatrix:SOURce:RLEVel:OFFSet {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CouplingRlevel:
		"""SCPI: CONFigure:WLAN:ANTMatrix:SOURce:RLEVel:OFFSet \n
		Snippet: value: enums.CouplingRlevel = driver.applications.k91Wlan.configure.wlan.antMatrix.source.refLevel.offset.get() \n
		This remote control command determines whether the reference level for the primary and secondary devices in a
		simultaneous MIMO setup are coupled or not. \n
			:return: coupling: PRIMary | MANual Coupling mode PRIMary The secondary analyzers' reference levels are set to match that of the primary. MANual The secondary analyzers' reference levels are specified individually (see method RsFsw.Applications.K91_Wlan.Configure.Wlan.AntMatrix.Source.RefLevel.Offset.set) and are not coupled to the reference level offset of the primary analyzer."""
		response = self._core.io.query_str(f'CONFigure:WLAN:ANTMatrix:SOURce:RLEVel:OFFSet?')
		return Conversions.str_to_scalar_enum(response, enums.CouplingRlevel)
