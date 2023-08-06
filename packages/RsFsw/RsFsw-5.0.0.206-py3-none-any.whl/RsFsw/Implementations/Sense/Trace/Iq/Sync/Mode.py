from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, dev_name: str, ms_sync_mode: enums.MsSyncMode) -> None:
		"""SCPI: [SENSe]:TRACe:IQ:SYNC:MODE \n
		Snippet: driver.sense.trace.iq.sync.mode.set(dev_name = '1', ms_sync_mode = enums.MsSyncMode.MASTer) \n
		No command help available \n
			:param dev_name: No help available
			:param ms_sync_mode: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('dev_name', dev_name, DataType.String), ArgSingle('ms_sync_mode', ms_sync_mode, DataType.Enum, enums.MsSyncMode))
		self._core.io.write(f'SENSe:TRACe:IQ:SYNC:MODE {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self) -> enums.MsSyncMode:
		"""SCPI: [SENSe]:TRACe:IQ:SYNC:MODE \n
		Snippet: value: enums.MsSyncMode = driver.sense.trace.iq.sync.mode.get() \n
		No command help available \n
			:return: ms_sync_mode: No help available"""
		response = self._core.io.query_str(f'SENSe:TRACe:IQ:SYNC:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.MsSyncMode)
