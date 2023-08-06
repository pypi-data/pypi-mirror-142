from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Port:
	"""Port commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("port", core, parent)

	def set(self, dev_name: str, ms_master_port: enums.TriggerPort) -> None:
		"""SCPI: TRIGger:MASTer:PORT \n
		Snippet: driver.trigger.master.port.set(dev_name = '1', ms_master_port = enums.TriggerPort.EXT1) \n
		No command help available \n
			:param dev_name: No help available
			:param ms_master_port: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('dev_name', dev_name, DataType.String), ArgSingle('ms_master_port', ms_master_port, DataType.Enum, enums.TriggerPort))
		self._core.io.write(f'TRIGger:MASTer:PORT {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self) -> enums.TriggerPort:
		"""SCPI: TRIGger:MASTer:PORT \n
		Snippet: value: enums.TriggerPort = driver.trigger.master.port.get() \n
		No command help available \n
			:return: ms_master_port: No help available"""
		response = self._core.io.query_str(f'TRIGger:MASTer:PORT?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerPort)
