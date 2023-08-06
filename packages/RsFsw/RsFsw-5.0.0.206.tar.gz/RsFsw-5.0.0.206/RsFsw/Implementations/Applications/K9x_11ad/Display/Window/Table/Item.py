from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Item:
	"""Item commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("item", core, parent)

	def set(self, item: enums.TableItemK9X, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TABLe:ITEM \n
		Snippet: driver.applications.k9X11Ad.display.window.table.item.set(item = enums.TableItemK9X.RxAll_CenterFreqError=RCFerror, state = False, window = repcap.Window.Default) \n
		Defines which items are displayed in the Result Summary (see 'Result Summary') . Note that the results are always
		calculated, regardless of their visibility in the Result Summary. \n
			:param item: EVM | EVMD | EVMP | IQOF | GIMB | QERR | CFER | SCER | RTI | FTIM | TSK | TDP | CFAC | HBER | PBER Item to be included in Result Summary. For the mapping of the result to the command parameter, see Table 'Parameters for the items of the 'Result Summary'' below. For a description of the individual parameters see 'Modulation accuracy parameters'.
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('item', item, DataType.Enum, enums.TableItemK9X), ArgSingle('state', state, DataType.Boolean))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write_with_opc(f'DISPlay:WINDow{window_cmd_val}:TABLe:ITEM {param}'.rstrip())
