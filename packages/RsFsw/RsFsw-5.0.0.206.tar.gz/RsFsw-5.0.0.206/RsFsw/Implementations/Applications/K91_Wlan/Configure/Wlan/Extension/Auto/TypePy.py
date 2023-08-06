from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, ppdu_type: enums.PpduType) -> None:
		"""SCPI: CONFigure:WLAN:EXTension:AUTO:TYPE \n
		Snippet: driver.applications.k91Wlan.configure.wlan.extension.auto.typePy.set(ppdu_type = enums.PpduType.ALL) \n
		Defines the PPDUs taking part in the analysis according to the Ness (Extension Spatial Streams) field content (for IEEE
		802.11n standard only) . \n
			:param ppdu_type: FBURst | ALL | M0 | M1 | M2 | M3 | D0 | D1 | D2 | D3 The first PPDU is analyzed and subsequent PPDUs are analyzed only if they match FBURst The Ness field contents of the first PPDU is detected and subsequent PPDUs are analyzed only if they have the same Ness field contents (corresponds to 'Auto, same type as first PPDU') ALL All recognized PPDUs are analyzed according to their individual Ness field contents (corresponds to 'Auto, individually for each PPDU') M0 | M1 | M2 | M3 Only PPDUs with the specified Ness value are analyzed. D0 | D1 | D2| D3 All PPDUs are analyzed assuming the specified Ness value.
		"""
		param = Conversions.enum_scalar_to_str(ppdu_type, enums.PpduType)
		self._core.io.write(f'CONFigure:WLAN:EXTension:AUTO:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PpduType:
		"""SCPI: CONFigure:WLAN:EXTension:AUTO:TYPE \n
		Snippet: value: enums.PpduType = driver.applications.k91Wlan.configure.wlan.extension.auto.typePy.get() \n
		Defines the PPDUs taking part in the analysis according to the Ness (Extension Spatial Streams) field content (for IEEE
		802.11n standard only) . \n
			:return: ppdu_type: FBURst | ALL | M0 | M1 | M2 | M3 | D0 | D1 | D2 | D3 The first PPDU is analyzed and subsequent PPDUs are analyzed only if they match FBURst The Ness field contents of the first PPDU is detected and subsequent PPDUs are analyzed only if they have the same Ness field contents (corresponds to 'Auto, same type as first PPDU') ALL All recognized PPDUs are analyzed according to their individual Ness field contents (corresponds to 'Auto, individually for each PPDU') M0 | M1 | M2 | M3 Only PPDUs with the specified Ness value are analyzed. D0 | D1 | D2| D3 All PPDUs are analyzed assuming the specified Ness value."""
		response = self._core.io.query_str(f'CONFigure:WLAN:EXTension:AUTO:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.PpduType)
