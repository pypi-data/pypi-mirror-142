from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: INPut:IQ:FULLscale[:LEVel] \n
		Snippet: driver.applications.k6Pulse.inputPy.iq.fullscale.level.set(value = 1.0) \n
		This command defines the peak voltage at the Baseband Input connector if the full scale level is set to manual mode (see
		method RsFsw.Applications.K10x_Lte.InputPy.Iq.Fullscale.Auto.set) . \n
			:param value: No help available
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'INPut:IQ:FULLscale:LEVel {param}')

	def get(self) -> float:
		"""SCPI: INPut:IQ:FULLscale[:LEVel] \n
		Snippet: value: float = driver.applications.k6Pulse.inputPy.iq.fullscale.level.get() \n
		This command defines the peak voltage at the Baseband Input connector if the full scale level is set to manual mode (see
		method RsFsw.Applications.K10x_Lte.InputPy.Iq.Fullscale.Auto.set) . \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'INPut:IQ:FULLscale:LEVel?')
		return Conversions.str_to_float(response)
