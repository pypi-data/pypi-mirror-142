from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefLevel:
	"""RefLevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refLevel", core, parent)

	def set(self, ref_level: float) -> None:
		"""SCPI: [SENSe]:DIRected:RLEVel \n
		Snippet: driver.applications.k50Spurious.sense.directed.refLevel.set(ref_level = 1.0) \n
		Defines the reference level for the directed search measurement. \n
			:param ref_level: (–10 dBm + RF attenuation – RF preamplifier gain) Range: -130 dBm to max. 30 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(ref_level)
		self._core.io.write(f'SENSe:DIRected:RLEVel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DIRected:RLEVel \n
		Snippet: value: float = driver.applications.k50Spurious.sense.directed.refLevel.get() \n
		Defines the reference level for the directed search measurement. \n
			:return: ref_level: (–10 dBm + RF attenuation – RF preamplifier gain) Range: -130 dBm to max. 30 dBm, Unit: dBm"""
		response = self._core.io.query_str(f'SENSe:DIRected:RLEVel?')
		return Conversions.str_to_float(response)
