from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, measurements: float, halfDecadeRange=repcap.HalfDecadeRange.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<hd>:SWEep:COUNt \n
		Snippet: driver.applications.k40PhaseNoise.sense.listPy.range.sweep.count.set(measurements = 1.0, halfDecadeRange = repcap.HalfDecadeRange.Default) \n
		This command defines the number of measurements included in the averaging for a half decade. \n
			:param measurements: Range: 1 to 10000
			:param halfDecadeRange: optional repeated capability selector. Default value: Rng_1Hz_3Hz (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(measurements)
		halfDecadeRange_cmd_val = self._cmd_group.get_repcap_cmd_value(halfDecadeRange, repcap.HalfDecadeRange)
		self._core.io.write(f'SENSe:LIST:RANGe{halfDecadeRange_cmd_val}:SWEep:COUNt {param}')

	def get(self, halfDecadeRange=repcap.HalfDecadeRange.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<hd>:SWEep:COUNt \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.listPy.range.sweep.count.get(halfDecadeRange = repcap.HalfDecadeRange.Default) \n
		This command defines the number of measurements included in the averaging for a half decade. \n
			:param halfDecadeRange: optional repeated capability selector. Default value: Rng_1Hz_3Hz (settable in the interface 'Range')
			:return: measurements: Range: 1 to 10000"""
		halfDecadeRange_cmd_val = self._cmd_group.get_repcap_cmd_value(halfDecadeRange, repcap.HalfDecadeRange)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{halfDecadeRange_cmd_val}:SWEep:COUNt?')
		return Conversions.str_to_float(response)
