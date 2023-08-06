from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: [SENSe]:ADEMod:ZOOM:STARt \n
		Snippet: driver.sense.ademod.zoom.start.set(time = 1.0) \n
		The command selects the start time for the zoomed display of analog-demodulated measurements in the specified window. The
		maximum possible value depends on the measurement time, which is set and can be queried with the [SENSe:]ADEMod:MTIMe
		command. If the zoom function is enabled, the defined number of sweep points are displayed from the start time specified
		with this command. \n
			:param time: Range: 0 s to (measurement time – zoom length) , Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SENSe:ADEMod:ZOOM:STARt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:ZOOM:STARt \n
		Snippet: value: float = driver.sense.ademod.zoom.start.get() \n
		The command selects the start time for the zoomed display of analog-demodulated measurements in the specified window. The
		maximum possible value depends on the measurement time, which is set and can be queried with the [SENSe:]ADEMod:MTIMe
		command. If the zoom function is enabled, the defined number of sweep points are displayed from the start time specified
		with this command. \n
			:return: time: Range: 0 s to (measurement time – zoom length) , Unit: S"""
		response = self._core.io.query_str(f'SENSe:ADEMod:ZOOM:STARt?')
		return Conversions.str_to_float(response)
