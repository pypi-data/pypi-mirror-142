from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StAdjust:
	"""StAdjust commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stAdjust", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:STADjust \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.stAdjust.set(value = 1.0) \n
		This command defines the symbol time adjustment. \n
			:param value: Range: 0 to 100, Unit: PCT
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'SENSe:NR5G:DEMod:STADjust {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:NR5G:DEMod:STADjust \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.demod.stAdjust.get() \n
		This command defines the symbol time adjustment. \n
			:return: value: Range: 0 to 100, Unit: PCT"""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:STADjust?')
		return Conversions.str_to_float(response)
