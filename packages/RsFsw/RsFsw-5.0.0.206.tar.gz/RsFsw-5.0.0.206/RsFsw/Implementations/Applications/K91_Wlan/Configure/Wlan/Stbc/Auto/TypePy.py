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

	def set(self, ppdu_type: enums.PpduTypeB) -> None:
		"""SCPI: CONFigure:WLAN:STBC:AUTO:TYPE \n
		Snippet: driver.applications.k91Wlan.configure.wlan.stbc.auto.typePy.set(ppdu_type = enums.PpduTypeB.ALL) \n
		This remote control command specifies which PPDUs are analyzed according to STBC streams (for IEEE 802.11n, ac standards
		only) . \n
			:param ppdu_type: FBURst | ALL | M0 | M1 | M2 | D0 | D1 | D2 FBURst The STBC of the first PPDU is detected and subsequent PPDUs are analyzed only if they have the same STBC (corresponds to 'Auto, same type as first PPDU') ALL All recognized PPDUs are analyzed according to their individual STBC (corresponds to 'Auto, individually for each PPDU') M0 | M1 | M2 Measure only if STBC field = 0 | 1 | 2 For details see 'STBC Field' D0 | D1 | D2 Demod all as STBC field = 0 | 1 | 2 For details see 'STBC Field'
		"""
		param = Conversions.enum_scalar_to_str(ppdu_type, enums.PpduTypeB)
		self._core.io.write(f'CONFigure:WLAN:STBC:AUTO:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PpduTypeB:
		"""SCPI: CONFigure:WLAN:STBC:AUTO:TYPE \n
		Snippet: value: enums.PpduTypeB = driver.applications.k91Wlan.configure.wlan.stbc.auto.typePy.get() \n
		This remote control command specifies which PPDUs are analyzed according to STBC streams (for IEEE 802.11n, ac standards
		only) . \n
			:return: ppdu_type: FBURst | ALL | M0 | M1 | M2 | D0 | D1 | D2 FBURst The STBC of the first PPDU is detected and subsequent PPDUs are analyzed only if they have the same STBC (corresponds to 'Auto, same type as first PPDU') ALL All recognized PPDUs are analyzed according to their individual STBC (corresponds to 'Auto, individually for each PPDU') M0 | M1 | M2 Measure only if STBC field = 0 | 1 | 2 For details see 'STBC Field' D0 | D1 | D2 Demod all as STBC field = 0 | 1 | 2 For details see 'STBC Field'"""
		response = self._core.io.query_str(f'CONFigure:WLAN:STBC:AUTO:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.PpduTypeB)
