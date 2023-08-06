from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Control:
	"""Control commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("control", core, parent)

	def set(self, mode: enums.AutoManualMode) -> None:
		"""SCPI: [SENSe]:CONFigure:CONTrol \n
		Snippet: driver.applications.k30NoiseFigure.sense.configure.control.set(mode = enums.AutoManualMode.AUTO) \n
		This command selects the measurement mode for the hot and cold power measurements. Note that selecting a noise source
		with resistor characteristics with [SENSe:]CORRection:ENR:CALibration:TYPE or [SENSe:]CORRection:ENR[:MEASurement]:TYPE
		automatically selects manual measurement mode. \n
			:param mode: AUTO | MANual AUTO Performs the Power (Hot) and Power (Cold) measurement in one step. MANual Performs the Power (Hot) and Power (Cold) measurement in two separate steps.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManualMode)
		self._core.io.write(f'SENSe:CONFigure:CONTrol {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoManualMode:
		"""SCPI: [SENSe]:CONFigure:CONTrol \n
		Snippet: value: enums.AutoManualMode = driver.applications.k30NoiseFigure.sense.configure.control.get() \n
		This command selects the measurement mode for the hot and cold power measurements. Note that selecting a noise source
		with resistor characteristics with [SENSe:]CORRection:ENR:CALibration:TYPE or [SENSe:]CORRection:ENR[:MEASurement]:TYPE
		automatically selects manual measurement mode. \n
			:return: mode: AUTO | MANual AUTO Performs the Power (Hot) and Power (Cold) measurement in one step. MANual Performs the Power (Hot) and Power (Cold) measurement in two separate steps."""
		response = self._core.io.query_str(f'SENSe:CONFigure:CONTrol?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
