from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SoFail:
	"""SoFail commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("soFail", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:SYNC:SOFail \n
		Snippet: driver.applications.k18AmplifierEt.configure.sync.soFail.set(state = False) \n
		This command turns a measurement stop on and off, when synchronization of measured and reference signal fails.
		This mostly has an effect on continuous measurements. Single measurements are not affected. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:SYNC:SOFail {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:SYNC:SOFail \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.sync.soFail.get() \n
		This command turns a measurement stop on and off, when synchronization of measured and reference signal fails.
		This mostly has an effect on continuous measurements. Single measurements are not affected. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:SYNC:SOFail?')
		return Conversions.str_to_bool(response)
