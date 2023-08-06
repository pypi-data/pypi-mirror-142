from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Xdistrib:
	"""Xdistrib commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("xdistrib", core, parent)

	def set(self, xdistribution: enums.Xdistribution) -> None:
		"""SCPI: FORMat:DEXPort:XDIStrib \n
		Snippet: driver.formatPy.dexport.xdistrib.set(xdistribution = enums.Xdistribution.BINCentered) \n
		Defines how the x-values of the trace are determined in the frequency domain. See 'X-Value of the Sweep point'. \n
			:param xdistribution: STARtstop | BINCentered BINCentered The full measurement span is divided by the number of sweep points to obtain bins. The x-value of the sweep point is defined as the x-value at the center of the bin (bin/2) . STARtstop (Default) : The x-value of the first sweep point corresponds to the starting point of the full measurement span. The x-value of the last sweep point corresponds to the end point of the full measurement span. All other sweep points are divided evenly between the first and last points.
		"""
		param = Conversions.enum_scalar_to_str(xdistribution, enums.Xdistribution)
		self._core.io.write(f'FORMat:DEXPort:XDIStrib {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Xdistribution:
		"""SCPI: FORMat:DEXPort:XDIStrib \n
		Snippet: value: enums.Xdistribution = driver.formatPy.dexport.xdistrib.get() \n
		Defines how the x-values of the trace are determined in the frequency domain. See 'X-Value of the Sweep point'. \n
			:return: xdistribution: STARtstop | BINCentered BINCentered The full measurement span is divided by the number of sweep points to obtain bins. The x-value of the sweep point is defined as the x-value at the center of the bin (bin/2) . STARtstop (Default) : The x-value of the first sweep point corresponds to the starting point of the full measurement span. The x-value of the last sweep point corresponds to the end point of the full measurement span. All other sweep points are divided evenly between the first and last points."""
		response = self._core.io.query_str(f'FORMat:DEXPort:XDIStrib?')
		return Conversions.str_to_scalar_enum(response, enums.Xdistribution)
