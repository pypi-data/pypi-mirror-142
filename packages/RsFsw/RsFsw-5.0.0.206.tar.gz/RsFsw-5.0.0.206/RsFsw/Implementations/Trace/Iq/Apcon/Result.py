from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> float:
		"""SCPI: TRACe:IQ:APCon:RESult \n
		Snippet: value: float = driver.trace.iq.apcon.result.get() \n
		Queries the average power consumption for an analog baseband input. This value is only calculated at the end of the I/Q
		data measurement if the method RsFsw.Trace.Iq.Apcon.State.set command is set to ON before the measurement is performed!
		For details see 'Average power consumption'. \n
			:return: average: numeric value Unit: W"""
		response = self._core.io.query_str(f'TRACe:IQ:APCon:RESult?')
		return Conversions.str_to_float(response)
