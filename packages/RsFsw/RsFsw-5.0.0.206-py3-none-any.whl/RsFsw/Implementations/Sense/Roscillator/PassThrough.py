from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.Utilities import trim_str_response
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PassThrough:
	"""PassThrough commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("passThrough", core, parent)

	def set(self, dev_name: str, arg_1: bool) -> None:
		"""SCPI: [SENSe]:ROSCillator:PASSthrough \n
		Snippet: driver.sense.roscillator.passThrough.set(dev_name = '1', arg_1 = False) \n
		No command help available \n
			:param dev_name: No help available
			:param arg_1: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('dev_name', dev_name, DataType.String), ArgSingle('arg_1', arg_1, DataType.Boolean))
		self._core.io.write(f'SENSe:ROSCillator:PASSthrough {param}'.rstrip())

	def get(self) -> str:
		"""SCPI: [SENSe]:ROSCillator:PASSthrough \n
		Snippet: value: str = driver.sense.roscillator.passThrough.get() \n
		No command help available \n
			:return: dev_name: No help available"""
		response = self._core.io.query_str(f'SENSe:ROSCillator:PASSthrough?')
		return trim_str_response(response)
