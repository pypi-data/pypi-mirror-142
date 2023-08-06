from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Predicted:
	"""Predicted commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("predicted", core, parent)

	def export(self, filename: str) -> None:
		"""SCPI: [SENSe]:FPLan:PREDicted:EXPort \n
		Snippet: driver.applications.k50Spurious.sense.fplan.predicted.export(filename = '1') \n
		Saves the current predicted list to a .csv file. \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:FPLan:PREDicted:EXPort {param}')
