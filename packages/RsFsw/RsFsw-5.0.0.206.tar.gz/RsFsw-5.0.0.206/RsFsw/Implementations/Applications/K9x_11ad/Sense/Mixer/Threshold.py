from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Threshold:
	"""Threshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("threshold", core, parent)

	def set(self, threshold: float) -> None:
		"""SCPI: [SENSe]:MIXer:THReshold \n
		Snippet: driver.applications.k9X11Ad.sense.mixer.threshold.set(threshold = 1.0) \n
		This command defines the maximum permissible level difference between test sweep and reference sweep to be corrected
		during automatic comparison (see [SENSe:]MIXer<x>:SIGNal) . \n
			:param threshold: No help available
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'SENSe:MIXer:THReshold {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:THReshold \n
		Snippet: value: float = driver.applications.k9X11Ad.sense.mixer.threshold.get() \n
		This command defines the maximum permissible level difference between test sweep and reference sweep to be corrected
		during automatic comparison (see [SENSe:]MIXer<x>:SIGNal) . \n
			:return: threshold: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:THReshold?')
		return Conversions.str_to_float(response)
