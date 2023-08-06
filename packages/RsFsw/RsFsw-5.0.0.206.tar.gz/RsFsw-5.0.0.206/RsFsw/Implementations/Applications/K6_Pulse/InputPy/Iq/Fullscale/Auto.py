from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INPut:IQ:FULLscale:AUTO \n
		Snippet: driver.applications.k6Pulse.inputPy.iq.fullscale.auto.set(state = False) \n
		This command defines whether the full scale level (i.e. the maximum input power on the Baseband Input connector) is
		defined automatically according to the reference level, or manually. \n
			:param state: ON | 1 Automatic definition OFF | 0 Manual definition according to method RsFsw.Applications.K6_Pulse.InputPy.Iq.Fullscale.Level.set
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:IQ:FULLscale:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: INPut:IQ:FULLscale:AUTO \n
		Snippet: value: bool = driver.applications.k6Pulse.inputPy.iq.fullscale.auto.get() \n
		This command defines whether the full scale level (i.e. the maximum input power on the Baseband Input connector) is
		defined automatically according to the reference level, or manually. \n
			:return: state: ON | 1 Automatic definition OFF | 0 Manual definition according to method RsFsw.Applications.K6_Pulse.InputPy.Iq.Fullscale.Level.set"""
		response = self._core.io.query_str(f'INPut:IQ:FULLscale:AUTO?')
		return Conversions.str_to_bool(response)
