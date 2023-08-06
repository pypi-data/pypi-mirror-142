from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, time: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:RESult:LENGth \n
		Snippet: driver.applications.k60Transient.calculate.result.length.set(time = 1.0, window = repcap.Window.Default) \n
		This command defines the length or duration of the result range. Note this command is only available for manual range
		scaling (see method RsFsw.Applications.K60_Transient.Calculate.Result.Range.Auto.set) . \n
			:param time: Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(time)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:RESult:LENGth {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:RESult:LENGth \n
		Snippet: value: float = driver.applications.k60Transient.calculate.result.length.get(window = repcap.Window.Default) \n
		This command defines the length or duration of the result range. Note this command is only available for manual range
		scaling (see method RsFsw.Applications.K60_Transient.Calculate.Result.Range.Auto.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: time: Unit: S"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:RESult:LENGth?')
		return Conversions.str_to_float(response)
