from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Define:
	"""Define commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("define", core, parent)

	def set(self, placeholder: str, type_py: str, interface: str, serial_no: str, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:PMETer<p>:DEFine \n
		Snippet: driver.applications.k14Xnr5G.system.communicate.rdevice.pmeter.define.set(placeholder = '1', type_py = '1', interface = '1', serial_no = '1', powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param placeholder: No help available
			:param type_py: No help available
			:param interface: No help available
			:param serial_no: No help available
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('placeholder', placeholder, DataType.String), ArgSingle('type_py', type_py, DataType.String), ArgSingle('interface', interface, DataType.String), ArgSingle('serial_no', serial_no, DataType.String))
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:PMETer{powerMeter_cmd_val}:DEFine {param}'.rstrip())

	# noinspection PyTypeChecker
	class DefineStruct(StructBase):
		"""Response structure. Fields: \n
			- Placeholder: str: No parameter help available
			- Type_Py: str: No parameter help available
			- Interface: str: No parameter help available
			- Serial_No: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Placeholder'),
			ArgStruct.scalar_str('Type_Py'),
			ArgStruct.scalar_str('Interface'),
			ArgStruct.scalar_str('Serial_No')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Placeholder: str = None
			self.Type_Py: str = None
			self.Interface: str = None
			self.Serial_No: str = None

	def get(self, powerMeter=repcap.PowerMeter.Default) -> DefineStruct:
		"""SCPI: SYSTem:COMMunicate:RDEVice:PMETer<p>:DEFine \n
		Snippet: value: DefineStruct = driver.applications.k14Xnr5G.system.communicate.rdevice.pmeter.define.get(powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: structure: for return value, see the help for DefineStruct structure arguments."""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		return self._core.io.query_struct(f'SYSTem:COMMunicate:RDEVice:PMETer{powerMeter_cmd_val}:DEFine?', self.__class__.DefineStruct())
