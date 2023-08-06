from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpath:
	"""Dpath commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpath", core, parent)

	def set(self, arg_0: enums.AutoOrOff) -> None:
		"""SCPI: INPut:DPATh \n
		Snippet: driver.applications.k40PhaseNoise.inputPy.dpath.set(arg_0 = enums.AutoOrOff.AUTO) \n
		Enables or disables the use of the direct path for frequencies close to 0 Hz. \n
			:param arg_0: No help available
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.AutoOrOff)
		self._core.io.write(f'INPut:DPATh {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoOrOff:
		"""SCPI: INPut:DPATh \n
		Snippet: value: enums.AutoOrOff = driver.applications.k40PhaseNoise.inputPy.dpath.get() \n
		Enables or disables the use of the direct path for frequencies close to 0 Hz. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'INPut:DPATh?')
		return Conversions.str_to_scalar_enum(response, enums.AutoOrOff)
