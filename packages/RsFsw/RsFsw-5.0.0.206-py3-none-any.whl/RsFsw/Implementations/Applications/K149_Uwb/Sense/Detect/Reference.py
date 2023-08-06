from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	def set(self, reference: enums.DetectReference) -> None:
		"""SCPI: [SENSe]:DETect:REFerence \n
		Snippet: driver.applications.k149Uwb.sense.detect.reference.set(reference = enums.DetectReference.ABSolute) \n
		Sets the reference level to be used for setting the burst detection threshold. \n
			:param reference: ABSolute | NOISe | PEAK | RLEVel
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.DetectReference)
		self._core.io.write(f'SENSe:DETect:REFerence {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DetectReference:
		"""SCPI: [SENSe]:DETect:REFerence \n
		Snippet: value: enums.DetectReference = driver.applications.k149Uwb.sense.detect.reference.get() \n
		Sets the reference level to be used for setting the burst detection threshold. \n
			:return: reference: ABSolute | NOISe | PEAK | RLEVel"""
		response = self._core.io.query_str(f'SENSe:DETect:REFerence?')
		return Conversions.str_to_scalar_enum(response, enums.DetectReference)
