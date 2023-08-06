from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transmission:
	"""Transmission commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transmission", core, parent)

	def set(self, transmission_type: enums.CestTransmType) -> None:
		"""SCPI: [SENSe]:CESTimation:TRANsmission \n
		Snippet: driver.applications.k17Mcgd.sense.cestimation.transmission.set(transmission_type = enums.CestTransmType.OWAY) \n
		Defines the satellite transmission type. This information is necessary to correctly calculate the Max Clock Offset. \n
			:param transmission_type: OWAY One-Way Transmission TWAY Two-Way Transmission
		"""
		param = Conversions.enum_scalar_to_str(transmission_type, enums.CestTransmType)
		self._core.io.write(f'SENSe:CESTimation:TRANsmission {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CestTransmType:
		"""SCPI: [SENSe]:CESTimation:TRANsmission \n
		Snippet: value: enums.CestTransmType = driver.applications.k17Mcgd.sense.cestimation.transmission.get() \n
		Defines the satellite transmission type. This information is necessary to correctly calculate the Max Clock Offset. \n
			:return: transmission_type: OWAY One-Way Transmission TWAY Two-Way Transmission"""
		response = self._core.io.query_str(f'SENSe:CESTimation:TRANsmission?')
		return Conversions.str_to_scalar_enum(response, enums.CestTransmType)
