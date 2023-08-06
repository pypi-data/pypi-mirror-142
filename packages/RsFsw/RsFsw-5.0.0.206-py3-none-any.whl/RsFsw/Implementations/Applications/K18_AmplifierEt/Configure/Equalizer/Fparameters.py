from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fparameters:
	"""Fparameters commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fparameters", core, parent)

	def set(self, coefficient: List[float]) -> None:
		"""SCPI: CONFigure:EQUalizer:FPARameters \n
		Snippet: driver.applications.k18AmplifierEt.configure.equalizer.fparameters.set(coefficient = [1.1, 2.2, 3.3]) \n
		This command defines the filter coefficients. You can use this command to define the filter coefficients manually instead
		of training a filter. \n
			:param coefficient: numeric value (integer only) List of comma separated values. Each coefficient consists of a real and an imaginary value. Coefficient_1_I,Coefficient_2_Q,Coefficient_2_I,Coefficient_2_Q,...,Coefficient_n_I,Coefficient_n_Q
		"""
		param = Conversions.list_to_csv_str(coefficient)
		self._core.io.write(f'CONFigure:EQUalizer:FPARameters {param}')

	def get(self) -> List[float]:
		"""SCPI: CONFigure:EQUalizer:FPARameters \n
		Snippet: value: List[float] = driver.applications.k18AmplifierEt.configure.equalizer.fparameters.get() \n
		This command defines the filter coefficients. You can use this command to define the filter coefficients manually instead
		of training a filter. \n
			:return: coefficient: numeric value (integer only) List of comma separated values. Each coefficient consists of a real and an imaginary value. Coefficient_1_I,Coefficient_2_Q,Coefficient_2_I,Coefficient_2_Q,...,Coefficient_n_I,Coefficient_n_Q"""
		response = self._core.io.query_bin_or_ascii_float_list(f'CONFigure:EQUalizer:FPARameters?')
		return response
