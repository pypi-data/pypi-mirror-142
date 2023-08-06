from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alpha:
	"""Alpha commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alpha", core, parent)

	def set(self, meas_filter_alpha_bt: float) -> None:
		"""SCPI: [SENSe]:DDEMod:FILTer:ALPHa \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.filterPy.alpha.set(meas_filter_alpha_bt = 1.0) \n
		This command determines the filter characteristic (ALPHA/BT) . \n
			:param meas_filter_alpha_bt: Range: 0.03 to 1.0
		"""
		param = Conversions.decimal_value_to_str(meas_filter_alpha_bt)
		self._core.io.write(f'SENSe:DDEMod:FILTer:ALPHa {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:FILTer:ALPHa \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.filterPy.alpha.get() \n
		This command determines the filter characteristic (ALPHA/BT) . \n
			:return: meas_filter_alpha_bt: Range: 0.03 to 1.0"""
		response = self._core.io.query_str(f'SENSe:DDEMod:FILTer:ALPHa?')
		return Conversions.str_to_float(response)
