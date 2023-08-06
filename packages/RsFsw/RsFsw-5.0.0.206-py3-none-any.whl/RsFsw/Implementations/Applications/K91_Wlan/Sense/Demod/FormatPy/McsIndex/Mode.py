from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.PpduSelectMode) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:MCSindex:MODE \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.mcsIndex.mode.set(mode = enums.PpduSelectMode.ALL) \n
		This command defines the PPDUs taking part in the analysis depending on their Modulation and Coding Scheme (MCS) index
		(for IEEE 802.11n, ac standards only) . \n
			:param mode: FBURst | ALL | MEASure | DEMod FBURst The MCS index of the first PPDU is detected and subsequent PPDUs are analyzed only if they have the same MCS index (corresponds to 'Auto, same type as first PPDU') ALL All recognized PPDUs are analyzed according to their individual MCS indexes (corresponds to 'Auto, individually for each PPDU') MEASure Only PPDUs with an MCS index which matches that specified by [SENSe:]DEMod:FORMat:MCSindex are analyzed DEMod All PPDUs will be analyzed according to the MCS index specified by [SENSe:]DEMod:FORMat:MCSindex.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PpduSelectMode)
		self._core.io.write(f'SENSe:DEMod:FORMat:MCSindex:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PpduSelectMode:
		"""SCPI: [SENSe]:DEMod:FORMat:MCSindex:MODE \n
		Snippet: value: enums.PpduSelectMode = driver.applications.k91Wlan.sense.demod.formatPy.mcsIndex.mode.get() \n
		This command defines the PPDUs taking part in the analysis depending on their Modulation and Coding Scheme (MCS) index
		(for IEEE 802.11n, ac standards only) . \n
			:return: mode: FBURst | ALL | MEASure | DEMod FBURst The MCS index of the first PPDU is detected and subsequent PPDUs are analyzed only if they have the same MCS index (corresponds to 'Auto, same type as first PPDU') ALL All recognized PPDUs are analyzed according to their individual MCS indexes (corresponds to 'Auto, individually for each PPDU') MEASure Only PPDUs with an MCS index which matches that specified by [SENSe:]DEMod:FORMat:MCSindex are analyzed DEMod All PPDUs will be analyzed according to the MCS index specified by [SENSe:]DEMod:FORMat:MCSindex."""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:MCSindex:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PpduSelectMode)
