from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trange:
	"""Trange commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trange", core, parent)

	def set(self, range_py: enums.TuningRange) -> None:
		"""SCPI: [SENSe]:ROSCillator:TRANge \n
		Snippet: driver.sense.roscillator.trange.set(range_py = enums.TuningRange.SMALl) \n
		Defines the tuning range. The tuning range is only available for the variable external reference frequency. It determines
		how far the frequency may deviate from the defined level in parts per million (10-6) . For more information see Table
		'Available Reference Frequency Input'. \n
			:param range_py: WIDE | SMALl The possible values depend on the reference source (see Table 'Available Reference Frequency Input') . SMALl With this smaller deviation (+/- 0.5 ppm) a very narrow fixed loop bandwidth of 0.1 Hz is realized. With this setting the instrument can synchronize to an external reference signal with a very precise frequency. Due to the very narrow loop bandwidth, unwanted noise or spurious components on the external reference input signal are strongly attenuated. Furthermore, the loop requires about 30 seconds to reach a locked state. During this locking process, 'NO REF' is displayed in the status bar. WIDE The larger deviation (+/- 6 ppm) allows the instrument to synchronize to less precise external reference input signals.
		"""
		param = Conversions.enum_scalar_to_str(range_py, enums.TuningRange)
		self._core.io.write(f'SENSe:ROSCillator:TRANge {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TuningRange:
		"""SCPI: [SENSe]:ROSCillator:TRANge \n
		Snippet: value: enums.TuningRange = driver.sense.roscillator.trange.get() \n
		Defines the tuning range. The tuning range is only available for the variable external reference frequency. It determines
		how far the frequency may deviate from the defined level in parts per million (10-6) . For more information see Table
		'Available Reference Frequency Input'. \n
			:return: range_py: WIDE | SMALl The possible values depend on the reference source (see Table 'Available Reference Frequency Input') . SMALl With this smaller deviation (+/- 0.5 ppm) a very narrow fixed loop bandwidth of 0.1 Hz is realized. With this setting the instrument can synchronize to an external reference signal with a very precise frequency. Due to the very narrow loop bandwidth, unwanted noise or spurious components on the external reference input signal are strongly attenuated. Furthermore, the loop requires about 30 seconds to reach a locked state. During this locking process, 'NO REF' is displayed in the status bar. WIDE The larger deviation (+/- 6 ppm) allows the instrument to synchronize to less precise external reference input signals."""
		response = self._core.io.query_str(f'SENSe:ROSCillator:TRANge?')
		return Conversions.str_to_scalar_enum(response, enums.TuningRange)
