from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SnRatio:
	"""SnRatio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snRatio", core, parent)

	def set(self, ratio: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:SNRatio \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.snRatio.set(ratio = 1.0, rangePy = repcap.RangePy.Default) \n
		Defines the minimum signal-to-noise ratio (in dB) that the power level must exceed for a spur to be recognized during the
		final spur frequency scan (see 'Measurement process') . \n
			:param ratio: Unit: DB
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(ratio)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:SNRatio {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:SNRatio \n
		Snippet: value: float = driver.applications.k50Spurious.sense.listPy.range.snRatio.get(rangePy = repcap.RangePy.Default) \n
		Defines the minimum signal-to-noise ratio (in dB) that the power level must exceed for a spur to be recognized during the
		final spur frequency scan (see 'Measurement process') . \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: ratio: Unit: DB"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:SNRatio?')
		return Conversions.str_to_float(response)
