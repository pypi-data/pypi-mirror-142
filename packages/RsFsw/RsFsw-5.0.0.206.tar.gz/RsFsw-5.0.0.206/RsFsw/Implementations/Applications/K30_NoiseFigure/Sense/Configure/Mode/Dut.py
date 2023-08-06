from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dut:
	"""Dut commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dut", core, parent)

	def set(self, dut_type: enums.DutType) -> None:
		"""SCPI: [SENSe]:CONFigure:MODE:DUT \n
		Snippet: driver.applications.k30NoiseFigure.sense.configure.mode.dut.set(dut_type = enums.DutType.AMPLifier) \n
		This command selects the type of DUT you are testing. Note that you have to use [SENSe:]CONFigure:MODE:SYSTem:LO to
		select if the LO or IF are fixed. \n
			:param dut_type: AMPLifier | DDOWnconv | DOWNconv | UPConv AMPLifier Measurements on fixed frequency DUTs. DOWNconv Measurements on down-converting DUTs. UPConv Measurements on up-converting DUTs.
		"""
		param = Conversions.enum_scalar_to_str(dut_type, enums.DutType)
		self._core.io.write(f'SENSe:CONFigure:MODE:DUT {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DutType:
		"""SCPI: [SENSe]:CONFigure:MODE:DUT \n
		Snippet: value: enums.DutType = driver.applications.k30NoiseFigure.sense.configure.mode.dut.get() \n
		This command selects the type of DUT you are testing. Note that you have to use [SENSe:]CONFigure:MODE:SYSTem:LO to
		select if the LO or IF are fixed. \n
			:return: dut_type: AMPLifier | DDOWnconv | DOWNconv | UPConv AMPLifier Measurements on fixed frequency DUTs. DOWNconv Measurements on down-converting DUTs. UPConv Measurements on up-converting DUTs."""
		response = self._core.io.query_str(f'SENSe:CONFigure:MODE:DUT?')
		return Conversions.str_to_scalar_enum(response, enums.DutType)
