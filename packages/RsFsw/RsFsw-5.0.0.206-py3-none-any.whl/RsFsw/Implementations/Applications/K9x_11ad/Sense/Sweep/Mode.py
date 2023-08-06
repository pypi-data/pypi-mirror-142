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

	def set(self, mode: enums.SweepModeB) -> None:
		"""SCPI: [SENSe]:SWEep:MODE \n
		Snippet: driver.applications.k9X11Ad.sense.sweep.mode.set(mode = enums.SweepModeB.AUTO) \n
		Selects the measurement to be performed. \n
			:param mode: AUTO | ESPectrum AUTO Standard IEEE 802.11ad I/Q measurement ESPectrum Spectrum emission mask measurement
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SweepModeB)
		self._core.io.write(f'SENSe:SWEep:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepModeB:
		"""SCPI: [SENSe]:SWEep:MODE \n
		Snippet: value: enums.SweepModeB = driver.applications.k9X11Ad.sense.sweep.mode.get() \n
		Selects the measurement to be performed. \n
			:return: mode: AUTO | ESPectrum AUTO Standard IEEE 802.11ad I/Q measurement ESPectrum Spectrum emission mask measurement"""
		response = self._core.io.query_str(f'SENSe:SWEep:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SweepModeB)
