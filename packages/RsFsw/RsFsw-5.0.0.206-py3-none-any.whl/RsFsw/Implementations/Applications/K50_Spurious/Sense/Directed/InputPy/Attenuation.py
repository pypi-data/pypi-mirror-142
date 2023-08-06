from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	def set(self, attenuation: float) -> None:
		"""SCPI: [SENSe]:DIRected:INPut:ATTenuation \n
		Snippet: driver.applications.k50Spurious.sense.directed.inputPy.attenuation.set(attenuation = 1.0) \n
		Defines the RF attenuation for the directed search measurement. \n
			:param attenuation: integer Range: 0 dB to 79 dB, Unit: DB
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'SENSe:DIRected:INPut:ATTenuation {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DIRected:INPut:ATTenuation \n
		Snippet: value: float = driver.applications.k50Spurious.sense.directed.inputPy.attenuation.get() \n
		Defines the RF attenuation for the directed search measurement. \n
			:return: attenuation: integer Range: 0 dB to 79 dB, Unit: DB"""
		response = self._core.io.query_str(f'SENSe:DIRected:INPut:ATTenuation?')
		return Conversions.str_to_float(response)
