from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MfRbw:
	"""MfRbw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mfRbw", core, parent)

	def set(self, max_final_rbw: float) -> None:
		"""SCPI: [SENSe]:DIRected:MFRBw \n
		Snippet: driver.applications.k50Spurious.sense.directed.mfRbw.set(max_final_rbw = 1.0) \n
		No command help available \n
			:param max_final_rbw: Range: 1 Hz to 10 MHz , Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(max_final_rbw)
		self._core.io.write(f'SENSe:DIRected:MFRBw {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DIRected:MFRBw \n
		Snippet: value: float = driver.applications.k50Spurious.sense.directed.mfRbw.get() \n
		No command help available \n
			:return: max_final_rbw: Range: 1 Hz to 10 MHz , Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:DIRected:MFRBw?')
		return Conversions.str_to_float(response)
