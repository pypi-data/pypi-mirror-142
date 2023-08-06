from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Column:
	"""Column commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("column", core, parent)

	def set(self, state: bool, headers: List[enums.HopTableHeaders] = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:COLumn \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.table.column.set(state = False, headers = [HopTableHeaders.ALL, HopTableHeaders.SWITching], window = repcap.Window.Default) \n
		This command enables or disables columns in all hop results and statistics tables. Note that only the enabled columns are
		returned for the method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Table.Results.get_ query. \n
			:param state: ON | OFF | 1 | 0 Enables or disables all subsequently listed headers ON | 1 Provides results for the defined Headers only OFF | 0 Provides results for all table parameters except the specified Headers.
			:param headers: ALL | STATe | BEGin | DWELl | SWITching | STAFrequency | FREQuency | RELFrequency | FMERror | MAXFm | RMSFm | AVGFm | MINPower | MAXPower | AVGPower | PWRRipple | AVPHm | MXPHm | RMSPm | FMSPoint | FMSTime | FMSLength | PMSPoint | PMSTime | PMSLength All listed parameters are displayed or hidden in the table results (depending on the State parameter) . ALL See 'Hop parameters'. STATe Hop state BEGin Hop Begin DWELl Hop dwell time SWITching Switching time STAFrequency State frequency (nominal) FREQuency Average frequency RELFrequency Relative frequency (hop-to-hop) FMERror Hop state deviation MAXFm Maximum frequency deviation RMSFm RMS frequency deviation AVGFm Average frequency deviation MINPower Minimum power MAXPower Maximum power AVGPower Average power PWRRipple Power ripple AVPHm Average phase deviation MXPHm Maximum phase deviation RMSPm RMS phase deviation FMSPoint FM settling point FMSTime FM settling time FMSLength FM settled length PMSPoint PM settling point PMSTime PM settling time PMSLength PM settled length
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('headers', headers, DataType.EnumList, enums.HopTableHeaders, True, True, 1))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:COLumn {param}'.rstrip())

	# noinspection PyTypeChecker
	class ColumnStruct(StructBase):
		"""Response structure. Fields: \n
			- State: bool: ON | OFF | 1 | 0 Enables or disables all subsequently listed headers ON | 1 Provides results for the defined Headers only OFF | 0 Provides results for all table parameters except the specified Headers.
			- Headers: List[enums.HopTableHeaders]: ALL | STATe | BEGin | DWELl | SWITching | STAFrequency | FREQuency | RELFrequency | FMERror | MAXFm | RMSFm | AVGFm | MINPower | MAXPower | AVGPower | PWRRipple | AVPHm | MXPHm | RMSPm | FMSPoint | FMSTime | FMSLength | PMSPoint | PMSTime | PMSLength All listed parameters are displayed or hidden in the table results (depending on the State parameter) . ALL See 'Hop parameters'. STATe Hop state BEGin Hop Begin DWELl Hop dwell time SWITching Switching time STAFrequency State frequency (nominal) FREQuency Average frequency RELFrequency Relative frequency (hop-to-hop) FMERror Hop state deviation MAXFm Maximum frequency deviation RMSFm RMS frequency deviation AVGFm Average frequency deviation MINPower Minimum power MAXPower Maximum power AVGPower Average power PWRRipple Power ripple AVPHm Average phase deviation MXPHm Maximum phase deviation RMSPm RMS phase deviation FMSPoint FM settling point FMSTime FM settling time FMSLength FM settled length PMSPoint PM settling point PMSTime PM settling time PMSLength PM settled length"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State'),
			ArgStruct('Headers', DataType.EnumList, enums.HopTableHeaders, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: bool = None
			self.Headers: List[enums.HopTableHeaders] = None

	def get(self, window=repcap.Window.Default) -> ColumnStruct:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:COLumn \n
		Snippet: value: ColumnStruct = driver.applications.k60Transient.calculate.hopDetection.table.column.get(window = repcap.Window.Default) \n
		This command enables or disables columns in all hop results and statistics tables. Note that only the enabled columns are
		returned for the method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Table.Results.get_ query. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for ColumnStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:COLumn?', self.__class__.ColumnStruct())
