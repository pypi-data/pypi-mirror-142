from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaReference:
	"""CaReference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caReference", core, parent)

	def set(self, reference: enums.FrCharReference) -> None:
		"""SCPI: UNIT:CAReference \n
		Snippet: driver.applications.k14Xnr5G.unit.caReference.set(reference = enums.FrCharReference.LRB) \n
		This command selects the reference for result displays whose x-axis shows frequency characteristics of the signal. \n
			:param reference: LRB Frequency values relative to the lowest resource block. RTCF Frequency values relative to the center frequency of the carrier.
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.FrCharReference)
		self._core.io.write(f'UNIT:CAReference {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FrCharReference:
		"""SCPI: UNIT:CAReference \n
		Snippet: value: enums.FrCharReference = driver.applications.k14Xnr5G.unit.caReference.get() \n
		This command selects the reference for result displays whose x-axis shows frequency characteristics of the signal. \n
			:return: reference: LRB Frequency values relative to the lowest resource block. RTCF Frequency values relative to the center frequency of the carrier."""
		response = self._core.io.query_str(f'UNIT:CAReference?')
		return Conversions.str_to_scalar_enum(response, enums.FrCharReference)
