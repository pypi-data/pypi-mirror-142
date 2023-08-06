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

	def set(self, mode: enums.SweepModeHalfDec) -> None:
		"""SCPI: [SENSe]:LIST:BWIDth[:RESolution]:TYPE \n
		Snippet: driver.applications.k40PhaseNoise.sense.listPy.bandwidth.resolution.typePy.set(mode = enums.SweepModeHalfDec.FFT) \n
		This command selects the sweep mode for all half decades. \n
			:param mode: NORMal | FFT | IQFFt NORMal Measurement based on spectrum analyzer data. FFT Measurement based on spectrum analyzer data. Kept for compatibility to R&S FSV.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SweepModeHalfDec)
		self._core.io.write(f'SENSe:LIST:BWIDth:RESolution:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepModeHalfDec:
		"""SCPI: [SENSe]:LIST:BWIDth[:RESolution]:TYPE \n
		Snippet: value: enums.SweepModeHalfDec = driver.applications.k40PhaseNoise.sense.listPy.bandwidth.resolution.typePy.get() \n
		This command selects the sweep mode for all half decades. \n
			:return: mode: NORMal | FFT | IQFFt NORMal Measurement based on spectrum analyzer data. FFT Measurement based on spectrum analyzer data. Kept for compatibility to R&S FSV."""
		response = self._core.io.query_str(f'SENSe:LIST:BWIDth:RESolution:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.SweepModeHalfDec)
