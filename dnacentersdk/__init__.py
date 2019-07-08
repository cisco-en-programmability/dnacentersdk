# -*- coding: utf-8 -*-
"""Community-developed Python SDK for the DNA Center APIs.

Copyright (c) 2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import logging

from ._metadata import *
from ._version import get_versions
from .api import DNACenterAPI
from .exceptions import (
    AccessTokenError, ApiError, MalformedResponse, MalformedRequest, RateLimitError, DownloadFailure,
    RateLimitWarning, dnacentersdkException,
)
from .models.mydict import mydict_data_factory

from .models.schema_validator import (
    JSONSchemaValidator00AeC9B1422AB27E,
    JSONSchemaValidator01B09A254B9AB259,
    JSONSchemaValidator109D1B4F4289Aecd,
    JSONSchemaValidator6099Da82477B858A,
    JSONSchemaValidator7781Fa0548A98342,
    JSONSchemaValidator9480Fa1F47Ca9254,
    JSONSchemaValidatorA7B42836408A8E74,
    JSONSchemaValidatorF393Abe84989Bb48,
    JSONSchemaValidatorC8Bf6B65414A9Bc7,
    JSONSchemaValidator62B05B2C40A9B216,
    JSONSchemaValidator83A3B9404Cb88787,
    JSONSchemaValidatorF6B119Ad4D4AAf16,
    JSONSchemaValidator9C9A785741CbB41F,
    JSONSchemaValidatorD0A1Abfa435B841D,
    JSONSchemaValidator00A2Fa6146089317,
    JSONSchemaValidator1399891C42A8Be64,
    JSONSchemaValidator429C28154BdaA13D,
    JSONSchemaValidator2E9DB85840FbB1Cf,
    JSONSchemaValidator4695090D403B8Eaa,
    JSONSchemaValidator45Bc7A8344A8Bc1E,
    JSONSchemaValidator4D86A993469A9Da9,
    JSONSchemaValidator8091A9B84BfbA53B,
    JSONSchemaValidatorC1A359B14C89B573,
    JSONSchemaValidatorEab7Abe048Fb99Ad,
    JSONSchemaValidatorCaa3Ea704D78B37E,
    JSONSchemaValidatorEe9AAb01487A8896,
    JSONSchemaValidator069D9823451B892D,
    JSONSchemaValidator17929Bc7465BB564,
    JSONSchemaValidator10B06A6A4F7BB3Cb,
    JSONSchemaValidator1Da5Ebdd434AAcfe,
    JSONSchemaValidator47A1B84B4E1B8044,
    JSONSchemaValidator33B799D04D0A8907,
    JSONSchemaValidator3D9B99C343398A27,
    JSONSchemaValidator4D9CA8E2431A8A24,
    JSONSchemaValidator44974Ba5435A801D,
    JSONSchemaValidator4C8CAb5F435A80F4,
    JSONSchemaValidator55B439Dc4239B140,
    JSONSchemaValidator63Bb88B74F59Aa17,
    JSONSchemaValidator6BacB8D14639Bdc7,
    JSONSchemaValidator948EA8194348Bc0B,
    JSONSchemaValidator89B36B4649999D81,
    JSONSchemaValidator99872A134D0A9Fb4,
    JSONSchemaValidator979688084B7BA60D,
    JSONSchemaValidatorA5Ac99774C6BB541,
    JSONSchemaValidator9788B8Fc4418831D,
    JSONSchemaValidatorB68A6Bd8473A9A25,
    JSONSchemaValidatorC1Ba9A424C08A01B,
    JSONSchemaValidatorDb8E09234A988Bab,
    JSONSchemaValidatorA6965B454C9A8663,
    JSONSchemaValidatorF5Ac590C4Ca9975A,
    JSONSchemaValidatorFba0D80747Eb82E8,
    JSONSchemaValidatorBf859Ac64A0BA19C,
    JSONSchemaValidatorC5AcD9Fa4C1A8Abc,
    JSONSchemaValidator58A3699E489B9529,
    JSONSchemaValidator709FDa3C42B8877A,
    JSONSchemaValidator7Aa3Da9D4E098Ef2,
    JSONSchemaValidatorA4967Be64DfaAa1A,
    JSONSchemaValidatorA6B798Ab4AcaA34E,
    JSONSchemaValidatorFf816B8E435897Eb,
    JSONSchemaValidatorF6Ac994F451BA011,
    JSONSchemaValidator26B44Ab04649A183,
    JSONSchemaValidatorA1A9387346Ba92B1,
    JSONSchemaValidatorE78BB8A2449B9Eed,
    JSONSchemaValidatorF5A269C44F2A95Fa,
    JSONSchemaValidatorE487F8D3481B94F2,
    JSONSchemaValidator33Bb2B9D40199E14,
    JSONSchemaValidatorD6B8Ca774739Adf4,
    JSONSchemaValidator3F89Bbfc4F6B8B50,
    JSONSchemaValidator42B6A86E44B8Bdfc,
    JSONSchemaValidator9698C8Ec4A0B8C1A,
    JSONSchemaValidator55Bc3Bf94E38B6Ff,
    JSONSchemaValidator7Ab9A8Bd4F3B86A4,
    JSONSchemaValidator8A9D2B76443B914E,
    JSONSchemaValidatorA395Fae644Ca899C,
    JSONSchemaValidator07913B7F4E1880De,
    JSONSchemaValidator20872Aec43B9Bf50,
    JSONSchemaValidator6896993E41B8Bd7A,
    JSONSchemaValidatorA0Be3A2F47Ab9F3C,
    JSONSchemaValidatorAe86A8C14B5980B7,
    JSONSchemaValidator47Ba59204E0AB742,
    JSONSchemaValidatorDb9F997F4E59Aec1,
    JSONSchemaValidatorC7A6592B4B98A369,
    JSONSchemaValidatorCca098344A489Dfa,
    JSONSchemaValidatorCca519Ba45EbB423,
    JSONSchemaValidator8A96Fb954D09A349,
    JSONSchemaValidator1E80Bb50430B8634,
    JSONSchemaValidatorA4B56A5F478A97Dd,
    JSONSchemaValidatorD0B3593C4A7AAf22,
    JSONSchemaValidator0Db7Da744C0B83D8,
    JSONSchemaValidator1C894B5848EaB214,
    JSONSchemaValidator3B9EF9674429Be4C,
    JSONSchemaValidator20B19B52464B8972,
    JSONSchemaValidator288DF9494F2A9746,
    JSONSchemaValidator38Bd0B884B89A785,
    JSONSchemaValidator349C888443B89A58,
    JSONSchemaValidator3D923B184Dc9A4Ca,
    JSONSchemaValidator4Bb22Af046Fa8F08,
    JSONSchemaValidator4Eb56A614Cc9A2D2,
    JSONSchemaValidator5B8639224Cd88Ea7,
    JSONSchemaValidator5Db21B8E43FaB7D8,
    JSONSchemaValidator70Ad397649E9B4D3,
    JSONSchemaValidator82918A1B4D289C5C,
    JSONSchemaValidator84B37Ae54C59Ab28,
    JSONSchemaValidator81Bb4804405A8D2F,
    JSONSchemaValidator84Ad8B0E42CaB48A,
    JSONSchemaValidator84B33A9E480ABcaf,
    JSONSchemaValidator819F9Aa54FeaB7Bf,
    JSONSchemaValidator8Fa8Eb404A4A8D96,
    JSONSchemaValidatorBa9DC85B4B8A9A17,
    JSONSchemaValidatorC9809B6744F8A502,
    JSONSchemaValidatorB9855Ad54Ae98156,
    JSONSchemaValidatorB7BcAa084E2B90D0,
    JSONSchemaValidatorCd98780F4888A66D,
    JSONSchemaValidatorCd8469E647CaAb0E,
    JSONSchemaValidatorD0A4B88145AaBb51,
    JSONSchemaValidator888F585C49B88441,
    JSONSchemaValidatorD888Ab6D4D59A8C1,
    JSONSchemaValidatorF5947A4C439A8Bf0,
    JSONSchemaValidator8Db939744649A782,
    JSONSchemaValidatorEb8249E34F69B0F1,
    JSONSchemaValidatorF6826A8E41BbA242,
    JSONSchemaValidatorAeb9Eb67460B92Df,
    JSONSchemaValidatorB888792D43BaBa46,
    JSONSchemaValidatorC3B3C9Ef4E6B8A09,
    JSONSchemaValidator89B2Fb144F5BB09B,
    JSONSchemaValidatorF49548C54Be8A3E2,
    JSONSchemaValidatorFfa748Cc44E9A437,
    JSONSchemaValidator17A82Ac94Cf99Ab0,
    JSONSchemaValidator33AaB9B842388023,
    JSONSchemaValidator23896B124Bd8B9Bf,
    JSONSchemaValidator209509D247599E19,
    JSONSchemaValidator92AcDa91406AA050,
    JSONSchemaValidatorD9BdB9034Df99Dba,
    JSONSchemaValidatorEeb168Eb41988E07,
    JSONSchemaValidatorEba669054E08A60E,
    JSONSchemaValidator6284Db4649Aa8D31,
    JSONSchemaValidator9Ba14A9E441B8A60,
    JSONSchemaValidatorB2B8Cb91459AA58F,
    JSONSchemaValidatorB9B48Ac8463A8Aba,
    JSONSchemaValidatorC2B5Fb764D888375,
    JSONSchemaValidatorCa91Da84401ABba1,
    JSONSchemaValidator149AA93B4Ddb80Dd,
    JSONSchemaValidatorE2AdBa7943BaB3E9,
    JSONSchemaValidator0B836B7B4B6A9Fd5,
    JSONSchemaValidator0A9C988445Cb91C8,
    JSONSchemaValidator09B0F9Ce4239Ae10,
    JSONSchemaValidator2499E9Ad42E8Ae5B,
    JSONSchemaValidator1E962Af345B8B59F,
    JSONSchemaValidator21A6Db2540298F55,
    JSONSchemaValidator3086C9624F498B85,
    JSONSchemaValidator3Cb24Acb486B89D2,
    JSONSchemaValidator5889Fb844939A13B,
    JSONSchemaValidator6F9819E84178870C,
    JSONSchemaValidator7989F86846FaAf99,
    JSONSchemaValidator70A479A6462A9496,
    JSONSchemaValidator7E92F9Eb46Db8320,
    JSONSchemaValidator8Da0391947088A5A,
    JSONSchemaValidator848B5A7B4F9B8C12,
    JSONSchemaValidatorA4B6C87A4Ffb9Efa,
    JSONSchemaValidator9E857B5A4A0BBcdb,
    JSONSchemaValidatorAf8D7B0E470B8Ae2,
    JSONSchemaValidatorCdab9B474899Ae06,
    JSONSchemaValidatorAeb4Dad04A99Bbe3,
    JSONSchemaValidatorBab6C9E5440885Cc,
    JSONSchemaValidatorD9A1Fa9C4068B23C,
    JSONSchemaValidator80AcB88E4Ac9Ac6D,
    JSONSchemaValidatorF09319674049A7D4,
    JSONSchemaValidatorE6B3Db8046C99654,
    JSONSchemaValidatorCf9418234D9AB37E,
    JSONSchemaValidatorF3B26B5544CaBab9,
    JSONSchemaValidatorD8A619974A8A8C48,
    JSONSchemaValidator0C8F7A0B49B9Aedd,
    JSONSchemaValidator8Cb6783B4FabA1F4,
    JSONSchemaValidator4Dbe3Bc743A891Bc,
    JSONSchemaValidatorFb9BEb664F2ABa4C,
    JSONSchemaValidatorBc8AAb4746Ca883D,
    JSONSchemaValidator7Fbe4B804879Baa4,
    JSONSchemaValidator828828F44F28Bd0D,
    JSONSchemaValidator2F97E8Fa45F8B2A3,
    JSONSchemaValidatorAc8AE94C4E69A09D,
    json_schema_validate
)


__version__ = get_versions()['version']
del get_versions


# Initialize Package Logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
