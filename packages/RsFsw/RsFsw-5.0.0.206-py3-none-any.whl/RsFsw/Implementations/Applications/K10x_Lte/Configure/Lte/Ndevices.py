from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ndevices:
	"""Ndevices commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ndevices", core, parent)

	def set(self, devices: float) -> None:
		"""SCPI: CONFigure[:LTE]:NDEVices \n
		Snippet: driver.applications.k10Xlte.configure.lte.ndevices.set(devices = 1.0) \n
		This command selects the number of R&S FSW used in a time alignment error measurement with carrier aggregation.
		(Note that for uplink time alignment error measurements, the number of devices is always '1'.) \n
			:param devices: 1 Performs a broadband measurement over all component carriers on a single R&S FSW. 2 Performs a measurement on two R&S FSW, each one analyzing a single component carrier.
		"""
		param = Conversions.decimal_value_to_str(devices)
		self._core.io.write(f'CONFigure:LTE:NDEVices {param}')

	def get(self) -> float:
		"""SCPI: CONFigure[:LTE]:NDEVices \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.ndevices.get() \n
		This command selects the number of R&S FSW used in a time alignment error measurement with carrier aggregation.
		(Note that for uplink time alignment error measurements, the number of devices is always '1'.) \n
			:return: devices: 1 Performs a broadband measurement over all component carriers on a single R&S FSW. 2 Performs a measurement on two R&S FSW, each one analyzing a single component carrier."""
		response = self._core.io.query_str(f'CONFigure:LTE:NDEVices?')
		return Conversions.str_to_float(response)
