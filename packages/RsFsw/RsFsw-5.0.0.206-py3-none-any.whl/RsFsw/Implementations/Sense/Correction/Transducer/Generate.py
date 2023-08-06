from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generate:
	"""Generate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generate", core, parent)

	def set(self, name: str) -> None:
		"""SCPI: [SENSe]:CORRection:TRANsducer:GENerate \n
		Snippet: driver.sense.correction.transducer.generate.set(name = '1') \n
		This command uses the normalized measurement data to generate a transducer factor with up to 1001 points. The trace data
		is converted to a transducer with unit dB and stored in a file with the specified name and the suffix .
		trd under C:/Program Files (x86) /Rohde-Schwarz/FSW/<version>/trd. The frequency points are allocated in equidistant
		steps between start and stop frequency. The generated transducer factor can be further adapted using the commands
		described in 'Working with Transducers') . This command is only valid if External Generator Control (R&S FSW-B10) is
		installed and active and normalization is switched on. \n
			:param name: 'name'
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SENSe:CORRection:TRANsducer:GENerate {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:CORRection:TRANsducer:GENerate \n
		Snippet: value: str = driver.sense.correction.transducer.generate.get() \n
		This command uses the normalized measurement data to generate a transducer factor with up to 1001 points. The trace data
		is converted to a transducer with unit dB and stored in a file with the specified name and the suffix .
		trd under C:/Program Files (x86) /Rohde-Schwarz/FSW/<version>/trd. The frequency points are allocated in equidistant
		steps between start and stop frequency. The generated transducer factor can be further adapted using the commands
		described in 'Working with Transducers') . This command is only valid if External Generator Control (R&S FSW-B10) is
		installed and active and normalization is switched on. \n
			:return: name: 'name'"""
		response = self._core.io.query_str(f'SENSe:CORRection:TRANsducer:GENerate?')
		return trim_str_response(response)
