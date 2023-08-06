from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UaRange:
	"""UaRange commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uaRange", core, parent)

	def set(self, param: enums.RangeParam, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:UARange \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.uaRange.set(param = enums.RangeParam.ARBW, rangePy = repcap.RangePy.Default) \n
		Writes the value of the specified parameter to all of the currently defined ranges. \n
			:param param: ARBW | LOFFset | MFRBw | NFFT | PAValue | PEXCursion | RBW | RFATtenuation | RLEVel | SNRatio | TSTR | TSTP
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.enum_scalar_to_str(param, enums.RangeParam)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:UARange {param}')
