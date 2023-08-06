from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class B:
	"""B commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("b", core, parent)

	def set(self, conv_fact: float) -> None:
		"""SCPI: TRACe:IQ:APCon:B \n
		Snippet: driver.trace.iq.apcon.b.set(conv_fact = 1.0) \n
		Defines the conversion factor B for the calculation of the average power consumption. For details see 'Average power
		consumption'. \n
			:param conv_fact: numeric value
		"""
		param = Conversions.decimal_value_to_str(conv_fact)
		self._core.io.write(f'TRACe:IQ:APCon:B {param}')

	def get(self) -> float:
		"""SCPI: TRACe:IQ:APCon:B \n
		Snippet: value: float = driver.trace.iq.apcon.b.get() \n
		Defines the conversion factor B for the calculation of the average power consumption. For details see 'Average power
		consumption'. \n
			:return: conv_fact: numeric value"""
		response = self._core.io.query_str(f'TRACe:IQ:APCon:B?')
		return Conversions.str_to_float(response)
