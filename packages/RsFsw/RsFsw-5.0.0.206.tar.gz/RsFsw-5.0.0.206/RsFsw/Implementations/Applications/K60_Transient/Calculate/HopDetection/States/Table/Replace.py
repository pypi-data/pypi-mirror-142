from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Replace:
	"""Replace commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("replace", core, parent)

	def set(self, start: List[int], step: List[int], number: List[int], window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:STATes:TABLe:REPLace \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.states.table.replace.set(start = [1, 2, 3], step = [1, 2, 3], number = [1, 2, 3], window = repcap.Window.Default) \n
		No command help available \n
			:param start: The frequency at which the first hop state will be generated. Unit: HZ
			:param step: The distance between two hop states. Unit: HZ
			:param number: Number of hop states to be generated.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('start', start, DataType.IntegerList, None), ArgSingle.as_open_list('step', step, DataType.IntegerList, None), ArgSingle.as_open_list('number', number, DataType.IntegerList, None))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:STATes:TABLe:REPLace {param}'.rstrip())
