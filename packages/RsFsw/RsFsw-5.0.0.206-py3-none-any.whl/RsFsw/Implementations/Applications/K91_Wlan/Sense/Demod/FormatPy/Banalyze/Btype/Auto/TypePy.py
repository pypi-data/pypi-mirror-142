from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, ppdu_format: enums.PpduFormat) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.banalyze.btype.auto.typePy.set(ppdu_format = enums.PpduFormat.AIEM) \n
		This remote control command specifies how signals are analyzed. \n
			:param ppdu_format: FBURst The format of the first valid PPDU is detected and subsequent PPDUs are analyzed only if they have the same format (corresponds to 'Auto, same type as first PPDU') ALL All PPDUs are analyzed regardless of their format (corresponds to 'Auto, individually for each PPDU') MNHT Only PPDUs with format 'Non-HT' are analyzed IEEE 802.11a, g (OFDM) , p DNHT All PPDUs are assumed to have the PPDU format 'Non-HT' IEEE 802.11a, g (OFDM) , p MMIX Only PPDUs with format 'HT-MF' (Mixed) are analyzed (IEEE 802.11 n) MGRF Only PPDUs with format 'HT-GF' (Greenfield) are analyzed (IEEE 802.11 n) DMIX All PPDUs are assumed to have the PPDU format 'HT-MF' (IEEE 802.11 n) DGRF All PPDUs are assumed to have the PPDU format 'HT-GF' (IEEE 802.11 n) MVHT Only PPDUs with format 'VHT' are analyzed (IEEE 802.11 ac) DVHT All PPDUs are assumed to have the PPDU format 'VHT' (IEEE 802.11 ac) AIHS Only HE Single-User PPDUs are analyzed (IEEE 802.11 ax) AIHM Only HE Multi-User PPDUs are analyzed (IEEE 802.11 ax) AIES Only HE Extended Range PPDUs are analyzed (IEEE 802.11 ax) AIHT Only HE Trigger-based PPDUs are analyzed (IEEE 802.11 ax) DHEP All PPDUs are assumed to have HE PPDU format (IEEE 802.11 ax) FMMM Only PPDUs with specified format are analyzed (see [SENSe:]DEMod:FORMat:BANalyze) (IEEE 802.11 b, g (DSSS) ) FMMD All PPDUs are assumed to have the specified PPDU format (see [SENSe:]DEMod:FORMat:BANalyze) (IEEE 802.11 b, g (DSSS) ) DEHP All PPDUs are assumed to have EHT PPDU format (IEEE 802.11 be) AIEM Only EHT MU PPDU are analyzed (IEEE 802.11 be) AIET Only EHT trigger-based PPDU are analyzed (IEEE 802.11 be) DEHTppdu All PPDUs are assumed to have EHT PPDU format (IEEE 802.11 be)
		"""
		param = Conversions.enum_scalar_to_str(ppdu_format, enums.PpduFormat)
		self._core.io.write(f'SENSe:DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PpduFormat:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE \n
		Snippet: value: enums.PpduFormat = driver.applications.k91Wlan.sense.demod.formatPy.banalyze.btype.auto.typePy.get() \n
		This remote control command specifies how signals are analyzed. \n
			:return: ppdu_format: FBURst The format of the first valid PPDU is detected and subsequent PPDUs are analyzed only if they have the same format (corresponds to 'Auto, same type as first PPDU') ALL All PPDUs are analyzed regardless of their format (corresponds to 'Auto, individually for each PPDU') MNHT Only PPDUs with format 'Non-HT' are analyzed IEEE 802.11a, g (OFDM) , p DNHT All PPDUs are assumed to have the PPDU format 'Non-HT' IEEE 802.11a, g (OFDM) , p MMIX Only PPDUs with format 'HT-MF' (Mixed) are analyzed (IEEE 802.11 n) MGRF Only PPDUs with format 'HT-GF' (Greenfield) are analyzed (IEEE 802.11 n) DMIX All PPDUs are assumed to have the PPDU format 'HT-MF' (IEEE 802.11 n) DGRF All PPDUs are assumed to have the PPDU format 'HT-GF' (IEEE 802.11 n) MVHT Only PPDUs with format 'VHT' are analyzed (IEEE 802.11 ac) DVHT All PPDUs are assumed to have the PPDU format 'VHT' (IEEE 802.11 ac) AIHS Only HE Single-User PPDUs are analyzed (IEEE 802.11 ax) AIHM Only HE Multi-User PPDUs are analyzed (IEEE 802.11 ax) AIES Only HE Extended Range PPDUs are analyzed (IEEE 802.11 ax) AIHT Only HE Trigger-based PPDUs are analyzed (IEEE 802.11 ax) DHEP All PPDUs are assumed to have HE PPDU format (IEEE 802.11 ax) FMMM Only PPDUs with specified format are analyzed (see [SENSe:]DEMod:FORMat:BANalyze) (IEEE 802.11 b, g (DSSS) ) FMMD All PPDUs are assumed to have the specified PPDU format (see [SENSe:]DEMod:FORMat:BANalyze) (IEEE 802.11 b, g (DSSS) ) DEHP All PPDUs are assumed to have EHT PPDU format (IEEE 802.11 be) AIEM Only EHT MU PPDU are analyzed (IEEE 802.11 be) AIET Only EHT trigger-based PPDU are analyzed (IEEE 802.11 be) DEHTppdu All PPDUs are assumed to have EHT PPDU format (IEEE 802.11 be)"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.PpduFormat)
