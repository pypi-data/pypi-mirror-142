from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:AR:TIME:LENGth \n
		Snippet: driver.applications.k60Transient.calculate.ar.time.length.set(length = 1.0, window = repcap.Window.Default) \n
		Defines the length of the time gate, that is, the duration (or height) of the analysis region. \n
			:param length: Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(length)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:AR:TIME:LENGth {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:AR:TIME:LENGth \n
		Snippet: value: float = driver.applications.k60Transient.calculate.ar.time.length.get(window = repcap.Window.Default) \n
		Defines the length of the time gate, that is, the duration (or height) of the analysis region. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: length: Unit: S"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:AR:TIME:LENGth?')
		return Conversions.str_to_float(response)
