from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Multiplier:
	"""Multiplier commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiplier", core, parent)

	def set(self, multiplier: float) -> None:
		"""SCPI: CONFigure:PAE:QCHannel:MULTiplier \n
		Snippet: driver.applications.k18AmplifierEt.configure.pae.qchannel.multiplier.set(multiplier = 1.0) \n
		This command defines a multiplier to take into account various effects resulting from the measurement equipment connected
		to the Q channel. \n
			:param multiplier: numeric value
		"""
		param = Conversions.decimal_value_to_str(multiplier)
		self._core.io.write(f'CONFigure:PAE:QCHannel:MULTiplier {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:PAE:QCHannel:MULTiplier \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.pae.qchannel.multiplier.get() \n
		This command defines a multiplier to take into account various effects resulting from the measurement equipment connected
		to the Q channel. \n
			:return: multiplier: numeric value"""
		response = self._core.io.query_str(f'CONFigure:PAE:QCHannel:MULTiplier?')
		return Conversions.str_to_float(response)
