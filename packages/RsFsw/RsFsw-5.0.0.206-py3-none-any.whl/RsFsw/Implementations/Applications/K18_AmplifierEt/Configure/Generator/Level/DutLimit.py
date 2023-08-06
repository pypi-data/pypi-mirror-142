from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DutLimit:
	"""DutLimit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dutLimit", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: CONFigure:GENerator:LEVel:DUTLimit \n
		Snippet: driver.applications.k18AmplifierEt.configure.generator.level.dutLimit.set(value = 1.0) \n
		This command defines the output power RMS level of the generator. \n
			:param value: numeric value Unit: dB
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:GENerator:LEVel:DUTLimit {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:LEVel:DUTLimit \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.generator.level.dutLimit.get() \n
		This command defines the output power RMS level of the generator. \n
			:return: value: numeric value Unit: dB"""
		response = self._core.io.query_str(f'CONFigure:GENerator:LEVel:DUTLimit?')
		return Conversions.str_to_float(response)
