from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DutGain:
	"""DutGain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dutGain", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: CONFigure:GENerator:MCGD:LEVel:DUTGain \n
		Snippet: driver.applications.k17Mcgd.configure.generator.mcgd.level.dutGain.set(level = 1.0) \n
		A gain due to the DUT is taken into consideration when determining the reference level on the R&S FSW and the signal
		level on the generator during the reference calibration. \n
			:param level: Unit: dB
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:GENerator:MCGD:LEVel:DUTGain {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:MCGD:LEVel:DUTGain \n
		Snippet: value: float = driver.applications.k17Mcgd.configure.generator.mcgd.level.dutGain.get() \n
		A gain due to the DUT is taken into consideration when determining the reference level on the R&S FSW and the signal
		level on the generator during the reference calibration. \n
			:return: level: Unit: dB"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:LEVel:DUTGain?')
		return Conversions.str_to_float(response)
