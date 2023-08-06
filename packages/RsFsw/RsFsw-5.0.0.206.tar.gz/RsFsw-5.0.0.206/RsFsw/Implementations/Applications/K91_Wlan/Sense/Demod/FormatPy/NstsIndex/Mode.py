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
		"""SCPI: [SENSe]:DEMod:FORMat:NSTSindex:MODE \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.nstsIndex.mode.set(mode = enums.PpduSelectMode.ALL) \n
		Defines the PPDUs taking part in the analysis depending on their Nsts. This command is only available for the IEEE 802.11
		ac standard. \n
			:param mode: FBURst | ALL | MEASure | DEMod FBURst The Nsts of the first PPDU is detected and subsequent PPDUs are analyzed only if they have the same Nsts (corresponds to 'Auto, same type as first PPDU') ALL All recognized PPDUs are analyzed according to their individual Nsts (corresponds to 'Auto, individually for each PPDU') MEASure Only PPDUs with the Nsts specified by [SENSe:]DEMod:FORMat:NSTSindex are analyzed DEMod The 'Nsts' index specified by [SENSe:]DEMod:FORMat:NSTSindexis used for all PPDUs.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PpduSelectMode)
		self._core.io.write(f'SENSe:DEMod:FORMat:NSTSindex:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PpduSelectMode:
		"""SCPI: [SENSe]:DEMod:FORMat:NSTSindex:MODE \n
		Snippet: value: enums.PpduSelectMode = driver.applications.k91Wlan.sense.demod.formatPy.nstsIndex.mode.get() \n
		Defines the PPDUs taking part in the analysis depending on their Nsts. This command is only available for the IEEE 802.11
		ac standard. \n
			:return: mode: FBURst | ALL | MEASure | DEMod FBURst The Nsts of the first PPDU is detected and subsequent PPDUs are analyzed only if they have the same Nsts (corresponds to 'Auto, same type as first PPDU') ALL All recognized PPDUs are analyzed according to their individual Nsts (corresponds to 'Auto, individually for each PPDU') MEASure Only PPDUs with the Nsts specified by [SENSe:]DEMod:FORMat:NSTSindex are analyzed DEMod The 'Nsts' index specified by [SENSe:]DEMod:FORMat:NSTSindexis used for all PPDUs."""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:NSTSindex:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PpduSelectMode)
