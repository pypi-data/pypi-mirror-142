from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Optimize:
	"""Optimize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("optimize", core, parent)

	def set(self, mode: enums.SweepOptimize) -> None:
		"""SCPI: [SENSe]:SWEep:OPTimize \n
		Snippet: driver.applications.k91Wlan.sense.sweep.optimize.set(mode = enums.SweepOptimize.AUTO) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SweepOptimize)
		self._core.io.write(f'SENSe:SWEep:OPTimize {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepOptimize:
		"""SCPI: [SENSe]:SWEep:OPTimize \n
		Snippet: value: enums.SweepOptimize = driver.applications.k91Wlan.sense.sweep.optimize.get() \n
		No command help available \n
			:return: mode: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:OPTimize?')
		return Conversions.str_to_scalar_enum(response, enums.SweepOptimize)
