from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sband:
	"""Sband commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sband", core, parent)

	def set(self, sideband_pos: enums.SidebandPos) -> None:
		"""SCPI: [SENSe]:DDEMod:SBANd \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.sband.set(sideband_pos = enums.SidebandPos.INVerse) \n
		This command selects the sideband for the demodulation. Note that this command is maintained for compatibility reasons
		only. Use the SENS:SWAP:IQ command for new remote control programs (see [SENSe:]SWAPiq) . \n
			:param sideband_pos: NORMal | INVerse NORMal Normal (non-inverted) position INVerse Inverted position
		"""
		param = Conversions.enum_scalar_to_str(sideband_pos, enums.SidebandPos)
		self._core.io.write(f'SENSe:DDEMod:SBANd {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SidebandPos:
		"""SCPI: [SENSe]:DDEMod:SBANd \n
		Snippet: value: enums.SidebandPos = driver.applications.k70Vsa.sense.ddemod.sband.get() \n
		This command selects the sideband for the demodulation. Note that this command is maintained for compatibility reasons
		only. Use the SENS:SWAP:IQ command for new remote control programs (see [SENSe:]SWAPiq) . \n
			:return: sideband_pos: NORMal | INVerse NORMal Normal (non-inverted) position INVerse Inverted position"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SBANd?')
		return Conversions.str_to_scalar_enum(response, enums.SidebandPos)
