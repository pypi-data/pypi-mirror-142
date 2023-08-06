from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cestimation:
	"""Cestimation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cestimation", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DEMod:CESTimation \n
		Snippet: driver.applications.k91Wlan.sense.demod.cestimation.set(state = False) \n
		This command defines whether channel estimation will be done in preamble and payload or only in preamble. The effect of
		this is most noticeable for the EVM measurement results, where the results will be improved when this feature is enabled.
		However, this functionality is not supported by the IEEE 802.11 standard and must be disabled if the results are to be
		measured strictly according to the standard. \n
			:param state: ON | OFF | 1 | 0 ON | 1 The channel estimation is performed in the preamble and the payload. The EVM results can be calculated more accurately. OFF | 0 The channel estimation is performed in the preamble as required in the standard.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DEMod:CESTimation {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DEMod:CESTimation \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.demod.cestimation.get() \n
		This command defines whether channel estimation will be done in preamble and payload or only in preamble. The effect of
		this is most noticeable for the EVM measurement results, where the results will be improved when this feature is enabled.
		However, this functionality is not supported by the IEEE 802.11 standard and must be disabled if the results are to be
		measured strictly according to the standard. \n
			:return: state: ON | OFF | 1 | 0 ON | 1 The channel estimation is performed in the preamble and the payload. The EVM results can be calculated more accurately. OFF | 0 The channel estimation is performed in the preamble as required in the standard."""
		response = self._core.io.query_str(f'SENSe:DEMod:CESTimation?')
		return Conversions.str_to_bool(response)
