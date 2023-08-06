from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ival:
	"""Ival commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ival", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Int_Start: float: Analysis start = Capture offset time Unit: s
			- Int_Stop: float: Analysis end = capture offset + capture time Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_float('Int_Start'),
			ArgStruct.scalar_float('Int_Stop')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Int_Start: float = None
			self.Int_Stop: float = None

	def get(self, window=repcap.Window.Default) -> GetStruct:
		"""SCPI: CALCulate<n>:MSRA:WINDow:IVAL \n
		Snippet: value: GetStruct = driver.applications.k60Transient.calculate.msra.window.ival.get(window = repcap.Window.Default) \n
		Returns the current analysis interval for applications in MSRA operating mode. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:MSRA:WINDow:IVAL?', self.__class__.GetStruct())
