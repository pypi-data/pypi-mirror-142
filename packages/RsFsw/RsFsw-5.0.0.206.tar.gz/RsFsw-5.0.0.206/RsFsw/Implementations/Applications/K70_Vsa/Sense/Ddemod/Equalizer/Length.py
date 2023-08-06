from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: float) -> None:
		"""SCPI: [SENSe]:DDEMod:EQUalizer:LENGth \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.equalizer.length.set(length = 1.0) \n
		This command defines the length of the equalizer in terms of symbols. \n
			:param length: Range: 1 to 256, Unit: SYMB
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'SENSe:DDEMod:EQUalizer:LENGth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:EQUalizer:LENGth \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.equalizer.length.get() \n
		This command defines the length of the equalizer in terms of symbols. \n
			:return: length: Range: 1 to 256, Unit: SYMB"""
		response = self._core.io.query_str(f'SENSe:DDEMod:EQUalizer:LENGth?')
		return Conversions.str_to_float(response)
