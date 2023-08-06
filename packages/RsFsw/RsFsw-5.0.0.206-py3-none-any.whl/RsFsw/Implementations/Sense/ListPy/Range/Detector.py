from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Detector:
	"""Detector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("detector", core, parent)

	def set(self, detector: enums.DetectorC, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:DETector \n
		Snippet: driver.sense.listPy.range.detector.set(detector = enums.DetectorC.ACSine, rangePy = repcap.RangePy.Default) \n
		This command selects the detector for a spurious emission measurement range. The sweep list cannot be configured using
		remote commands during an on-going sweep operation. \n
			:param detector: APEak Autopeak NEGative minimum peak detector POSitive peak detector SAMPle sample detector RMS RMS detector AVERage average detector
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.enum_scalar_to_str(detector, enums.DetectorC)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:DETector {param}')

	# noinspection PyTypeChecker
	def get(self, rangePy=repcap.RangePy.Default) -> enums.DetectorC:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:DETector \n
		Snippet: value: enums.DetectorC = driver.sense.listPy.range.detector.get(rangePy = repcap.RangePy.Default) \n
		This command selects the detector for a spurious emission measurement range. The sweep list cannot be configured using
		remote commands during an on-going sweep operation. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: detector: APEak Autopeak NEGative minimum peak detector POSitive peak detector SAMPle sample detector RMS RMS detector AVERage average detector"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:DETector?')
		return Conversions.str_to_scalar_enum(response, enums.DetectorC)
