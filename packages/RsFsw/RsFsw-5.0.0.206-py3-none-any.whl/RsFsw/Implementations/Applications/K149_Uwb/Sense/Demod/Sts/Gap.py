from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gap:
	"""Gap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gap", core, parent)

	def set(self, sts_gap: float) -> None:
		"""SCPI: [SENSe]:DEMod:STS:GAP \n
		Snippet: driver.applications.k149Uwb.sense.demod.sts.gap.set(sts_gap = 1.0) \n
		Gap between payload and STS section in packet configuration 2. \n
			:param sts_gap: numeric value
		"""
		param = Conversions.decimal_value_to_str(sts_gap)
		self._core.io.write(f'SENSe:DEMod:STS:GAP {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:STS:GAP \n
		Snippet: value: float = driver.applications.k149Uwb.sense.demod.sts.gap.get() \n
		Gap between payload and STS section in packet configuration 2. \n
			:return: sts_gap: numeric value"""
		response = self._core.io.query_str(f'SENSe:DEMod:STS:GAP?')
		return Conversions.str_to_float(response)
