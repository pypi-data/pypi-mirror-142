from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, time: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:RESult:OFFSet \n
		Snippet: driver.applications.k60Transient.calculate.result.offset.set(time = 1.0, window = repcap.Window.Default) \n
		The offset in seconds from the hop/chirp edge or center at which the result range reference point occurs. \n
			:param time: Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(time)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:RESult:OFFSet {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:RESult:OFFSet \n
		Snippet: value: float = driver.applications.k60Transient.calculate.result.offset.get(window = repcap.Window.Default) \n
		The offset in seconds from the hop/chirp edge or center at which the result range reference point occurs. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: time: Unit: S"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:RESult:OFFSet?')
		return Conversions.str_to_float(response)
