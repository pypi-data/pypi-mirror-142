from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Oversampling:
	"""Oversampling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oversampling", core, parent)

	def set(self, ov_factor: enums.OversampleFactor) -> None:
		"""SCPI: [SENSe]:CAPTure:OVERsampling \n
		Snippet: driver.applications.k149Uwb.sense.capture.oversampling.set(ov_factor = enums.OversampleFactor.OV10) \n
		Sets the oversampling factor. \n
			:param ov_factor: OV4 | OV6 | OV8 | OV10 | OV12
		"""
		param = Conversions.enum_scalar_to_str(ov_factor, enums.OversampleFactor)
		self._core.io.write(f'SENSe:CAPTure:OVERsampling {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.OversampleFactor:
		"""SCPI: [SENSe]:CAPTure:OVERsampling \n
		Snippet: value: enums.OversampleFactor = driver.applications.k149Uwb.sense.capture.oversampling.get() \n
		Sets the oversampling factor. \n
			:return: ov_factor: OV4 | OV6 | OV8 | OV10 | OV12"""
		response = self._core.io.query_str(f'SENSe:CAPTure:OVERsampling?')
		return Conversions.str_to_scalar_enum(response, enums.OversampleFactor)
