from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preamble:
	"""Preamble commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preamble", core, parent)

	def set(self, mode: enums.PreambeTrackMode) -> None:
		"""SCPI: [SENSe]:TRACking:PREamble \n
		Snippet: driver.applications.k91Wlan.sense.tracking.preamble.set(mode = enums.PreambeTrackMode.PAYLoad) \n
		Defines which results are used for preamble tracking prior to the preamble channel estimation. \n
			:param mode: PAYLoad Payload tracking results are used for preamble tracking prior to the preamble channel estimation VHT (V) HT-LTF Symbols and Payload tracking results are used for preamble tracking prior to the preamble channel estimation.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PreambeTrackMode)
		self._core.io.write(f'SENSe:TRACking:PREamble {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PreambeTrackMode:
		"""SCPI: [SENSe]:TRACking:PREamble \n
		Snippet: value: enums.PreambeTrackMode = driver.applications.k91Wlan.sense.tracking.preamble.get() \n
		Defines which results are used for preamble tracking prior to the preamble channel estimation. \n
			:return: mode: PAYLoad Payload tracking results are used for preamble tracking prior to the preamble channel estimation VHT (V) HT-LTF Symbols and Payload tracking results are used for preamble tracking prior to the preamble channel estimation."""
		response = self._core.io.query_str(f'SENSe:TRACking:PREamble?')
		return Conversions.str_to_scalar_enum(response, enums.PreambeTrackMode)
