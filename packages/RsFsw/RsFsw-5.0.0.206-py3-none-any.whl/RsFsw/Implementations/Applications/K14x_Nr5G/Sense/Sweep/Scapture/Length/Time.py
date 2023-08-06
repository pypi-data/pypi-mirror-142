from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, length: float) -> None:
		"""SCPI: [SENSe]:SWEep:SCAPture:LENGth[:TIME] \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.scapture.length.time.set(length = 1.0) \n
		This command defines the length of a segment for segmented data capture.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select external of IF power trigger source (TRIGger[:SEQuence]:SOURce<ant>) .
			- Turn on segmented capture ([SENSe:]SWEep:SCAPture:STATe) . \n
			:param length: Unit: s
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'SENSe:SWEep:SCAPture:LENGth:TIME {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:SCAPture:LENGth[:TIME] \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.sweep.scapture.length.time.get() \n
		This command defines the length of a segment for segmented data capture.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select external of IF power trigger source (TRIGger[:SEQuence]:SOURce<ant>) .
			- Turn on segmented capture ([SENSe:]SWEep:SCAPture:STATe) . \n
			:return: length: Unit: s"""
		response = self._core.io.query_str(f'SENSe:SWEep:SCAPture:LENGth:TIME?')
		return Conversions.str_to_float(response)
