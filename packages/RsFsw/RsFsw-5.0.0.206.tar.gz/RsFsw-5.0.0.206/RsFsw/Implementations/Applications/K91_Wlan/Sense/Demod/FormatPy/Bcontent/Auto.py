from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat[:BCONtent]:AUTO \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.bcontent.auto.set(state = False) \n
		This command determines whether the PPDUs to be analyzed are determined automatically or by the user. \n
			:param state: ON | 1 The signal field, i.e. the PLCP header field, of the first recognized PPDU is analyzed to determine the details of the PPDU. All PPDUs identical to the first recognized PPDU are analyzed. OFF | 0 Only PPDUs that match the user-defined PPDU type and modulation are considered in results analysis (see [SENSe:]DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE and [SENSe:]DEMod:FORMat:BANalyze) .
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DEMod:FORMat:BCONtent:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DEMod:FORMat[:BCONtent]:AUTO \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.demod.formatPy.bcontent.auto.get() \n
		This command determines whether the PPDUs to be analyzed are determined automatically or by the user. \n
			:return: state: ON | 1 The signal field, i.e. the PLCP header field, of the first recognized PPDU is analyzed to determine the details of the PPDU. All PPDUs identical to the first recognized PPDU are analyzed. OFF | 0 Only PPDUs that match the user-defined PPDU type and modulation are considered in results analysis (see [SENSe:]DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE and [SENSe:]DEMod:FORMat:BANalyze) ."""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:BCONtent:AUTO?')
		return Conversions.str_to_bool(response)
