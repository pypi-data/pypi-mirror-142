from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nstate:
	"""Nstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nstate", core, parent)

	def set(self, qamn_state: float) -> None:
		"""SCPI: [SENSe]:DDEMod:QAM:NSTate \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.qam.nstate.set(qamn_state = 1.0) \n
		This command defines the demodulation order for QAM.
			Table Header: <QAMNSTate> / Order \n
			- 16 / 16QAM
			- 16 / Pi/4-16QAM
			- 32 / 32QAM
			- 32 / Pi/4-32QAM
			- 64 / 64QAM
			- 128 / 128QAM
			- 256 / 256QAM
			- 512 / 512QAM
			- 1024 / 1024QAM \n
			:param qamn_state: No help available
		"""
		param = Conversions.decimal_value_to_str(qamn_state)
		self._core.io.write(f'SENSe:DDEMod:QAM:NSTate {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:QAM:NSTate \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.qam.nstate.get() \n
		This command defines the demodulation order for QAM.
			Table Header: <QAMNSTate> / Order \n
			- 16 / 16QAM
			- 16 / Pi/4-16QAM
			- 32 / 32QAM
			- 32 / Pi/4-32QAM
			- 64 / 64QAM
			- 128 / 128QAM
			- 256 / 256QAM
			- 512 / 512QAM
			- 1024 / 1024QAM \n
			:return: qamn_state: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:QAM:NSTate?')
		return Conversions.str_to_float(response)
