from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: MMEMory:LOAD:STATe \n
		Snippet: driver.massMemory.load.state.set(filename = '1') \n
		This command restores and activates the instrument configuration stored in a *.dfl file. Note that files with other
		formats cannot be loaded with this command. The contents that are reloaded from the file are defined by the last
		selection made either in the 'Save/Recall' dialogs (manual operation) or through the MMEMory:SELect[:ITEM] commands
		(remote operation; the settings are identical in both cases) . By default, the selection is limited to the user settings
		('User Settings' selection in the dialogs, HWSettings in SCPI) . The selection is not reset by [Preset] or *RST.
		As a consequence, the results of a SCPI script using the method RsFsw.MassMemory.Load.State.set command without a
		previous MMEMory:SELect[:ITEM] command may vary, depending on previous actions in the GUI or in previous scripts, even if
		the script starts with the *RST command. It is therefore recommended that you use the appropriate MMEMory:SELect[:ITEM]
		command before using method RsFsw.MassMemory.Load.State.set. \n
			:param filename: String containing the path and name of the file to load. The string may or may not include the file's extension.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write_with_opc(f'MMEMory:LOAD:STATe 1, {param}')
