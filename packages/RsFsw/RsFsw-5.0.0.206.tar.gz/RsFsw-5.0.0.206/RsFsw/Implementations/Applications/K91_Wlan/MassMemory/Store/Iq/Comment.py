from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Comment:
	"""Comment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("comment", core, parent)

	def set(self, state: int, trace: str) -> None:
		"""SCPI: MMEMory:STORe:IQ:COMMent \n
		Snippet: driver.applications.k91Wlan.massMemory.store.iq.comment.set(state = 1, trace = '1') \n
		This command adds a comment to a file that contains I/Q data. \n
			:param state: No help available
			:param trace: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Integer), ArgSingle('trace', trace, DataType.String))
		self._core.io.write(f'MMEMory:STORe:IQ:COMMent {param}'.rstrip())
