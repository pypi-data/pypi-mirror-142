from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequence:
	"""Sequence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequence", core, parent)

	def set(self, state: enums.DpdOrder) -> None:
		"""SCPI: CONFigure:MODeling:SEQuence \n
		Snippet: driver.applications.k18AmplifierEt.configure.modeling.sequence.set(state = enums.DpdOrder.AMFirst) \n
		This command selects the sequence in which the models are calculated. \n
			:param state: AMFirst Calculates the AM/AM model before calculating the AM/PM model. PMFirst Calculates the AM/PM model before calculating the AM/AM model.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.DpdOrder)
		self._core.io.write(f'CONFigure:MODeling:SEQuence {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DpdOrder:
		"""SCPI: CONFigure:MODeling:SEQuence \n
		Snippet: value: enums.DpdOrder = driver.applications.k18AmplifierEt.configure.modeling.sequence.get() \n
		This command selects the sequence in which the models are calculated. \n
			:return: state: AMFirst Calculates the AM/AM model before calculating the AM/PM model. PMFirst Calculates the AM/PM model before calculating the AM/AM model."""
		response = self._core.io.query_str(f'CONFigure:MODeling:SEQuence?')
		return Conversions.str_to_scalar_enum(response, enums.DpdOrder)
