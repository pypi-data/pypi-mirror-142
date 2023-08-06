from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SigSymbol:
	"""SigSymbol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sigSymbol", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:SIGSymbol \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.sigSymbol.set(state = False) \n
		Activates and deactivates signal symbol field decoding. For IEEE 802.11b this command can only be queried as the decoding
		of the signal field is always performed for this standard. \n
			:param state: OFF | 0 Deactivates signal symbol field decoding. All PPDUs are assumed to have the specified PPDU format / PSDU modulation, regardless of the actual format or modulation. ON | 1 If activated, the signal symbol field of the PPDU is analyzed to determine the details of the PPDU. Only PPDUs which match the PPDU type/ PSDU modulation defined by [SENSe:]DEMod:FORMat:BANalyze and [SENSe:]DEMod:FORMat:BANalyze:BTYPe are considered in results analysis.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DEMod:FORMat:SIGSymbol {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DEMod:FORMat:SIGSymbol \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.demod.formatPy.sigSymbol.get() \n
		Activates and deactivates signal symbol field decoding. For IEEE 802.11b this command can only be queried as the decoding
		of the signal field is always performed for this standard. \n
			:return: state: OFF | 0 Deactivates signal symbol field decoding. All PPDUs are assumed to have the specified PPDU format / PSDU modulation, regardless of the actual format or modulation. ON | 1 If activated, the signal symbol field of the PPDU is analyzed to determine the details of the PPDU. Only PPDUs which match the PPDU type/ PSDU modulation defined by [SENSe:]DEMod:FORMat:BANalyze and [SENSe:]DEMod:FORMat:BANalyze:BTYPe are considered in results analysis."""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:SIGSymbol?')
		return Conversions.str_to_bool(response)
