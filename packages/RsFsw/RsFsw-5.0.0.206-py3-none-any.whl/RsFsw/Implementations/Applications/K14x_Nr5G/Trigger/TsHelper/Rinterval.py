from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rinterval:
	"""Rinterval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rinterval", core, parent)

	def set(self, interval: float) -> None:
		"""SCPI: TRIGger:TSHelper:RINTerval \n
		Snippet: driver.applications.k14Xnr5G.trigger.tsHelper.rinterval.set(interval = 1.0) \n
		This command defines the recalibration interval for combined measurements.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select time trigger (method RsFsw.Applications.K14x_Nr5G.Trigger.TsHelper.Sequence.set) . \n
			:param interval: No help available
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'TRIGger:TSHelper:RINTerval {param}')

	def get(self) -> float:
		"""SCPI: TRIGger:TSHelper:RINTerval \n
		Snippet: value: float = driver.applications.k14Xnr5G.trigger.tsHelper.rinterval.get() \n
		This command defines the recalibration interval for combined measurements.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select time trigger (method RsFsw.Applications.K14x_Nr5G.Trigger.TsHelper.Sequence.set) . \n
			:return: interval: No help available"""
		response = self._core.io.query_str(f'TRIGger:TSHelper:RINTerval?')
		return Conversions.str_to_float(response)
