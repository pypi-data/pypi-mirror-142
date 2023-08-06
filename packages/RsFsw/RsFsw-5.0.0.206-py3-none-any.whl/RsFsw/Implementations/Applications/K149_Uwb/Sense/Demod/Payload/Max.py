from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Max:
	"""Max commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("max", core, parent)

	def set(self, payload_max: enums.PayloadMax) -> None:
		"""SCPI: [SENSe]:DEMod:PAYLoad:MAX \n
		Snippet: driver.applications.k149Uwb.sense.demod.payload.max.set(payload_max = enums.PayloadMax.S0) \n
		Selects the maximum payload size. \n
			:param payload_max: S0 | S1 | S2
		"""
		param = Conversions.enum_scalar_to_str(payload_max, enums.PayloadMax)
		self._core.io.write(f'SENSe:DEMod:PAYLoad:MAX {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PayloadMax:
		"""SCPI: [SENSe]:DEMod:PAYLoad:MAX \n
		Snippet: value: enums.PayloadMax = driver.applications.k149Uwb.sense.demod.payload.max.get() \n
		Selects the maximum payload size. \n
			:return: payload_max: S0 | S1 | S2"""
		response = self._core.io.query_str(f'SENSe:DEMod:PAYLoad:MAX?')
		return Conversions.str_to_scalar_enum(response, enums.PayloadMax)
