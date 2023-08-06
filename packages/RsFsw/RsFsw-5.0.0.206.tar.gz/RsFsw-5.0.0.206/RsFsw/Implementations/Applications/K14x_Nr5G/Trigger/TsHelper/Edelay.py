from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Edelay:
	"""Edelay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edelay", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: TRIGger:TSHelper:EDELay \n
		Snippet: driver.applications.k14Xnr5G.trigger.tsHelper.edelay.set(time = 1.0) \n
		This command defines the event delay for combined measurements.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select periodic sequence (method RsFsw.Applications.K14x_Nr5G.Trigger.TsHelper.Sequence.set) . \n
			:param time: Unit: s
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'TRIGger:TSHelper:EDELay {param}')

	def get(self) -> float:
		"""SCPI: TRIGger:TSHelper:EDELay \n
		Snippet: value: float = driver.applications.k14Xnr5G.trigger.tsHelper.edelay.get() \n
		This command defines the event delay for combined measurements.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select periodic sequence (method RsFsw.Applications.K14x_Nr5G.Trigger.TsHelper.Sequence.set) . \n
			:return: time: Unit: s"""
		response = self._core.io.query_str(f'TRIGger:TSHelper:EDELay?')
		return Conversions.str_to_float(response)
