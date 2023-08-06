from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Low:
	"""Low commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("low", core, parent)

	def set(self, harm_order: float) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic[:LOW] \n
		Snippet: driver.applications.k70Vsa.sense.mixer.harmonic.low.set(harm_order = 1.0) \n
		This command specifies the harmonic order to be used for the low (first) range. \n
			:param harm_order: Range: 2 to 128 (USER band) ; for other bands: see band definition
		"""
		param = Conversions.decimal_value_to_str(harm_order)
		self._core.io.write(f'SENSe:MIXer:HARMonic:LOW {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:HARMonic[:LOW] \n
		Snippet: value: float = driver.applications.k70Vsa.sense.mixer.harmonic.low.get() \n
		This command specifies the harmonic order to be used for the low (first) range. \n
			:return: harm_order: Range: 2 to 128 (USER band) ; for other bands: see band definition"""
		response = self._core.io.query_str(f'SENSe:MIXer:HARMonic:LOW?')
		return Conversions.str_to_float(response)
