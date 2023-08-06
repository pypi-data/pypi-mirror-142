from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Resolution:
	"""Resolution commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resolution", core, parent)

	def set(self, rbw: float, halfDecadeRange=repcap.HalfDecadeRange.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<hd>:BWIDth[:RESolution] \n
		Snippet: driver.applications.k40PhaseNoise.sense.listPy.range.bandwidth.resolution.set(rbw = 1.0, halfDecadeRange = repcap.HalfDecadeRange.Default) \n
		This command defines the resolution bandwidth for a particular half decade. \n
			:param rbw: Note that each half decade has a limited range of available bandwidths. Unit: HZ
			:param halfDecadeRange: optional repeated capability selector. Default value: Rng_1Hz_3Hz (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(rbw)
		halfDecadeRange_cmd_val = self._cmd_group.get_repcap_cmd_value(halfDecadeRange, repcap.HalfDecadeRange)
		self._core.io.write(f'SENSe:LIST:RANGe{halfDecadeRange_cmd_val}:BWIDth:RESolution {param}')

	def get(self, halfDecadeRange=repcap.HalfDecadeRange.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<hd>:BWIDth[:RESolution] \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.listPy.range.bandwidth.resolution.get(halfDecadeRange = repcap.HalfDecadeRange.Default) \n
		This command defines the resolution bandwidth for a particular half decade. \n
			:param halfDecadeRange: optional repeated capability selector. Default value: Rng_1Hz_3Hz (settable in the interface 'Range')
			:return: rbw: Note that each half decade has a limited range of available bandwidths. Unit: HZ"""
		halfDecadeRange_cmd_val = self._cmd_group.get_repcap_cmd_value(halfDecadeRange, repcap.HalfDecadeRange)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{halfDecadeRange_cmd_val}:BWIDth:RESolution?')
		return Conversions.str_to_float(response)
