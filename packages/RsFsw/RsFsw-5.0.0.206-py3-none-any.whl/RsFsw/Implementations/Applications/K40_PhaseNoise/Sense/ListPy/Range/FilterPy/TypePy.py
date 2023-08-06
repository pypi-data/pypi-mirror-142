from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, mode: enums.SweepModeHalfDec, halfDecadeRange=repcap.HalfDecadeRange.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<hd>:FILTer:TYPE \n
		Snippet: driver.applications.k40PhaseNoise.sense.listPy.range.filterPy.typePy.set(mode = enums.SweepModeHalfDec.FFT, halfDecadeRange = repcap.HalfDecadeRange.Default) \n
		This command selects the sweep mode for a particular half decade. \n
			:param mode: NORMal Measurement based on spectrum analyzer data. FFT Measurement based on spectrum analyzer data. Kept for compatibility to R&S FSV. IQFFt Measurement based on I/Q data.
			:param halfDecadeRange: optional repeated capability selector. Default value: Rng_1Hz_3Hz (settable in the interface 'Range')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SweepModeHalfDec)
		halfDecadeRange_cmd_val = self._cmd_group.get_repcap_cmd_value(halfDecadeRange, repcap.HalfDecadeRange)
		self._core.io.write(f'SENSe:LIST:RANGe{halfDecadeRange_cmd_val}:FILTer:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, halfDecadeRange=repcap.HalfDecadeRange.Default) -> enums.SweepModeHalfDec:
		"""SCPI: [SENSe]:LIST:RANGe<hd>:FILTer:TYPE \n
		Snippet: value: enums.SweepModeHalfDec = driver.applications.k40PhaseNoise.sense.listPy.range.filterPy.typePy.get(halfDecadeRange = repcap.HalfDecadeRange.Default) \n
		This command selects the sweep mode for a particular half decade. \n
			:param halfDecadeRange: optional repeated capability selector. Default value: Rng_1Hz_3Hz (settable in the interface 'Range')
			:return: mode: NORMal Measurement based on spectrum analyzer data. FFT Measurement based on spectrum analyzer data. Kept for compatibility to R&S FSV. IQFFt Measurement based on I/Q data."""
		halfDecadeRange_cmd_val = self._cmd_group.get_repcap_cmd_value(halfDecadeRange, repcap.HalfDecadeRange)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{halfDecadeRange_cmd_val}:FILTer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.SweepModeHalfDec)
