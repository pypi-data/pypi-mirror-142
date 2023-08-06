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

	def set(self, reference: enums.DetectReferenceB) -> None:
		"""SCPI: [SENSe]:DETect:REFerence \n
		Snippet: driver.applications.k6Pulse.sense.detect.reference.set(reference = enums.DetectReferenceB.ABSolute) \n
		The reference level to be used for setting the pulse detection threshold. \n
			:param reference: REFLevel | PEAK | NOISe | ABSolute REFLevel Current reference level PEAK Peak level as measured over the entire capture data interval NOISe Noise level determined from the current capture data according to [SENSe:]TRACe:MEASurement:DEFine:DURation:MIN. ABSolute Absolute level defined by [SENSe:]DETect:THReshold.
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.DetectReferenceB)
		self._core.io.write(f'SENSe:DETect:REFerence {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DetectReferenceB:
		"""SCPI: [SENSe]:DETect:REFerence \n
		Snippet: value: enums.DetectReferenceB = driver.applications.k6Pulse.sense.detect.reference.get() \n
		The reference level to be used for setting the pulse detection threshold. \n
			:return: reference: REFLevel | PEAK | NOISe | ABSolute REFLevel Current reference level PEAK Peak level as measured over the entire capture data interval NOISe Noise level determined from the current capture data according to [SENSe:]TRACe:MEASurement:DEFine:DURation:MIN. ABSolute Absolute level defined by [SENSe:]DETect:THReshold."""
		response = self._core.io.query_str(f'SENSe:DETect:REFerence?')
		return Conversions.str_to_scalar_enum(response, enums.DetectReferenceB)
