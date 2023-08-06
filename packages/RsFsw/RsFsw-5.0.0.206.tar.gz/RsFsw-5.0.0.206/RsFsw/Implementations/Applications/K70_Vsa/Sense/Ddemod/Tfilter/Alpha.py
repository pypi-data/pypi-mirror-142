from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alpha:
	"""Alpha commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alpha", core, parent)

	def set(self, alpha: float) -> None:
		"""SCPI: [SENSe]:DDEMod:TFILter:ALPHa \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.tfilter.alpha.set(alpha = 1.0) \n
		This command determines the TX filter characteristic (ALPHA/BT) . \n
			:param alpha: Range: 0.03 to 1.0
		"""
		param = Conversions.decimal_value_to_str(alpha)
		self._core.io.write(f'SENSe:DDEMod:TFILter:ALPHa {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:TFILter:ALPHa \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.tfilter.alpha.get() \n
		This command determines the TX filter characteristic (ALPHA/BT) . \n
			:return: alpha: Range: 0.03 to 1.0"""
		response = self._core.io.query_str(f'SENSe:DDEMod:TFILter:ALPHa?')
		return Conversions.str_to_float(response)
