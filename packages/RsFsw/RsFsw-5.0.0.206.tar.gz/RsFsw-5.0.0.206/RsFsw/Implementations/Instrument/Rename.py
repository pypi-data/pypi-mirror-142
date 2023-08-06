from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rename:
	"""Rename commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rename", core, parent)

	def set(self, channel_name_1: str, channel_name_2: str) -> None:
		"""SCPI: INSTrument:REName \n
		Snippet: driver.instrument.rename.set(channel_name_1 = '1', channel_name_2 = '1') \n
		This command renames a channel. \n
			:param channel_name_1: String containing the name of the channel you want to rename.
			:param channel_name_2: String containing the new channel name. Note that you cannot assign an existing channel name to a new channel; this will cause an error. Channel names can have a maximum of 31 characters, and must be compatible with the Windows conventions for file names. In particular, they must not contain special characters such as ':', '*', '?'.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('channel_name_1', channel_name_1, DataType.String), ArgSingle('channel_name_2', channel_name_2, DataType.String))
		self._core.io.write(f'INSTrument:REName {param}'.rstrip())
