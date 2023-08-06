from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Polynomial:
	"""Polynomial commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("polynomial", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:DPD:POLYnomial \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.dpd.polynomial.get() \n
		This command queries the polynomial factors of the correctional polynomial.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) .
			- Run polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.File.Generate.set) . \n
			:return: values: List of numerical values. The number of values depends on the DPD configuration. The real and imaginary parts of the DPD coefficients are returned interleaved in the following order: real(a0) , imag(a0) , real(a1) , imag(a1) , …"""
		response = self._core.io.query_str(f'FETCh:DPD:POLYnomial?')
		return Conversions.str_to_float(response)
