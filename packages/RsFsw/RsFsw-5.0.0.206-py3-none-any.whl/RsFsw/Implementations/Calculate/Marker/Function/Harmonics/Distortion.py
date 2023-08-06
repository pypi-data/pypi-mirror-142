from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Distortion:
	"""Distortion commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("distortion", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Distortion_Pct: float: No parameter help available
			- Distortion_Db: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Distortion_Pct'),
			ArgStruct.scalar_float('Distortion_Db')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Distortion_Pct: float = None
			self.Distortion_Db: float = None

	def get(self, result: enums.ResultTypeD = None, window=repcap.Window.Default, marker=repcap.Marker.Default) -> GetStruct:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:HARMonics:DISTortion \n
		Snippet: value: GetStruct = driver.calculate.marker.function.harmonics.distortion.get(result = enums.ResultTypeD.TOTal, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the total harmonic distortion of the signal. To get a valid result, you have to perform a complete
		measurement with synchronization to the end of the measurement before reading out the result. This is only possible for
		single sweep mode. See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param result: TOTal
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('result', result, DataType.Enum, enums.ResultTypeD, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:HARMonics:DISTortion? {param}'.rstrip(), self.__class__.GetStruct())
