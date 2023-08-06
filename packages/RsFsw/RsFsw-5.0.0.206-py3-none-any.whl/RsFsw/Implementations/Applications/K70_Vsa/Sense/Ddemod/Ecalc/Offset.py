from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:ECALc:OFFSet \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.ecalc.offset.set(state = False) \n
		Configures the way the VSA application calculates the error vector results for offset QPSK. \n
			:param state: ON | 1 VSA application compensates the delay of the Q component with respect to the I component in the measurement signal as well as the reference signal before calculating the error vector. That means that the error vector contains only one symbol instant per symbol period. OFF | 0 The VSA application subtracts the measured signal from the reference signal to calculate the error vector. This method results in the fact that the error vector contains two symbol instants per symbol period: one that corresponds to the I component and one that corresponds to the Q component.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:ECALc:OFFSet {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:ECALc:OFFSet \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.ecalc.offset.get() \n
		Configures the way the VSA application calculates the error vector results for offset QPSK. \n
			:return: state: ON | 1 VSA application compensates the delay of the Q component with respect to the I component in the measurement signal as well as the reference signal before calculating the error vector. That means that the error vector contains only one symbol instant per symbol period. OFF | 0 The VSA application subtracts the measured signal from the reference signal to calculate the error vector. This method results in the fact that the error vector contains two symbol instants per symbol period: one that corresponds to the I component and one that corresponds to the Q component."""
		response = self._core.io.query_str(f'SENSe:DDEMod:ECALc:OFFSet?')
		return Conversions.str_to_bool(response)
