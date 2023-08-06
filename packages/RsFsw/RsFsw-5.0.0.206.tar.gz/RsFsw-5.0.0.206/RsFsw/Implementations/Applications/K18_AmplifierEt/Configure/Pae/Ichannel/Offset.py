from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset: float) -> None:
		"""SCPI: CONFigure:PAE:ICHannel:OFFSet \n
		Snippet: driver.applications.k18AmplifierEt.configure.pae.ichannel.offset.set(offset = 1.0) \n
		This command defines an offset for the I channel. \n
			:param offset: numeric value Unit: No unit
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:PAE:ICHannel:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:PAE:ICHannel:OFFSet \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.pae.ichannel.offset.get() \n
		This command defines an offset for the I channel. \n
			:return: offset: numeric value Unit: No unit"""
		response = self._core.io.query_str(f'CONFigure:PAE:ICHannel:OFFSet?')
		return Conversions.str_to_float(response)
