from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: CONFigure:POWer:AUTO:SWEep:TIME \n
		Snippet: driver.applications.k91Wlan.configure.power.auto.sweep.time.set(value = 1.0) \n
		This command is used to specify the auto track time, i.e. the sweep time for auto level detection. This setting can
		currently only be defined in remote control, not in manual operation. \n
			:param value: Auto level measurement sweep time Unit: S
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:POWer:AUTO:SWEep:TIME {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:POWer:AUTO:SWEep:TIME \n
		Snippet: value: float = driver.applications.k91Wlan.configure.power.auto.sweep.time.get() \n
		This command is used to specify the auto track time, i.e. the sweep time for auto level detection. This setting can
		currently only be defined in remote control, not in manual operation. \n
			:return: value: Auto level measurement sweep time Unit: S"""
		response = self._core.io.query_str(f'CONFigure:POWer:AUTO:SWEep:TIME?')
		return Conversions.str_to_float(response)
