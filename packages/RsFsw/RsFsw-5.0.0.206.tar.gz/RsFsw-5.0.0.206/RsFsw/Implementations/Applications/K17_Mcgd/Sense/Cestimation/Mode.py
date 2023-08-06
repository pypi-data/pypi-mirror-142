from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.CestMode) -> None:
		"""SCPI: [SENSe]:CESTimation:MODE \n
		Snippet: driver.applications.k17Mcgd.sense.cestimation.mode.set(mode = enums.CestMode.CARRiers) \n
		Sets/queries the carrier estimation mode. This defines how the carrier frequencies of the captured multi-carrier signal
		are estimated and how differences compared to the multi-carrier signal description are being compensated. \n
			:param mode: CARRiers | OFFSet | OFF CARRiers Estimates the frequency for each carrier and uses the determined frequencies when calculating measurement results. This estimation is useful for in-orbit measurements of satellites for which the group delay can be distorted due to the Doppler effect. (Corresponds to the manual setting 'All Carriers') OFFSet The frequency offset is assumed to be identical for all carriers. It is estimated and the determined frequencies are then used for calculation of measurement results. OFF No estimation is performed. The carrier frequencies as defined in the multi-carrier signal description are used. Possible frequency offsets or Doppler-effects are not compensated.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.CestMode)
		self._core.io.write(f'SENSe:CESTimation:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CestMode:
		"""SCPI: [SENSe]:CESTimation:MODE \n
		Snippet: value: enums.CestMode = driver.applications.k17Mcgd.sense.cestimation.mode.get() \n
		Sets/queries the carrier estimation mode. This defines how the carrier frequencies of the captured multi-carrier signal
		are estimated and how differences compared to the multi-carrier signal description are being compensated. \n
			:return: mode: CARRiers | OFFSet | OFF CARRiers Estimates the frequency for each carrier and uses the determined frequencies when calculating measurement results. This estimation is useful for in-orbit measurements of satellites for which the group delay can be distorted due to the Doppler effect. (Corresponds to the manual setting 'All Carriers') OFFSet The frequency offset is assumed to be identical for all carriers. It is estimated and the determined frequencies are then used for calculation of measurement results. OFF No estimation is performed. The carrier frequencies as defined in the multi-carrier signal description are used. Possible frequency offsets or Doppler-effects are not compensated."""
		response = self._core.io.query_str(f'SENSe:CESTimation:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.CestMode)
