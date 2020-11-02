# -*- coding: utf-8 -*-
"""Validates DNA Center JSON request objects.

Classes:
    SchemaValidator: Validates DNA Center JSON request objects.

The SchemaValidator class validates any dict structure passed by
the user with the JSON schema of the request.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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

from builtins import *
import json

import fastjsonschema
from dnacentersdk.exceptions import MalformedRequest

from .validators.v1_2_10.jsd_00aec9b1422ab27e \
    import JSONSchemaValidator00AeC9B1422AB27E \
    as JSONSchemaValidator00AeC9B1422AB27E_v1_2_10
from .validators.v1_2_10.jsd_7781fa0548a98342 \
    import JSONSchemaValidator7781Fa0548A98342 \
    as JSONSchemaValidator7781Fa0548A98342_v1_2_10
from .validators.v1_2_10.jsd_6099da82477b858a \
    import JSONSchemaValidator6099Da82477B858A \
    as JSONSchemaValidator6099Da82477B858A_v1_2_10
from .validators.v1_2_10.jsd_9480fa1f47ca9254 \
    import JSONSchemaValidator9480Fa1F47Ca9254 \
    as JSONSchemaValidator9480Fa1F47Ca9254_v1_2_10
from .validators.v1_2_10.jsd_62b05b2c40a9b216 \
    import JSONSchemaValidator62B05B2C40A9B216 \
    as JSONSchemaValidator62B05B2C40A9B216_v1_2_10
from .validators.v1_2_10.jsd_f393abe84989bb48 \
    import JSONSchemaValidatorF393Abe84989Bb48 \
    as JSONSchemaValidatorF393Abe84989Bb48_v1_2_10
from .validators.v1_2_10.jsd_f6b119ad4d4aaf16 \
    import JSONSchemaValidatorF6B119Ad4D4AAf16 \
    as JSONSchemaValidatorF6B119Ad4D4AAf16_v1_2_10
from .validators.v1_2_10.jsd_00a2fa6146089317 \
    import JSONSchemaValidator00A2Fa6146089317 \
    as JSONSchemaValidator00A2Fa6146089317_v1_2_10
from .validators.v1_2_10.jsd_1399891c42a8be64 \
    import JSONSchemaValidator1399891C42A8Be64 \
    as JSONSchemaValidator1399891C42A8Be64_v1_2_10
from .validators.v1_2_10.jsd_45bc7a8344a8bc1e \
    import JSONSchemaValidator45Bc7A8344A8Bc1E \
    as JSONSchemaValidator45Bc7A8344A8Bc1E_v1_2_10
from .validators.v1_2_10.jsd_4d86a993469a9da9 \
    import JSONSchemaValidator4D86A993469A9Da9 \
    as JSONSchemaValidator4D86A993469A9Da9_v1_2_10
from .validators.v1_2_10.jsd_17929bc7465bb564 \
    import JSONSchemaValidator17929Bc7465BB564 \
    as JSONSchemaValidator17929Bc7465BB564_v1_2_10
from .validators.v1_2_10.jsd_10b06a6a4f7bb3cb \
    import JSONSchemaValidator10B06A6A4F7BB3Cb \
    as JSONSchemaValidator10B06A6A4F7BB3Cb_v1_2_10
from .validators.v1_2_10.jsd_1da5ebdd434aacfe \
    import JSONSchemaValidator1Da5Ebdd434AAcfe \
    as JSONSchemaValidator1Da5Ebdd434AAcfe_v1_2_10
from .validators.v1_2_10.jsd_55b439dc4239b140 \
    import JSONSchemaValidator55B439Dc4239B140 \
    as JSONSchemaValidator55B439Dc4239B140_v1_2_10
from .validators.v1_2_10.jsd_6bacb8d14639bdc7 \
    import JSONSchemaValidator6BacB8D14639Bdc7 \
    as JSONSchemaValidator6BacB8D14639Bdc7_v1_2_10
from .validators.v1_2_10.jsd_4d9ca8e2431a8a24 \
    import JSONSchemaValidator4D9CA8E2431A8A24 \
    as JSONSchemaValidator4D9CA8E2431A8A24_v1_2_10
from .validators.v1_2_10.jsd_709fda3c42b8877a \
    import JSONSchemaValidator709FDa3C42B8877A \
    as JSONSchemaValidator709FDa3C42B8877A_v1_2_10
from .validators.v1_2_10.jsd_7aa3da9d4e098ef2 \
    import JSONSchemaValidator7Aa3Da9D4E098Ef2 \
    as JSONSchemaValidator7Aa3Da9D4E098Ef2_v1_2_10
from .validators.v1_2_10.jsd_9788b8fc4418831d \
    import JSONSchemaValidator9788B8Fc4418831D \
    as JSONSchemaValidator9788B8Fc4418831D_v1_2_10
from .validators.v1_2_10.jsd_948ea8194348bc0b \
    import JSONSchemaValidator948EA8194348Bc0B \
    as JSONSchemaValidator948EA8194348Bc0B_v1_2_10
from .validators.v1_2_10.jsd_47a1b84b4e1b8044 \
    import JSONSchemaValidator47A1B84B4E1B8044 \
    as JSONSchemaValidator47A1B84B4E1B8044_v1_2_10
from .validators.v1_2_10.jsd_a5ac99774c6bb541 \
    import JSONSchemaValidatorA5Ac99774C6BB541 \
    as JSONSchemaValidatorA5Ac99774C6BB541_v1_2_10
from .validators.v1_2_10.jsd_b68a6bd8473a9a25 \
    import JSONSchemaValidatorB68A6Bd8473A9A25 \
    as JSONSchemaValidatorB68A6Bd8473A9A25_v1_2_10
from .validators.v1_2_10.jsd_bf859ac64a0ba19c \
    import JSONSchemaValidatorBf859Ac64A0BA19C \
    as JSONSchemaValidatorBf859Ac64A0BA19C_v1_2_10
from .validators.v1_2_10.jsd_c5acd9fa4c1a8abc \
    import JSONSchemaValidatorC5AcD9Fa4C1A8Abc \
    as JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v1_2_10
from .validators.v1_2_10.jsd_89b36b4649999d81 \
    import JSONSchemaValidator89B36B4649999D81 \
    as JSONSchemaValidator89B36B4649999D81_v1_2_10
from .validators.v1_2_10.jsd_fba0d80747eb82e8 \
    import JSONSchemaValidatorFba0D80747Eb82E8 \
    as JSONSchemaValidatorFba0D80747Eb82E8_v1_2_10
from .validators.v1_2_10.jsd_979688084b7ba60d \
    import JSONSchemaValidator979688084B7BA60D \
    as JSONSchemaValidator979688084B7BA60D_v1_2_10
from .validators.v1_2_10.jsd_d6b8ca774739adf4 \
    import JSONSchemaValidatorD6B8Ca774739Adf4 \
    as JSONSchemaValidatorD6B8Ca774739Adf4_v1_2_10
from .validators.v1_2_10.jsd_a395fae644ca899c \
    import JSONSchemaValidatorA395Fae644Ca899C \
    as JSONSchemaValidatorA395Fae644Ca899C_v1_2_10
from .validators.v1_2_10.jsd_8cb6783b4faba1f4 \
    import JSONSchemaValidator8Cb6783B4FabA1F4 \
    as JSONSchemaValidator8Cb6783B4FabA1F4_v1_2_10
from .validators.v1_2_10.jsd_bc8aab4746ca883d \
    import JSONSchemaValidatorBc8AAb4746Ca883D \
    as JSONSchemaValidatorBc8AAb4746Ca883D_v1_2_10
from .validators.v1_2_10.jsd_fb9beb664f2aba4c \
    import JSONSchemaValidatorFb9BEb664F2ABa4C \
    as JSONSchemaValidatorFb9BEb664F2ABa4C_v1_2_10
from .validators.v1_2_10.jsd_21a6db2540298f55 \
    import JSONSchemaValidator21A6Db2540298F55 \
    as JSONSchemaValidator21A6Db2540298F55_v1_2_10
from .validators.v1_2_10.jsd_3086c9624f498b85 \
    import JSONSchemaValidator3086C9624F498B85 \
    as JSONSchemaValidator3086C9624F498B85_v1_2_10
from .validators.v1_2_10.jsd_0b836b7b4b6a9fd5 \
    import JSONSchemaValidator0B836B7B4B6A9Fd5 \
    as JSONSchemaValidator0B836B7B4B6A9Fd5_v1_2_10
from .validators.v1_2_10.jsd_1e962af345b8b59f \
    import JSONSchemaValidator1E962Af345B8B59F \
    as JSONSchemaValidator1E962Af345B8B59F_v1_2_10
from .validators.v1_2_10.jsd_09b0f9ce4239ae10 \
    import JSONSchemaValidator09B0F9Ce4239Ae10 \
    as JSONSchemaValidator09B0F9Ce4239Ae10_v1_2_10
from .validators.v1_2_10.jsd_5889fb844939a13b \
    import JSONSchemaValidator5889Fb844939A13B \
    as JSONSchemaValidator5889Fb844939A13B_v1_2_10
from .validators.v1_2_10.jsd_6f9819e84178870c \
    import JSONSchemaValidator6F9819E84178870C \
    as JSONSchemaValidator6F9819E84178870C_v1_2_10
from .validators.v1_2_10.jsd_8da0391947088a5a \
    import JSONSchemaValidator8Da0391947088A5A \
    as JSONSchemaValidator8Da0391947088A5A_v1_2_10
from .validators.v1_2_10.jsd_9e857b5a4a0bbcdb \
    import JSONSchemaValidator9E857B5A4A0BBcdb \
    as JSONSchemaValidator9E857B5A4A0BBcdb_v1_2_10
from .validators.v1_2_10.jsd_a4b6c87a4ffb9efa \
    import JSONSchemaValidatorA4B6C87A4Ffb9Efa \
    as JSONSchemaValidatorA4B6C87A4Ffb9Efa_v1_2_10
from .validators.v1_2_10.jsd_cf9418234d9ab37e \
    import JSONSchemaValidatorCf9418234D9AB37E \
    as JSONSchemaValidatorCf9418234D9AB37E_v1_2_10
from .validators.v1_2_10.jsd_d8a619974a8a8c48 \
    import JSONSchemaValidatorD8A619974A8A8C48 \
    as JSONSchemaValidatorD8A619974A8A8C48_v1_2_10
from .validators.v1_2_10.jsd_848b5a7b4f9b8c12 \
    import JSONSchemaValidator848B5A7B4F9B8C12 \
    as JSONSchemaValidator848B5A7B4F9B8C12_v1_2_10
from .validators.v1_2_10.jsd_f3b26b5544cabab9 \
    import JSONSchemaValidatorF3B26B5544CaBab9 \
    as JSONSchemaValidatorF3B26B5544CaBab9_v1_2_10
from .validators.v1_2_10.jsd_828828f44f28bd0d \
    import JSONSchemaValidator828828F44F28Bd0D \
    as JSONSchemaValidator828828F44F28Bd0D_v1_2_10
from .validators.v1_2_10.jsd_3b9ef9674429be4c \
    import JSONSchemaValidator3B9EF9674429Be4C \
    as JSONSchemaValidator3B9EF9674429Be4C_v1_2_10
from .validators.v1_2_10.jsd_4bb22af046fa8f08 \
    import JSONSchemaValidator4Bb22Af046Fa8F08 \
    as JSONSchemaValidator4Bb22Af046Fa8F08_v1_2_10
from .validators.v1_2_10.jsd_b9855ad54ae98156 \
    import JSONSchemaValidatorB9855Ad54Ae98156 \
    as JSONSchemaValidatorB9855Ad54Ae98156_v1_2_10
from .validators.v1_2_10.jsd_aeb9eb67460b92df \
    import JSONSchemaValidatorAeb9Eb67460B92Df \
    as JSONSchemaValidatorAeb9Eb67460B92Df_v1_2_10
from .validators.v1_2_10.jsd_cd98780f4888a66d \
    import JSONSchemaValidatorCd98780F4888A66D \
    as JSONSchemaValidatorCd98780F4888A66D_v1_2_10
from .validators.v1_2_10.jsd_eeb168eb41988e07 \
    import JSONSchemaValidatorEeb168Eb41988E07 \
    as JSONSchemaValidatorEeb168Eb41988E07_v1_2_10
from .validators.v1_2_10.jsd_50b589fd4c7a930a \
    import JSONSchemaValidator50B589Fd4C7A930A \
    as JSONSchemaValidator50B589Fd4C7A930A_v1_2_10
from .validators.v1_2_10.jsd_8a96fb954d09a349 \
    import JSONSchemaValidator8A96Fb954D09A349 \
    as JSONSchemaValidator8A96Fb954D09A349_v1_2_10
from .validators.v1_2_10.jsd_db9f997f4e59aec1 \
    import JSONSchemaValidatorDb9F997F4E59Aec1 \
    as JSONSchemaValidatorDb9F997F4E59Aec1_v1_2_10
from .validators.v1_2_10.jsd_bead7b3443b996a7 \
    import JSONSchemaValidatorBead7B3443B996A7 \
    as JSONSchemaValidatorBead7B3443B996A7_v1_2_10
from .validators.v1_3_0.jsd_00aec9b1422ab27e \
    import JSONSchemaValidator00AeC9B1422AB27E \
    as JSONSchemaValidator00AeC9B1422AB27E_v1_3_0
from .validators.v1_3_0.jsd_6099da82477b858a \
    import JSONSchemaValidator6099Da82477B858A \
    as JSONSchemaValidator6099Da82477B858A_v1_3_0
from .validators.v1_3_0.jsd_7781fa0548a98342 \
    import JSONSchemaValidator7781Fa0548A98342 \
    as JSONSchemaValidator7781Fa0548A98342_v1_3_0
from .validators.v1_3_0.jsd_9480fa1f47ca9254 \
    import JSONSchemaValidator9480Fa1F47Ca9254 \
    as JSONSchemaValidator9480Fa1F47Ca9254_v1_3_0
from .validators.v1_3_0.jsd_f393abe84989bb48 \
    import JSONSchemaValidatorF393Abe84989Bb48 \
    as JSONSchemaValidatorF393Abe84989Bb48_v1_3_0
from .validators.v1_3_0.jsd_62b05b2c40a9b216 \
    import JSONSchemaValidator62B05B2C40A9B216 \
    as JSONSchemaValidator62B05B2C40A9B216_v1_3_0
from .validators.v1_3_0.jsd_f6b119ad4d4aaf16 \
    import JSONSchemaValidatorF6B119Ad4D4AAf16 \
    as JSONSchemaValidatorF6B119Ad4D4AAf16_v1_3_0
from .validators.v1_3_0.jsd_00a2fa6146089317 \
    import JSONSchemaValidator00A2Fa6146089317 \
    as JSONSchemaValidator00A2Fa6146089317_v1_3_0
from .validators.v1_3_0.jsd_1399891c42a8be64 \
    import JSONSchemaValidator1399891C42A8Be64 \
    as JSONSchemaValidator1399891C42A8Be64_v1_3_0
from .validators.v1_3_0.jsd_45bc7a8344a8bc1e \
    import JSONSchemaValidator45Bc7A8344A8Bc1E \
    as JSONSchemaValidator45Bc7A8344A8Bc1E_v1_3_0
from .validators.v1_3_0.jsd_4d86a993469a9da9 \
    import JSONSchemaValidator4D86A993469A9Da9 \
    as JSONSchemaValidator4D86A993469A9Da9_v1_3_0
from .validators.v1_3_0.jsd_17929bc7465bb564 \
    import JSONSchemaValidator17929Bc7465BB564 \
    as JSONSchemaValidator17929Bc7465BB564_v1_3_0
from .validators.v1_3_0.jsd_10b06a6a4f7bb3cb \
    import JSONSchemaValidator10B06A6A4F7BB3Cb \
    as JSONSchemaValidator10B06A6A4F7BB3Cb_v1_3_0
from .validators.v1_3_0.jsd_1da5ebdd434aacfe \
    import JSONSchemaValidator1Da5Ebdd434AAcfe \
    as JSONSchemaValidator1Da5Ebdd434AAcfe_v1_3_0
from .validators.v1_3_0.jsd_47a1b84b4e1b8044 \
    import JSONSchemaValidator47A1B84B4E1B8044 \
    as JSONSchemaValidator47A1B84B4E1B8044_v1_3_0
from .validators.v1_3_0.jsd_4d9ca8e2431a8a24 \
    import JSONSchemaValidator4D9CA8E2431A8A24 \
    as JSONSchemaValidator4D9CA8E2431A8A24_v1_3_0
from .validators.v1_3_0.jsd_55b439dc4239b140 \
    import JSONSchemaValidator55B439Dc4239B140 \
    as JSONSchemaValidator55B439Dc4239B140_v1_3_0
from .validators.v1_3_0.jsd_6bacb8d14639bdc7 \
    import JSONSchemaValidator6BacB8D14639Bdc7 \
    as JSONSchemaValidator6BacB8D14639Bdc7_v1_3_0
from .validators.v1_3_0.jsd_948ea8194348bc0b \
    import JSONSchemaValidator948EA8194348Bc0B \
    as JSONSchemaValidator948EA8194348Bc0B_v1_3_0
from .validators.v1_3_0.jsd_89b36b4649999d81 \
    import JSONSchemaValidator89B36B4649999D81 \
    as JSONSchemaValidator89B36B4649999D81_v1_3_0
from .validators.v1_3_0.jsd_979688084b7ba60d \
    import JSONSchemaValidator979688084B7BA60D \
    as JSONSchemaValidator979688084B7BA60D_v1_3_0
from .validators.v1_3_0.jsd_a5ac99774c6bb541 \
    import JSONSchemaValidatorA5Ac99774C6BB541 \
    as JSONSchemaValidatorA5Ac99774C6BB541_v1_3_0
from .validators.v1_3_0.jsd_9788b8fc4418831d \
    import JSONSchemaValidator9788B8Fc4418831D \
    as JSONSchemaValidator9788B8Fc4418831D_v1_3_0
from .validators.v1_3_0.jsd_b68a6bd8473a9a25 \
    import JSONSchemaValidatorB68A6Bd8473A9A25 \
    as JSONSchemaValidatorB68A6Bd8473A9A25_v1_3_0
from .validators.v1_3_0.jsd_fba0d80747eb82e8 \
    import JSONSchemaValidatorFba0D80747Eb82E8 \
    as JSONSchemaValidatorFba0D80747Eb82E8_v1_3_0
from .validators.v1_3_0.jsd_bf859ac64a0ba19c \
    import JSONSchemaValidatorBf859Ac64A0BA19C \
    as JSONSchemaValidatorBf859Ac64A0BA19C_v1_3_0
from .validators.v1_3_0.jsd_c5acd9fa4c1a8abc \
    import JSONSchemaValidatorC5AcD9Fa4C1A8Abc \
    as JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v1_3_0
from .validators.v1_3_0.jsd_709fda3c42b8877a \
    import JSONSchemaValidator709FDa3C42B8877A \
    as JSONSchemaValidator709FDa3C42B8877A_v1_3_0
from .validators.v1_3_0.jsd_7aa3da9d4e098ef2 \
    import JSONSchemaValidator7Aa3Da9D4E098Ef2 \
    as JSONSchemaValidator7Aa3Da9D4E098Ef2_v1_3_0
from .validators.v1_3_0.jsd_d6b8ca774739adf4 \
    import JSONSchemaValidatorD6B8Ca774739Adf4 \
    as JSONSchemaValidatorD6B8Ca774739Adf4_v1_3_0
from .validators.v1_3_0.jsd_a395fae644ca899c \
    import JSONSchemaValidatorA395Fae644Ca899C \
    as JSONSchemaValidatorA395Fae644Ca899C_v1_3_0
from .validators.v1_3_0.jsd_07913b7f4e1880de \
    import JSONSchemaValidator07913B7F4E1880De \
    as JSONSchemaValidator07913B7F4E1880De_v1_3_0
from .validators.v1_3_0.jsd_20872aec43b9bf50 \
    import JSONSchemaValidator20872Aec43B9Bf50 \
    as JSONSchemaValidator20872Aec43B9Bf50_v1_3_0
from .validators.v1_3_0.jsd_a0be3a2f47ab9f3c \
    import JSONSchemaValidatorA0Be3A2F47Ab9F3C \
    as JSONSchemaValidatorA0Be3A2F47Ab9F3C_v1_3_0
from .validators.v1_3_0.jsd_47ba59204e0ab742 \
    import JSONSchemaValidator47Ba59204E0AB742 \
    as JSONSchemaValidator47Ba59204E0AB742_v1_3_0
from .validators.v1_3_0.jsd_db9f997f4e59aec1 \
    import JSONSchemaValidatorDb9F997F4E59Aec1 \
    as JSONSchemaValidatorDb9F997F4E59Aec1_v1_3_0
from .validators.v1_3_0.jsd_8a96fb954d09a349 \
    import JSONSchemaValidator8A96Fb954D09A349 \
    as JSONSchemaValidator8A96Fb954D09A349_v1_3_0
from .validators.v1_3_0.jsd_a4b56a5f478a97dd \
    import JSONSchemaValidatorA4B56A5F478A97Dd \
    as JSONSchemaValidatorA4B56A5F478A97Dd_v1_3_0
from .validators.v1_3_0.jsd_3b9ef9674429be4c \
    import JSONSchemaValidator3B9EF9674429Be4C \
    as JSONSchemaValidator3B9EF9674429Be4C_v1_3_0
from .validators.v1_3_0.jsd_4bb22af046fa8f08 \
    import JSONSchemaValidator4Bb22Af046Fa8F08 \
    as JSONSchemaValidator4Bb22Af046Fa8F08_v1_3_0
from .validators.v1_3_0.jsd_b9855ad54ae98156 \
    import JSONSchemaValidatorB9855Ad54Ae98156 \
    as JSONSchemaValidatorB9855Ad54Ae98156_v1_3_0
from .validators.v1_3_0.jsd_cd98780f4888a66d \
    import JSONSchemaValidatorCd98780F4888A66D \
    as JSONSchemaValidatorCd98780F4888A66D_v1_3_0
from .validators.v1_3_0.jsd_aeb9eb67460b92df \
    import JSONSchemaValidatorAeb9Eb67460B92Df \
    as JSONSchemaValidatorAeb9Eb67460B92Df_v1_3_0
from .validators.v1_3_0.jsd_33aab9b842388023 \
    import JSONSchemaValidator33AaB9B842388023 \
    as JSONSchemaValidator33AaB9B842388023_v1_3_0
from .validators.v1_3_0.jsd_23896b124bd8b9bf \
    import JSONSchemaValidator23896B124Bd8B9Bf \
    as JSONSchemaValidator23896B124Bd8B9Bf_v1_3_0
from .validators.v1_3_0.jsd_eeb168eb41988e07 \
    import JSONSchemaValidatorEeb168Eb41988E07 \
    as JSONSchemaValidatorEeb168Eb41988E07_v1_3_0
from .validators.v1_3_0.jsd_0b836b7b4b6a9fd5 \
    import JSONSchemaValidator0B836B7B4B6A9Fd5 \
    as JSONSchemaValidator0B836B7B4B6A9Fd5_v1_3_0
from .validators.v1_3_0.jsd_09b0f9ce4239ae10 \
    import JSONSchemaValidator09B0F9Ce4239Ae10 \
    as JSONSchemaValidator09B0F9Ce4239Ae10_v1_3_0
from .validators.v1_3_0.jsd_1e962af345b8b59f \
    import JSONSchemaValidator1E962Af345B8B59F \
    as JSONSchemaValidator1E962Af345B8B59F_v1_3_0
from .validators.v1_3_0.jsd_21a6db2540298f55 \
    import JSONSchemaValidator21A6Db2540298F55 \
    as JSONSchemaValidator21A6Db2540298F55_v1_3_0
from .validators.v1_3_0.jsd_3086c9624f498b85 \
    import JSONSchemaValidator3086C9624F498B85 \
    as JSONSchemaValidator3086C9624F498B85_v1_3_0
from .validators.v1_3_0.jsd_5889fb844939a13b \
    import JSONSchemaValidator5889Fb844939A13B \
    as JSONSchemaValidator5889Fb844939A13B_v1_3_0
from .validators.v1_3_0.jsd_6f9819e84178870c \
    import JSONSchemaValidator6F9819E84178870C \
    as JSONSchemaValidator6F9819E84178870C_v1_3_0
from .validators.v1_3_0.jsd_8da0391947088a5a \
    import JSONSchemaValidator8Da0391947088A5A \
    as JSONSchemaValidator8Da0391947088A5A_v1_3_0
from .validators.v1_3_0.jsd_848b5a7b4f9b8c12 \
    import JSONSchemaValidator848B5A7B4F9B8C12 \
    as JSONSchemaValidator848B5A7B4F9B8C12_v1_3_0
from .validators.v1_3_0.jsd_a4b6c87a4ffb9efa \
    import JSONSchemaValidatorA4B6C87A4Ffb9Efa \
    as JSONSchemaValidatorA4B6C87A4Ffb9Efa_v1_3_0
from .validators.v1_3_0.jsd_9e857b5a4a0bbcdb \
    import JSONSchemaValidator9E857B5A4A0BBcdb \
    as JSONSchemaValidator9E857B5A4A0BBcdb_v1_3_0
from .validators.v1_3_0.jsd_cf9418234d9ab37e \
    import JSONSchemaValidatorCf9418234D9AB37E \
    as JSONSchemaValidatorCf9418234D9AB37E_v1_3_0
from .validators.v1_3_0.jsd_f3b26b5544cabab9 \
    import JSONSchemaValidatorF3B26B5544CaBab9 \
    as JSONSchemaValidatorF3B26B5544CaBab9_v1_3_0
from .validators.v1_3_0.jsd_d8a619974a8a8c48 \
    import JSONSchemaValidatorD8A619974A8A8C48 \
    as JSONSchemaValidatorD8A619974A8A8C48_v1_3_0
from .validators.v1_3_0.jsd_8cb6783b4faba1f4 \
    import JSONSchemaValidator8Cb6783B4FabA1F4 \
    as JSONSchemaValidator8Cb6783B4FabA1F4_v1_3_0
from .validators.v1_3_0.jsd_fb9beb664f2aba4c \
    import JSONSchemaValidatorFb9BEb664F2ABa4C \
    as JSONSchemaValidatorFb9BEb664F2ABa4C_v1_3_0
from .validators.v1_3_0.jsd_bc8aab4746ca883d \
    import JSONSchemaValidatorBc8AAb4746Ca883D \
    as JSONSchemaValidatorBc8AAb4746Ca883D_v1_3_0
from .validators.v1_3_0.jsd_828828f44f28bd0d \
    import JSONSchemaValidator828828F44F28Bd0D \
    as JSONSchemaValidator828828F44F28Bd0D_v1_3_0
from .validators.v1_3_0.jsd_2f97e8fa45f8b2a3 \
    import JSONSchemaValidator2F97E8Fa45F8B2A3 \
    as JSONSchemaValidator2F97E8Fa45F8B2A3_v1_3_0
from .validators.v1_3_1.jsd_00a2fa6146089317 \
    import JSONSchemaValidator00A2Fa6146089317 \
    as JSONSchemaValidator00A2Fa6146089317_v1_3_1
from .validators.v1_3_1.jsd_1399891c42a8be64 \
    import JSONSchemaValidator1399891C42A8Be64 \
    as JSONSchemaValidator1399891C42A8Be64_v1_3_1
from .validators.v1_3_1.jsd_45bc7a8344a8bc1e \
    import JSONSchemaValidator45Bc7A8344A8Bc1E \
    as JSONSchemaValidator45Bc7A8344A8Bc1E_v1_3_1
from .validators.v1_3_1.jsd_4d86a993469a9da9 \
    import JSONSchemaValidator4D86A993469A9Da9 \
    as JSONSchemaValidator4D86A993469A9Da9_v1_3_1
from .validators.v1_3_1.jsd_10b06a6a4f7bb3cb \
    import JSONSchemaValidator10B06A6A4F7BB3Cb \
    as JSONSchemaValidator10B06A6A4F7BB3Cb_v1_3_1
from .validators.v1_3_1.jsd_1da5ebdd434aacfe \
    import JSONSchemaValidator1Da5Ebdd434AAcfe \
    as JSONSchemaValidator1Da5Ebdd434AAcfe_v1_3_1
from .validators.v1_3_1.jsd_47a1b84b4e1b8044 \
    import JSONSchemaValidator47A1B84B4E1B8044 \
    as JSONSchemaValidator47A1B84B4E1B8044_v1_3_1
from .validators.v1_3_1.jsd_55b439dc4239b140 \
    import JSONSchemaValidator55B439Dc4239B140 \
    as JSONSchemaValidator55B439Dc4239B140_v1_3_1
from .validators.v1_3_1.jsd_709fda3c42b8877a \
    import JSONSchemaValidator709FDa3C42B8877A \
    as JSONSchemaValidator709FDa3C42B8877A_v1_3_1
from .validators.v1_3_1.jsd_7aa3da9d4e098ef2 \
    import JSONSchemaValidator7Aa3Da9D4E098Ef2 \
    as JSONSchemaValidator7Aa3Da9D4E098Ef2_v1_3_1
from .validators.v1_3_1.jsd_6bacb8d14639bdc7 \
    import JSONSchemaValidator6BacB8D14639Bdc7 \
    as JSONSchemaValidator6BacB8D14639Bdc7_v1_3_1
from .validators.v1_3_1.jsd_89b36b4649999d81 \
    import JSONSchemaValidator89B36B4649999D81 \
    as JSONSchemaValidator89B36B4649999D81_v1_3_1
from .validators.v1_3_1.jsd_9788b8fc4418831d \
    import JSONSchemaValidator9788B8Fc4418831D \
    as JSONSchemaValidator9788B8Fc4418831D_v1_3_1
from .validators.v1_3_1.jsd_a5ac99774c6bb541 \
    import JSONSchemaValidatorA5Ac99774C6BB541 \
    as JSONSchemaValidatorA5Ac99774C6BB541_v1_3_1
from .validators.v1_3_1.jsd_948ea8194348bc0b \
    import JSONSchemaValidator948EA8194348Bc0B \
    as JSONSchemaValidator948EA8194348Bc0B_v1_3_1
from .validators.v1_3_1.jsd_b68a6bd8473a9a25 \
    import JSONSchemaValidatorB68A6Bd8473A9A25 \
    as JSONSchemaValidatorB68A6Bd8473A9A25_v1_3_1
from .validators.v1_3_1.jsd_979688084b7ba60d \
    import JSONSchemaValidator979688084B7BA60D \
    as JSONSchemaValidator979688084B7BA60D_v1_3_1
from .validators.v1_3_1.jsd_fba0d80747eb82e8 \
    import JSONSchemaValidatorFba0D80747Eb82E8 \
    as JSONSchemaValidatorFba0D80747Eb82E8_v1_3_1
from .validators.v1_3_1.jsd_17929bc7465bb564 \
    import JSONSchemaValidator17929Bc7465BB564 \
    as JSONSchemaValidator17929Bc7465BB564_v1_3_1
from .validators.v1_3_1.jsd_4d9ca8e2431a8a24 \
    import JSONSchemaValidator4D9CA8E2431A8A24 \
    as JSONSchemaValidator4D9CA8E2431A8A24_v1_3_1
from .validators.v1_3_1.jsd_bf859ac64a0ba19c \
    import JSONSchemaValidatorBf859Ac64A0BA19C \
    as JSONSchemaValidatorBf859Ac64A0BA19C_v1_3_1
from .validators.v1_3_1.jsd_c5acd9fa4c1a8abc \
    import JSONSchemaValidatorC5AcD9Fa4C1A8Abc \
    as JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v1_3_1
from .validators.v1_3_1.jsd_d6b8ca774739adf4 \
    import JSONSchemaValidatorD6B8Ca774739Adf4 \
    as JSONSchemaValidatorD6B8Ca774739Adf4_v1_3_1
from .validators.v1_3_1.jsd_a395fae644ca899c \
    import JSONSchemaValidatorA395Fae644Ca899C \
    as JSONSchemaValidatorA395Fae644Ca899C_v1_3_1
from .validators.v1_3_1.jsd_00aec9b1422ab27e \
    import JSONSchemaValidator00AeC9B1422AB27E \
    as JSONSchemaValidator00AeC9B1422AB27E_v1_3_1
from .validators.v1_3_1.jsd_62b05b2c40a9b216 \
    import JSONSchemaValidator62B05B2C40A9B216 \
    as JSONSchemaValidator62B05B2C40A9B216_v1_3_1
from .validators.v1_3_1.jsd_6099da82477b858a \
    import JSONSchemaValidator6099Da82477B858A \
    as JSONSchemaValidator6099Da82477B858A_v1_3_1
from .validators.v1_3_1.jsd_7781fa0548a98342 \
    import JSONSchemaValidator7781Fa0548A98342 \
    as JSONSchemaValidator7781Fa0548A98342_v1_3_1
from .validators.v1_3_1.jsd_f6b119ad4d4aaf16 \
    import JSONSchemaValidatorF6B119Ad4D4AAf16 \
    as JSONSchemaValidatorF6B119Ad4D4AAf16_v1_3_1
from .validators.v1_3_1.jsd_f393abe84989bb48 \
    import JSONSchemaValidatorF393Abe84989Bb48 \
    as JSONSchemaValidatorF393Abe84989Bb48_v1_3_1
from .validators.v1_3_1.jsd_9480fa1f47ca9254 \
    import JSONSchemaValidator9480Fa1F47Ca9254 \
    as JSONSchemaValidator9480Fa1F47Ca9254_v1_3_1
from .validators.v1_3_1.jsd_0b836b7b4b6a9fd5 \
    import JSONSchemaValidator0B836B7B4B6A9Fd5 \
    as JSONSchemaValidator0B836B7B4B6A9Fd5_v1_3_1
from .validators.v1_3_1.jsd_09b0f9ce4239ae10 \
    import JSONSchemaValidator09B0F9Ce4239Ae10 \
    as JSONSchemaValidator09B0F9Ce4239Ae10_v1_3_1
from .validators.v1_3_1.jsd_1e962af345b8b59f \
    import JSONSchemaValidator1E962Af345B8B59F \
    as JSONSchemaValidator1E962Af345B8B59F_v1_3_1
from .validators.v1_3_1.jsd_5889fb844939a13b \
    import JSONSchemaValidator5889Fb844939A13B \
    as JSONSchemaValidator5889Fb844939A13B_v1_3_1
from .validators.v1_3_1.jsd_6f9819e84178870c \
    import JSONSchemaValidator6F9819E84178870C \
    as JSONSchemaValidator6F9819E84178870C_v1_3_1
from .validators.v1_3_1.jsd_848b5a7b4f9b8c12 \
    import JSONSchemaValidator848B5A7B4F9B8C12 \
    as JSONSchemaValidator848B5A7B4F9B8C12_v1_3_1
from .validators.v1_3_1.jsd_a4b6c87a4ffb9efa \
    import JSONSchemaValidatorA4B6C87A4Ffb9Efa \
    as JSONSchemaValidatorA4B6C87A4Ffb9Efa_v1_3_1
from .validators.v1_3_1.jsd_9e857b5a4a0bbcdb \
    import JSONSchemaValidator9E857B5A4A0BBcdb \
    as JSONSchemaValidator9E857B5A4A0BBcdb_v1_3_1
from .validators.v1_3_1.jsd_21a6db2540298f55 \
    import JSONSchemaValidator21A6Db2540298F55 \
    as JSONSchemaValidator21A6Db2540298F55_v1_3_1
from .validators.v1_3_1.jsd_3086c9624f498b85 \
    import JSONSchemaValidator3086C9624F498B85 \
    as JSONSchemaValidator3086C9624F498B85_v1_3_1
from .validators.v1_3_1.jsd_8da0391947088a5a \
    import JSONSchemaValidator8Da0391947088A5A \
    as JSONSchemaValidator8Da0391947088A5A_v1_3_1
from .validators.v1_3_1.jsd_f3b26b5544cabab9 \
    import JSONSchemaValidatorF3B26B5544CaBab9 \
    as JSONSchemaValidatorF3B26B5544CaBab9_v1_3_1
from .validators.v1_3_1.jsd_cf9418234d9ab37e \
    import JSONSchemaValidatorCf9418234D9AB37E \
    as JSONSchemaValidatorCf9418234D9AB37E_v1_3_1
from .validators.v1_3_1.jsd_d8a619974a8a8c48 \
    import JSONSchemaValidatorD8A619974A8A8C48 \
    as JSONSchemaValidatorD8A619974A8A8C48_v1_3_1
from .validators.v1_3_1.jsd_8cb6783b4faba1f4 \
    import JSONSchemaValidator8Cb6783B4FabA1F4 \
    as JSONSchemaValidator8Cb6783B4FabA1F4_v1_3_1
from .validators.v1_3_1.jsd_bc8aab4746ca883d \
    import JSONSchemaValidatorBc8AAb4746Ca883D \
    as JSONSchemaValidatorBc8AAb4746Ca883D_v1_3_1
from .validators.v1_3_1.jsd_fb9beb664f2aba4c \
    import JSONSchemaValidatorFb9BEb664F2ABa4C \
    as JSONSchemaValidatorFb9BEb664F2ABa4C_v1_3_1
from .validators.v1_3_1.jsd_6f9cda9a465884b4 \
    import JSONSchemaValidator6F9CDa9A465884B4 \
    as JSONSchemaValidator6F9CDa9A465884B4_v1_3_1
from .validators.v1_3_1.jsd_2f97e8fa45f8b2a3 \
    import JSONSchemaValidator2F97E8Fa45F8B2A3 \
    as JSONSchemaValidator2F97E8Fa45F8B2A3_v1_3_1
from .validators.v1_3_1.jsd_4bb22af046fa8f08 \
    import JSONSchemaValidator4Bb22Af046Fa8F08 \
    as JSONSchemaValidator4Bb22Af046Fa8F08_v1_3_1
from .validators.v1_3_1.jsd_aeb9eb67460b92df \
    import JSONSchemaValidatorAeb9Eb67460B92Df \
    as JSONSchemaValidatorAeb9Eb67460B92Df_v1_3_1
from .validators.v1_3_1.jsd_3b9ef9674429be4c \
    import JSONSchemaValidator3B9EF9674429Be4C \
    as JSONSchemaValidator3B9EF9674429Be4C_v1_3_1
from .validators.v1_3_1.jsd_b9855ad54ae98156 \
    import JSONSchemaValidatorB9855Ad54Ae98156 \
    as JSONSchemaValidatorB9855Ad54Ae98156_v1_3_1
from .validators.v1_3_1.jsd_cd98780f4888a66d \
    import JSONSchemaValidatorCd98780F4888A66D \
    as JSONSchemaValidatorCd98780F4888A66D_v1_3_1
from .validators.v1_3_1.jsd_eeb7eb4b4bd8a1dd \
    import JSONSchemaValidatorEeb7Eb4B4Bd8A1Dd \
    as JSONSchemaValidatorEeb7Eb4B4Bd8A1Dd_v1_3_1
from .validators.v1_3_1.jsd_eeb168eb41988e07 \
    import JSONSchemaValidatorEeb168Eb41988E07 \
    as JSONSchemaValidatorEeb168Eb41988E07_v1_3_1
from .validators.v1_3_1.jsd_50b589fd4c7a930a \
    import JSONSchemaValidator50B589Fd4C7A930A \
    as JSONSchemaValidator50B589Fd4C7A930A_v1_3_1
from .validators.v1_3_1.jsd_4f9f7a7b40f990de \
    import JSONSchemaValidator4F9F7A7B40F990De \
    as JSONSchemaValidator4F9F7A7B40F990De_v1_3_1
from .validators.v1_3_1.jsd_579a6a7248cb94cf \
    import JSONSchemaValidator579A6A7248Cb94Cf \
    as JSONSchemaValidator579A6A7248Cb94Cf_v1_3_1
from .validators.v1_3_1.jsd_1eb72ad34e098990 \
    import JSONSchemaValidator1Eb72Ad34E098990 \
    as JSONSchemaValidator1Eb72Ad34E098990_v1_3_1
from .validators.v1_3_1.jsd_cfbd3870405aad55 \
    import JSONSchemaValidatorCfbd3870405AAd55 \
    as JSONSchemaValidatorCfbd3870405AAd55_v1_3_1
from .validators.v1_3_1.jsd_709769624bf988d5 \
    import JSONSchemaValidator709769624Bf988D5 \
    as JSONSchemaValidator709769624Bf988D5_v1_3_1
from .validators.v1_3_1.jsd_8a96fb954d09a349 \
    import JSONSchemaValidator8A96Fb954D09A349 \
    as JSONSchemaValidator8A96Fb954D09A349_v1_3_1
from .validators.v1_3_1.jsd_87a5ab044139862d \
    import JSONSchemaValidator87A5Ab044139862D \
    as JSONSchemaValidator87A5Ab044139862D_v1_3_1
from .validators.v1_3_1.jsd_b78329674878b815 \
    import JSONSchemaValidatorB78329674878B815 \
    as JSONSchemaValidatorB78329674878B815_v1_3_1
from .validators.v1_3_1.jsd_d09b08a3447aa3b9 \
    import JSONSchemaValidatorD09B08A3447AA3B9 \
    as JSONSchemaValidatorD09B08A3447AA3B9_v1_3_1
from .validators.v1_3_1.jsd_e9b99b2248c88014 \
    import JSONSchemaValidatorE9B99B2248C88014 \
    as JSONSchemaValidatorE9B99B2248C88014_v1_3_1
from .validators.v1_3_1.jsd_8984ea7744d98a54 \
    import JSONSchemaValidator8984Ea7744D98A54 \
    as JSONSchemaValidator8984Ea7744D98A54_v1_3_1
from .validators.v1_3_1.jsd_9582ab824ce8b29d \
    import JSONSchemaValidator9582Ab824Ce8B29D \
    as JSONSchemaValidator9582Ab824Ce8B29D_v1_3_1
from .validators.v1_3_1.jsd_87a8ba444ce9bc59 \
    import JSONSchemaValidator87A8Ba444Ce9Bc59 \
    as JSONSchemaValidator87A8Ba444Ce9Bc59_v1_3_1
from .validators.v1_3_1.jsd_bca339d844c8a3c0 \
    import JSONSchemaValidatorBca339D844C8A3C0 \
    as JSONSchemaValidatorBca339D844C8A3C0_v1_3_1
from .validators.v1_3_1.jsd_208579ea4ed98f4f \
    import JSONSchemaValidator208579Ea4Ed98F4F \
    as JSONSchemaValidator208579Ea4Ed98F4F_v1_3_1
from .validators.v1_3_1.jsd_bead7b3443b996a7 \
    import JSONSchemaValidatorBead7B3443B996A7 \
    as JSONSchemaValidatorBead7B3443B996A7_v1_3_1
from .validators.v1_3_1.jsd_3e94cb1b485b8b0e \
    import JSONSchemaValidator3E94Cb1B485B8B0E \
    as JSONSchemaValidator3E94Cb1B485B8B0E_v1_3_1
from .validators.v1_3_1.jsd_fb9bf80f491a9851 \
    import JSONSchemaValidatorFb9BF80F491A9851 \
    as JSONSchemaValidatorFb9BF80F491A9851_v1_3_1
from .validators.v1_3_1.jsd_398668874439a41d \
    import JSONSchemaValidator398668874439A41D \
    as JSONSchemaValidator398668874439A41D_v1_3_1
from .validators.v1_3_3.jsd_00a2fa6146089317 \
    import JSONSchemaValidator00A2Fa6146089317 \
    as JSONSchemaValidator00A2Fa6146089317_v1_3_3
from .validators.v1_3_3.jsd_1399891c42a8be64 \
    import JSONSchemaValidator1399891C42A8Be64 \
    as JSONSchemaValidator1399891C42A8Be64_v1_3_3
from .validators.v1_3_3.jsd_45bc7a8344a8bc1e \
    import JSONSchemaValidator45Bc7A8344A8Bc1E \
    as JSONSchemaValidator45Bc7A8344A8Bc1E_v1_3_3
from .validators.v1_3_3.jsd_4d86a993469a9da9 \
    import JSONSchemaValidator4D86A993469A9Da9 \
    as JSONSchemaValidator4D86A993469A9Da9_v1_3_3
from .validators.v1_3_3.jsd_17929bc7465bb564 \
    import JSONSchemaValidator17929Bc7465BB564 \
    as JSONSchemaValidator17929Bc7465BB564_v1_3_3
from .validators.v1_3_3.jsd_10b06a6a4f7bb3cb \
    import JSONSchemaValidator10B06A6A4F7BB3Cb \
    as JSONSchemaValidator10B06A6A4F7BB3Cb_v1_3_3
from .validators.v1_3_3.jsd_1da5ebdd434aacfe \
    import JSONSchemaValidator1Da5Ebdd434AAcfe \
    as JSONSchemaValidator1Da5Ebdd434AAcfe_v1_3_3
from .validators.v1_3_3.jsd_47a1b84b4e1b8044 \
    import JSONSchemaValidator47A1B84B4E1B8044 \
    as JSONSchemaValidator47A1B84B4E1B8044_v1_3_3
from .validators.v1_3_3.jsd_4d9ca8e2431a8a24 \
    import JSONSchemaValidator4D9CA8E2431A8A24 \
    as JSONSchemaValidator4D9CA8E2431A8A24_v1_3_3
from .validators.v1_3_3.jsd_55b439dc4239b140 \
    import JSONSchemaValidator55B439Dc4239B140 \
    as JSONSchemaValidator55B439Dc4239B140_v1_3_3
from .validators.v1_3_3.jsd_709fda3c42b8877a \
    import JSONSchemaValidator709FDa3C42B8877A \
    as JSONSchemaValidator709FDa3C42B8877A_v1_3_3
from .validators.v1_3_3.jsd_6bacb8d14639bdc7 \
    import JSONSchemaValidator6BacB8D14639Bdc7 \
    as JSONSchemaValidator6BacB8D14639Bdc7_v1_3_3
from .validators.v1_3_3.jsd_7aa3da9d4e098ef2 \
    import JSONSchemaValidator7Aa3Da9D4E098Ef2 \
    as JSONSchemaValidator7Aa3Da9D4E098Ef2_v1_3_3
from .validators.v1_3_3.jsd_89b36b4649999d81 \
    import JSONSchemaValidator89B36B4649999D81 \
    as JSONSchemaValidator89B36B4649999D81_v1_3_3
from .validators.v1_3_3.jsd_9788b8fc4418831d \
    import JSONSchemaValidator9788B8Fc4418831D \
    as JSONSchemaValidator9788B8Fc4418831D_v1_3_3
from .validators.v1_3_3.jsd_948ea8194348bc0b \
    import JSONSchemaValidator948EA8194348Bc0B \
    as JSONSchemaValidator948EA8194348Bc0B_v1_3_3
from .validators.v1_3_3.jsd_a5ac99774c6bb541 \
    import JSONSchemaValidatorA5Ac99774C6BB541 \
    as JSONSchemaValidatorA5Ac99774C6BB541_v1_3_3
from .validators.v1_3_3.jsd_979688084b7ba60d \
    import JSONSchemaValidator979688084B7BA60D \
    as JSONSchemaValidator979688084B7BA60D_v1_3_3
from .validators.v1_3_3.jsd_b68a6bd8473a9a25 \
    import JSONSchemaValidatorB68A6Bd8473A9A25 \
    as JSONSchemaValidatorB68A6Bd8473A9A25_v1_3_3
from .validators.v1_3_3.jsd_bf859ac64a0ba19c \
    import JSONSchemaValidatorBf859Ac64A0BA19C \
    as JSONSchemaValidatorBf859Ac64A0BA19C_v1_3_3
from .validators.v1_3_3.jsd_c5acd9fa4c1a8abc \
    import JSONSchemaValidatorC5AcD9Fa4C1A8Abc \
    as JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v1_3_3
from .validators.v1_3_3.jsd_fba0d80747eb82e8 \
    import JSONSchemaValidatorFba0D80747Eb82E8 \
    as JSONSchemaValidatorFba0D80747Eb82E8_v1_3_3
from .validators.v1_3_3.jsd_d6b8ca774739adf4 \
    import JSONSchemaValidatorD6B8Ca774739Adf4 \
    as JSONSchemaValidatorD6B8Ca774739Adf4_v1_3_3
from .validators.v1_3_3.jsd_a395fae644ca899c \
    import JSONSchemaValidatorA395Fae644Ca899C \
    as JSONSchemaValidatorA395Fae644Ca899C_v1_3_3
from .validators.v1_3_3.jsd_00aec9b1422ab27e \
    import JSONSchemaValidator00AeC9B1422AB27E \
    as JSONSchemaValidator00AeC9B1422AB27E_v1_3_3
from .validators.v1_3_3.jsd_62b05b2c40a9b216 \
    import JSONSchemaValidator62B05B2C40A9B216 \
    as JSONSchemaValidator62B05B2C40A9B216_v1_3_3
from .validators.v1_3_3.jsd_6099da82477b858a \
    import JSONSchemaValidator6099Da82477B858A \
    as JSONSchemaValidator6099Da82477B858A_v1_3_3
from .validators.v1_3_3.jsd_7781fa0548a98342 \
    import JSONSchemaValidator7781Fa0548A98342 \
    as JSONSchemaValidator7781Fa0548A98342_v1_3_3
from .validators.v1_3_3.jsd_9480fa1f47ca9254 \
    import JSONSchemaValidator9480Fa1F47Ca9254 \
    as JSONSchemaValidator9480Fa1F47Ca9254_v1_3_3
from .validators.v1_3_3.jsd_f393abe84989bb48 \
    import JSONSchemaValidatorF393Abe84989Bb48 \
    as JSONSchemaValidatorF393Abe84989Bb48_v1_3_3
from .validators.v1_3_3.jsd_f6b119ad4d4aaf16 \
    import JSONSchemaValidatorF6B119Ad4D4AAf16 \
    as JSONSchemaValidatorF6B119Ad4D4AAf16_v1_3_3
from .validators.v1_3_3.jsd_0b836b7b4b6a9fd5 \
    import JSONSchemaValidator0B836B7B4B6A9Fd5 \
    as JSONSchemaValidator0B836B7B4B6A9Fd5_v1_3_3
from .validators.v1_3_3.jsd_09b0f9ce4239ae10 \
    import JSONSchemaValidator09B0F9Ce4239Ae10 \
    as JSONSchemaValidator09B0F9Ce4239Ae10_v1_3_3
from .validators.v1_3_3.jsd_21a6db2540298f55 \
    import JSONSchemaValidator21A6Db2540298F55 \
    as JSONSchemaValidator21A6Db2540298F55_v1_3_3
from .validators.v1_3_3.jsd_1e962af345b8b59f \
    import JSONSchemaValidator1E962Af345B8B59F \
    as JSONSchemaValidator1E962Af345B8B59F_v1_3_3
from .validators.v1_3_3.jsd_3086c9624f498b85 \
    import JSONSchemaValidator3086C9624F498B85 \
    as JSONSchemaValidator3086C9624F498B85_v1_3_3
from .validators.v1_3_3.jsd_5889fb844939a13b \
    import JSONSchemaValidator5889Fb844939A13B \
    as JSONSchemaValidator5889Fb844939A13B_v1_3_3
from .validators.v1_3_3.jsd_6f9819e84178870c \
    import JSONSchemaValidator6F9819E84178870C \
    as JSONSchemaValidator6F9819E84178870C_v1_3_3
from .validators.v1_3_3.jsd_848b5a7b4f9b8c12 \
    import JSONSchemaValidator848B5A7B4F9B8C12 \
    as JSONSchemaValidator848B5A7B4F9B8C12_v1_3_3
from .validators.v1_3_3.jsd_8da0391947088a5a \
    import JSONSchemaValidator8Da0391947088A5A \
    as JSONSchemaValidator8Da0391947088A5A_v1_3_3
from .validators.v1_3_3.jsd_9e857b5a4a0bbcdb \
    import JSONSchemaValidator9E857B5A4A0BBcdb \
    as JSONSchemaValidator9E857B5A4A0BBcdb_v1_3_3
from .validators.v1_3_3.jsd_a4b6c87a4ffb9efa \
    import JSONSchemaValidatorA4B6C87A4Ffb9Efa \
    as JSONSchemaValidatorA4B6C87A4Ffb9Efa_v1_3_3
from .validators.v1_3_3.jsd_cf9418234d9ab37e \
    import JSONSchemaValidatorCf9418234D9AB37E \
    as JSONSchemaValidatorCf9418234D9AB37E_v1_3_3
from .validators.v1_3_3.jsd_d8a619974a8a8c48 \
    import JSONSchemaValidatorD8A619974A8A8C48 \
    as JSONSchemaValidatorD8A619974A8A8C48_v1_3_3
from .validators.v1_3_3.jsd_f3b26b5544cabab9 \
    import JSONSchemaValidatorF3B26B5544CaBab9 \
    as JSONSchemaValidatorF3B26B5544CaBab9_v1_3_3
from .validators.v1_3_3.jsd_8cb6783b4faba1f4 \
    import JSONSchemaValidator8Cb6783B4FabA1F4 \
    as JSONSchemaValidator8Cb6783B4FabA1F4_v1_3_3
from .validators.v1_3_3.jsd_bc8aab4746ca883d \
    import JSONSchemaValidatorBc8AAb4746Ca883D \
    as JSONSchemaValidatorBc8AAb4746Ca883D_v1_3_3
from .validators.v1_3_3.jsd_fb9beb664f2aba4c \
    import JSONSchemaValidatorFb9BEb664F2ABa4C \
    as JSONSchemaValidatorFb9BEb664F2ABa4C_v1_3_3
from .validators.v1_3_3.jsd_03b4c8b44919b964 \
    import JSONSchemaValidator03B4C8B44919B964 \
    as JSONSchemaValidator03B4C8B44919B964_v1_3_3
from .validators.v1_3_3.jsd_4da91a544e29842d \
    import JSONSchemaValidator4Da91A544E29842D \
    as JSONSchemaValidator4Da91A544E29842D_v1_3_3
from .validators.v1_3_3.jsd_5087daae4cc98566 \
    import JSONSchemaValidator5087Daae4Cc98566 \
    as JSONSchemaValidator5087Daae4Cc98566_v1_3_3
from .validators.v1_3_3.jsd_4f947a1c4fc884f6 \
    import JSONSchemaValidator4F947A1C4Fc884F6 \
    as JSONSchemaValidator4F947A1C4Fc884F6_v1_3_3
from .validators.v1_3_3.jsd_698bfbb44dcb9fca \
    import JSONSchemaValidator698BFbb44Dcb9Fca \
    as JSONSchemaValidator698BFbb44Dcb9Fca_v1_3_3
from .validators.v1_3_3.jsd_a39a1a214debb781 \
    import JSONSchemaValidatorA39A1A214DebB781 \
    as JSONSchemaValidatorA39A1A214DebB781_v1_3_3
from .validators.v1_3_3.jsd_be892bd84a78865a \
    import JSONSchemaValidatorBe892Bd84A78865A \
    as JSONSchemaValidatorBe892Bd84A78865A_v1_3_3
from .validators.v1_3_3.jsd_fbb95b37484a9fce \
    import JSONSchemaValidatorFbb95B37484A9Fce \
    as JSONSchemaValidatorFbb95B37484A9Fce_v1_3_3
from .validators.v1_3_3.jsd_f793192a43dabed9 \
    import JSONSchemaValidatorF793192A43DaBed9 \
    as JSONSchemaValidatorF793192A43DaBed9_v1_3_3
from .validators.v1_3_3.jsd_2f97e8fa45f8b2a3 \
    import JSONSchemaValidator2F97E8Fa45F8B2A3 \
    as JSONSchemaValidator2F97E8Fa45F8B2A3_v1_3_3
from .validators.v1_3_3.jsd_6f9cda9a465884b4 \
    import JSONSchemaValidator6F9CDa9A465884B4 \
    as JSONSchemaValidator6F9CDa9A465884B4_v1_3_3
from .validators.v1_3_3.jsd_3b9ef9674429be4c \
    import JSONSchemaValidator3B9EF9674429Be4C \
    as JSONSchemaValidator3B9EF9674429Be4C_v1_3_3
from .validators.v1_3_3.jsd_4bb22af046fa8f08 \
    import JSONSchemaValidator4Bb22Af046Fa8F08 \
    as JSONSchemaValidator4Bb22Af046Fa8F08_v1_3_3
from .validators.v1_3_3.jsd_b9855ad54ae98156 \
    import JSONSchemaValidatorB9855Ad54Ae98156 \
    as JSONSchemaValidatorB9855Ad54Ae98156_v1_3_3
from .validators.v1_3_3.jsd_cd98780f4888a66d \
    import JSONSchemaValidatorCd98780F4888A66D \
    as JSONSchemaValidatorCd98780F4888A66D_v1_3_3
from .validators.v1_3_3.jsd_aeb9eb67460b92df \
    import JSONSchemaValidatorAeb9Eb67460B92Df \
    as JSONSchemaValidatorAeb9Eb67460B92Df_v1_3_3
from .validators.v1_3_3.jsd_eeb168eb41988e07 \
    import JSONSchemaValidatorEeb168Eb41988E07 \
    as JSONSchemaValidatorEeb168Eb41988E07_v1_3_3
from .validators.v1_3_3.jsd_50b589fd4c7a930a \
    import JSONSchemaValidator50B589Fd4C7A930A \
    as JSONSchemaValidator50B589Fd4C7A930A_v1_3_3
from .validators.v1_3_3.jsd_eeb7eb4b4bd8a1dd \
    import JSONSchemaValidatorEeb7Eb4B4Bd8A1Dd \
    as JSONSchemaValidatorEeb7Eb4B4Bd8A1Dd_v1_3_3
from .validators.v1_3_3.jsd_4f9f7a7b40f990de \
    import JSONSchemaValidator4F9F7A7B40F990De \
    as JSONSchemaValidator4F9F7A7B40F990De_v1_3_3
from .validators.v1_3_3.jsd_579a6a7248cb94cf \
    import JSONSchemaValidator579A6A7248Cb94Cf \
    as JSONSchemaValidator579A6A7248Cb94Cf_v1_3_3
from .validators.v1_3_3.jsd_1eb72ad34e098990 \
    import JSONSchemaValidator1Eb72Ad34E098990 \
    as JSONSchemaValidator1Eb72Ad34E098990_v1_3_3
from .validators.v1_3_3.jsd_709769624bf988d5 \
    import JSONSchemaValidator709769624Bf988D5 \
    as JSONSchemaValidator709769624Bf988D5_v1_3_3
from .validators.v1_3_3.jsd_87a5ab044139862d \
    import JSONSchemaValidator87A5Ab044139862D \
    as JSONSchemaValidator87A5Ab044139862D_v1_3_3
from .validators.v1_3_3.jsd_8a96fb954d09a349 \
    import JSONSchemaValidator8A96Fb954D09A349 \
    as JSONSchemaValidator8A96Fb954D09A349_v1_3_3
from .validators.v1_3_3.jsd_b78329674878b815 \
    import JSONSchemaValidatorB78329674878B815 \
    as JSONSchemaValidatorB78329674878B815_v1_3_3
from .validators.v1_3_3.jsd_d09b08a3447aa3b9 \
    import JSONSchemaValidatorD09B08A3447AA3B9 \
    as JSONSchemaValidatorD09B08A3447AA3B9_v1_3_3
from .validators.v1_3_3.jsd_cfbd3870405aad55 \
    import JSONSchemaValidatorCfbd3870405AAd55 \
    as JSONSchemaValidatorCfbd3870405AAd55_v1_3_3
from .validators.v1_3_3.jsd_e9b99b2248c88014 \
    import JSONSchemaValidatorE9B99B2248C88014 \
    as JSONSchemaValidatorE9B99B2248C88014_v1_3_3
from .validators.v1_3_3.jsd_208579ea4ed98f4f \
    import JSONSchemaValidator208579Ea4Ed98F4F \
    as JSONSchemaValidator208579Ea4Ed98F4F_v1_3_3
from .validators.v1_3_3.jsd_518c59cd441aa9fc \
    import JSONSchemaValidator518C59Cd441AA9Fc \
    as JSONSchemaValidator518C59Cd441AA9Fc_v1_3_3
from .validators.v1_3_3.jsd_6db9292d4f28a26b \
    import JSONSchemaValidator6Db9292D4F28A26B \
    as JSONSchemaValidator6Db9292D4F28A26B_v1_3_3
from .validators.v1_3_3.jsd_87a8ba444ce9bc59 \
    import JSONSchemaValidator87A8Ba444Ce9Bc59 \
    as JSONSchemaValidator87A8Ba444Ce9Bc59_v1_3_3
from .validators.v1_3_3.jsd_9582ab824ce8b29d \
    import JSONSchemaValidator9582Ab824Ce8B29D \
    as JSONSchemaValidator9582Ab824Ce8B29D_v1_3_3
from .validators.v1_3_3.jsd_8984ea7744d98a54 \
    import JSONSchemaValidator8984Ea7744D98A54 \
    as JSONSchemaValidator8984Ea7744D98A54_v1_3_3
from .validators.v1_3_3.jsd_bead7b3443b996a7 \
    import JSONSchemaValidatorBead7B3443B996A7 \
    as JSONSchemaValidatorBead7B3443B996A7_v1_3_3
from .validators.v1_3_3.jsd_c2a43ad24098baa7 \
    import JSONSchemaValidatorC2A43Ad24098Baa7 \
    as JSONSchemaValidatorC2A43Ad24098Baa7_v1_3_3
from .validators.v1_3_3.jsd_bca339d844c8a3c0 \
    import JSONSchemaValidatorBca339D844C8A3C0 \
    as JSONSchemaValidatorBca339D844C8A3C0_v1_3_3
from .validators.v1_3_3.jsd_dd85c91042489a3f \
    import JSONSchemaValidatorDd85C91042489A3F \
    as JSONSchemaValidatorDd85C91042489A3F_v1_3_3
from .validators.v1_3_3.jsd_d2b4d9d04a4b884c \
    import JSONSchemaValidatorD2B4D9D04A4B884C \
    as JSONSchemaValidatorD2B4D9D04A4B884C_v1_3_3
from .validators.v1_3_3.jsd_398668874439a41d \
    import JSONSchemaValidator398668874439A41D \
    as JSONSchemaValidator398668874439A41D_v1_3_3
from .validators.v1_3_3.jsd_3e94cb1b485b8b0e \
    import JSONSchemaValidator3E94Cb1B485B8B0E \
    as JSONSchemaValidator3E94Cb1B485B8B0E_v1_3_3
from .validators.v1_3_3.jsd_fb9bf80f491a9851 \
    import JSONSchemaValidatorFb9BF80F491A9851 \
    as JSONSchemaValidatorFb9BF80F491A9851_v1_3_3
from .validators.v2_1_1.jsd_17929bc7465bb564 \
    import JSONSchemaValidator17929Bc7465BB564 \
    as JSONSchemaValidator17929Bc7465BB564_v2_1_1
from .validators.v2_1_1.jsd_10b06a6a4f7bb3cb \
    import JSONSchemaValidator10B06A6A4F7BB3Cb \
    as JSONSchemaValidator10B06A6A4F7BB3Cb_v2_1_1
from .validators.v2_1_1.jsd_1da5ebdd434aacfe \
    import JSONSchemaValidator1Da5Ebdd434AAcfe \
    as JSONSchemaValidator1Da5Ebdd434AAcfe_v2_1_1
from .validators.v2_1_1.jsd_47a1b84b4e1b8044 \
    import JSONSchemaValidator47A1B84B4E1B8044 \
    as JSONSchemaValidator47A1B84B4E1B8044_v2_1_1
from .validators.v2_1_1.jsd_4d9ca8e2431a8a24 \
    import JSONSchemaValidator4D9CA8E2431A8A24 \
    as JSONSchemaValidator4D9CA8E2431A8A24_v2_1_1
from .validators.v2_1_1.jsd_55b439dc4239b140 \
    import JSONSchemaValidator55B439Dc4239B140 \
    as JSONSchemaValidator55B439Dc4239B140_v2_1_1
from .validators.v2_1_1.jsd_6bacb8d14639bdc7 \
    import JSONSchemaValidator6BacB8D14639Bdc7 \
    as JSONSchemaValidator6BacB8D14639Bdc7_v2_1_1
from .validators.v2_1_1.jsd_709fda3c42b8877a \
    import JSONSchemaValidator709FDa3C42B8877A \
    as JSONSchemaValidator709FDa3C42B8877A_v2_1_1
from .validators.v2_1_1.jsd_7aa3da9d4e098ef2 \
    import JSONSchemaValidator7Aa3Da9D4E098Ef2 \
    as JSONSchemaValidator7Aa3Da9D4E098Ef2_v2_1_1
from .validators.v2_1_1.jsd_979688084b7ba60d \
    import JSONSchemaValidator979688084B7BA60D \
    as JSONSchemaValidator979688084B7BA60D_v2_1_1
from .validators.v2_1_1.jsd_89b36b4649999d81 \
    import JSONSchemaValidator89B36B4649999D81 \
    as JSONSchemaValidator89B36B4649999D81_v2_1_1
from .validators.v2_1_1.jsd_948ea8194348bc0b \
    import JSONSchemaValidator948EA8194348Bc0B \
    as JSONSchemaValidator948EA8194348Bc0B_v2_1_1
from .validators.v2_1_1.jsd_a5ac99774c6bb541 \
    import JSONSchemaValidatorA5Ac99774C6BB541 \
    as JSONSchemaValidatorA5Ac99774C6BB541_v2_1_1
from .validators.v2_1_1.jsd_9788b8fc4418831d \
    import JSONSchemaValidator9788B8Fc4418831D \
    as JSONSchemaValidator9788B8Fc4418831D_v2_1_1
from .validators.v2_1_1.jsd_bf859ac64a0ba19c \
    import JSONSchemaValidatorBf859Ac64A0BA19C \
    as JSONSchemaValidatorBf859Ac64A0BA19C_v2_1_1
from .validators.v2_1_1.jsd_b68a6bd8473a9a25 \
    import JSONSchemaValidatorB68A6Bd8473A9A25 \
    as JSONSchemaValidatorB68A6Bd8473A9A25_v2_1_1
from .validators.v2_1_1.jsd_c5acd9fa4c1a8abc \
    import JSONSchemaValidatorC5AcD9Fa4C1A8Abc \
    as JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v2_1_1
from .validators.v2_1_1.jsd_fba0d80747eb82e8 \
    import JSONSchemaValidatorFba0D80747Eb82E8 \
    as JSONSchemaValidatorFba0D80747Eb82E8_v2_1_1
from .validators.v2_1_1.jsd_00a2fa6146089317 \
    import JSONSchemaValidator00A2Fa6146089317 \
    as JSONSchemaValidator00A2Fa6146089317_v2_1_1
from .validators.v2_1_1.jsd_1399891c42a8be64 \
    import JSONSchemaValidator1399891C42A8Be64 \
    as JSONSchemaValidator1399891C42A8Be64_v2_1_1
from .validators.v2_1_1.jsd_45bc7a8344a8bc1e \
    import JSONSchemaValidator45Bc7A8344A8Bc1E \
    as JSONSchemaValidator45Bc7A8344A8Bc1E_v2_1_1
from .validators.v2_1_1.jsd_4d86a993469a9da9 \
    import JSONSchemaValidator4D86A993469A9Da9 \
    as JSONSchemaValidator4D86A993469A9Da9_v2_1_1
from .validators.v2_1_1.jsd_d6b8ca774739adf4 \
    import JSONSchemaValidatorD6B8Ca774739Adf4 \
    as JSONSchemaValidatorD6B8Ca774739Adf4_v2_1_1
from .validators.v2_1_1.jsd_a395fae644ca899c \
    import JSONSchemaValidatorA395Fae644Ca899C \
    as JSONSchemaValidatorA395Fae644Ca899C_v2_1_1
from .validators.v2_1_1.jsd_00aec9b1422ab27e \
    import JSONSchemaValidator00AeC9B1422AB27E \
    as JSONSchemaValidator00AeC9B1422AB27E_v2_1_1
from .validators.v2_1_1.jsd_6099da82477b858a \
    import JSONSchemaValidator6099Da82477B858A \
    as JSONSchemaValidator6099Da82477B858A_v2_1_1
from .validators.v2_1_1.jsd_62b05b2c40a9b216 \
    import JSONSchemaValidator62B05B2C40A9B216 \
    as JSONSchemaValidator62B05B2C40A9B216_v2_1_1
from .validators.v2_1_1.jsd_7781fa0548a98342 \
    import JSONSchemaValidator7781Fa0548A98342 \
    as JSONSchemaValidator7781Fa0548A98342_v2_1_1
from .validators.v2_1_1.jsd_9480fa1f47ca9254 \
    import JSONSchemaValidator9480Fa1F47Ca9254 \
    as JSONSchemaValidator9480Fa1F47Ca9254_v2_1_1
from .validators.v2_1_1.jsd_f393abe84989bb48 \
    import JSONSchemaValidatorF393Abe84989Bb48 \
    as JSONSchemaValidatorF393Abe84989Bb48_v2_1_1
from .validators.v2_1_1.jsd_f6b119ad4d4aaf16 \
    import JSONSchemaValidatorF6B119Ad4D4AAf16 \
    as JSONSchemaValidatorF6B119Ad4D4AAf16_v2_1_1
from .validators.v2_1_1.jsd_0b836b7b4b6a9fd5 \
    import JSONSchemaValidator0B836B7B4B6A9Fd5 \
    as JSONSchemaValidator0B836B7B4B6A9Fd5_v2_1_1
from .validators.v2_1_1.jsd_09b0f9ce4239ae10 \
    import JSONSchemaValidator09B0F9Ce4239Ae10 \
    as JSONSchemaValidator09B0F9Ce4239Ae10_v2_1_1
from .validators.v2_1_1.jsd_1e962af345b8b59f \
    import JSONSchemaValidator1E962Af345B8B59F \
    as JSONSchemaValidator1E962Af345B8B59F_v2_1_1
from .validators.v2_1_1.jsd_21a6db2540298f55 \
    import JSONSchemaValidator21A6Db2540298F55 \
    as JSONSchemaValidator21A6Db2540298F55_v2_1_1
from .validators.v2_1_1.jsd_3086c9624f498b85 \
    import JSONSchemaValidator3086C9624F498B85 \
    as JSONSchemaValidator3086C9624F498B85_v2_1_1
from .validators.v2_1_1.jsd_5889fb844939a13b \
    import JSONSchemaValidator5889Fb844939A13B \
    as JSONSchemaValidator5889Fb844939A13B_v2_1_1
from .validators.v2_1_1.jsd_6f9819e84178870c \
    import JSONSchemaValidator6F9819E84178870C \
    as JSONSchemaValidator6F9819E84178870C_v2_1_1
from .validators.v2_1_1.jsd_8da0391947088a5a \
    import JSONSchemaValidator8Da0391947088A5A \
    as JSONSchemaValidator8Da0391947088A5A_v2_1_1
from .validators.v2_1_1.jsd_848b5a7b4f9b8c12 \
    import JSONSchemaValidator848B5A7B4F9B8C12 \
    as JSONSchemaValidator848B5A7B4F9B8C12_v2_1_1
from .validators.v2_1_1.jsd_9e857b5a4a0bbcdb \
    import JSONSchemaValidator9E857B5A4A0BBcdb \
    as JSONSchemaValidator9E857B5A4A0BBcdb_v2_1_1
from .validators.v2_1_1.jsd_a4b6c87a4ffb9efa \
    import JSONSchemaValidatorA4B6C87A4Ffb9Efa \
    as JSONSchemaValidatorA4B6C87A4Ffb9Efa_v2_1_1
from .validators.v2_1_1.jsd_cf9418234d9ab37e \
    import JSONSchemaValidatorCf9418234D9AB37E \
    as JSONSchemaValidatorCf9418234D9AB37E_v2_1_1
from .validators.v2_1_1.jsd_d8a619974a8a8c48 \
    import JSONSchemaValidatorD8A619974A8A8C48 \
    as JSONSchemaValidatorD8A619974A8A8C48_v2_1_1
from .validators.v2_1_1.jsd_f3b26b5544cabab9 \
    import JSONSchemaValidatorF3B26B5544CaBab9 \
    as JSONSchemaValidatorF3B26B5544CaBab9_v2_1_1
from .validators.v2_1_1.jsd_8cb6783b4faba1f4 \
    import JSONSchemaValidator8Cb6783B4FabA1F4 \
    as JSONSchemaValidator8Cb6783B4FabA1F4_v2_1_1
from .validators.v2_1_1.jsd_bc8aab4746ca883d \
    import JSONSchemaValidatorBc8AAb4746Ca883D \
    as JSONSchemaValidatorBc8AAb4746Ca883D_v2_1_1
from .validators.v2_1_1.jsd_fb9beb664f2aba4c \
    import JSONSchemaValidatorFb9BEb664F2ABa4C \
    as JSONSchemaValidatorFb9BEb664F2ABa4C_v2_1_1
from .validators.v2_1_1.jsd_3faaa9944b49bc9f \
    import JSONSchemaValidator3FaaA9944B49Bc9F \
    as JSONSchemaValidator3FaaA9944B49Bc9F_v2_1_1
from .validators.v2_1_1.jsd_4ababa75489ab24b \
    import JSONSchemaValidator4AbaBa75489AB24B \
    as JSONSchemaValidator4AbaBa75489AB24B_v2_1_1
from .validators.v2_1_1.jsd_64b9dad0403aaca1 \
    import JSONSchemaValidator64B9Dad0403AAca1 \
    as JSONSchemaValidator64B9Dad0403AAca1_v2_1_1
from .validators.v2_1_1.jsd_03b4c8b44919b964 \
    import JSONSchemaValidator03B4C8B44919B964 \
    as JSONSchemaValidator03B4C8B44919B964_v2_1_1
from .validators.v2_1_1.jsd_5087daae4cc98566 \
    import JSONSchemaValidator5087Daae4Cc98566 \
    as JSONSchemaValidator5087Daae4Cc98566_v2_1_1
from .validators.v2_1_1.jsd_4da91a544e29842d \
    import JSONSchemaValidator4Da91A544E29842D \
    as JSONSchemaValidator4Da91A544E29842D_v2_1_1
from .validators.v2_1_1.jsd_698bfbb44dcb9fca \
    import JSONSchemaValidator698BFbb44Dcb9Fca \
    as JSONSchemaValidator698BFbb44Dcb9Fca_v2_1_1
from .validators.v2_1_1.jsd_4f947a1c4fc884f6 \
    import JSONSchemaValidator4F947A1C4Fc884F6 \
    as JSONSchemaValidator4F947A1C4Fc884F6_v2_1_1
from .validators.v2_1_1.jsd_a39a1a214debb781 \
    import JSONSchemaValidatorA39A1A214DebB781 \
    as JSONSchemaValidatorA39A1A214DebB781_v2_1_1
from .validators.v2_1_1.jsd_be892bd84a78865a \
    import JSONSchemaValidatorBe892Bd84A78865A \
    as JSONSchemaValidatorBe892Bd84A78865A_v2_1_1
from .validators.v2_1_1.jsd_fbb95b37484a9fce \
    import JSONSchemaValidatorFbb95B37484A9Fce \
    as JSONSchemaValidatorFbb95B37484A9Fce_v2_1_1
from .validators.v2_1_1.jsd_f793192a43dabed9 \
    import JSONSchemaValidatorF793192A43DaBed9 \
    as JSONSchemaValidatorF793192A43DaBed9_v2_1_1
from .validators.v2_1_1.jsd_0fa00adf48698287 \
    import JSONSchemaValidator0Fa00Adf48698287 \
    as JSONSchemaValidator0Fa00Adf48698287_v2_1_1
from .validators.v2_1_1.jsd_2f97e8fa45f8b2a3 \
    import JSONSchemaValidator2F97E8Fa45F8B2A3 \
    as JSONSchemaValidator2F97E8Fa45F8B2A3_v2_1_1
from .validators.v2_1_1.jsd_66951aaa407ba89c \
    import JSONSchemaValidator66951Aaa407BA89C \
    as JSONSchemaValidator66951Aaa407BA89C_v2_1_1
from .validators.v2_1_1.jsd_6f9cda9a465884b4 \
    import JSONSchemaValidator6F9CDa9A465884B4 \
    as JSONSchemaValidator6F9CDa9A465884B4_v2_1_1
from .validators.v2_1_1.jsd_3b9ef9674429be4c \
    import JSONSchemaValidator3B9EF9674429Be4C \
    as JSONSchemaValidator3B9EF9674429Be4C_v2_1_1
from .validators.v2_1_1.jsd_4bb22af046fa8f08 \
    import JSONSchemaValidator4Bb22Af046Fa8F08 \
    as JSONSchemaValidator4Bb22Af046Fa8F08_v2_1_1
from .validators.v2_1_1.jsd_aeb9eb67460b92df \
    import JSONSchemaValidatorAeb9Eb67460B92Df \
    as JSONSchemaValidatorAeb9Eb67460B92Df_v2_1_1
from .validators.v2_1_1.jsd_b9855ad54ae98156 \
    import JSONSchemaValidatorB9855Ad54Ae98156 \
    as JSONSchemaValidatorB9855Ad54Ae98156_v2_1_1
from .validators.v2_1_1.jsd_cd98780f4888a66d \
    import JSONSchemaValidatorCd98780F4888A66D \
    as JSONSchemaValidatorCd98780F4888A66D_v2_1_1
from .validators.v2_1_1.jsd_eeb168eb41988e07 \
    import JSONSchemaValidatorEeb168Eb41988E07 \
    as JSONSchemaValidatorEeb168Eb41988E07_v2_1_1
from .validators.v2_1_1.jsd_50b589fd4c7a930a \
    import JSONSchemaValidator50B589Fd4C7A930A \
    as JSONSchemaValidator50B589Fd4C7A930A_v2_1_1
from .validators.v2_1_1.jsd_eeb7eb4b4bd8a1dd \
    import JSONSchemaValidatorEeb7Eb4B4Bd8A1Dd \
    as JSONSchemaValidatorEeb7Eb4B4Bd8A1Dd_v2_1_1
from .validators.v2_1_1.jsd_579a6a7248cb94cf \
    import JSONSchemaValidator579A6A7248Cb94Cf \
    as JSONSchemaValidator579A6A7248Cb94Cf_v2_1_1
from .validators.v2_1_1.jsd_4f9f7a7b40f990de \
    import JSONSchemaValidator4F9F7A7B40F990De \
    as JSONSchemaValidator4F9F7A7B40F990De_v2_1_1
from .validators.v2_1_1.jsd_208579ea4ed98f4f \
    import JSONSchemaValidator208579Ea4Ed98F4F \
    as JSONSchemaValidator208579Ea4Ed98F4F_v2_1_1
from .validators.v2_1_1.jsd_518c59cd441aa9fc \
    import JSONSchemaValidator518C59Cd441AA9Fc \
    as JSONSchemaValidator518C59Cd441AA9Fc_v2_1_1
from .validators.v2_1_1.jsd_8984ea7744d98a54 \
    import JSONSchemaValidator8984Ea7744D98A54 \
    as JSONSchemaValidator8984Ea7744D98A54_v2_1_1
from .validators.v2_1_1.jsd_6db9292d4f28a26b \
    import JSONSchemaValidator6Db9292D4F28A26B \
    as JSONSchemaValidator6Db9292D4F28A26B_v2_1_1
from .validators.v2_1_1.jsd_87a8ba444ce9bc59 \
    import JSONSchemaValidator87A8Ba444Ce9Bc59 \
    as JSONSchemaValidator87A8Ba444Ce9Bc59_v2_1_1
from .validators.v2_1_1.jsd_9582ab824ce8b29d \
    import JSONSchemaValidator9582Ab824Ce8B29D \
    as JSONSchemaValidator9582Ab824Ce8B29D_v2_1_1
from .validators.v2_1_1.jsd_bca339d844c8a3c0 \
    import JSONSchemaValidatorBca339D844C8A3C0 \
    as JSONSchemaValidatorBca339D844C8A3C0_v2_1_1
from .validators.v2_1_1.jsd_d2b4d9d04a4b884c \
    import JSONSchemaValidatorD2B4D9D04A4B884C \
    as JSONSchemaValidatorD2B4D9D04A4B884C_v2_1_1
from .validators.v2_1_1.jsd_bead7b3443b996a7 \
    import JSONSchemaValidatorBead7B3443B996A7 \
    as JSONSchemaValidatorBead7B3443B996A7_v2_1_1
from .validators.v2_1_1.jsd_c2a43ad24098baa7 \
    import JSONSchemaValidatorC2A43Ad24098Baa7 \
    as JSONSchemaValidatorC2A43Ad24098Baa7_v2_1_1
from .validators.v2_1_1.jsd_dd85c91042489a3f \
    import JSONSchemaValidatorDd85C91042489A3F \
    as JSONSchemaValidatorDd85C91042489A3F_v2_1_1
from .validators.v2_1_1.jsd_1eb72ad34e098990 \
    import JSONSchemaValidator1Eb72Ad34E098990 \
    as JSONSchemaValidator1Eb72Ad34E098990_v2_1_1
from .validators.v2_1_1.jsd_709769624bf988d5 \
    import JSONSchemaValidator709769624Bf988D5 \
    as JSONSchemaValidator709769624Bf988D5_v2_1_1
from .validators.v2_1_1.jsd_87a5ab044139862d \
    import JSONSchemaValidator87A5Ab044139862D \
    as JSONSchemaValidator87A5Ab044139862D_v2_1_1
from .validators.v2_1_1.jsd_8a96fb954d09a349 \
    import JSONSchemaValidator8A96Fb954D09A349 \
    as JSONSchemaValidator8A96Fb954D09A349_v2_1_1
from .validators.v2_1_1.jsd_b78329674878b815 \
    import JSONSchemaValidatorB78329674878B815 \
    as JSONSchemaValidatorB78329674878B815_v2_1_1
from .validators.v2_1_1.jsd_d09b08a3447aa3b9 \
    import JSONSchemaValidatorD09B08A3447AA3B9 \
    as JSONSchemaValidatorD09B08A3447AA3B9_v2_1_1
from .validators.v2_1_1.jsd_e9b99b2248c88014 \
    import JSONSchemaValidatorE9B99B2248C88014 \
    as JSONSchemaValidatorE9B99B2248C88014_v2_1_1
from .validators.v2_1_1.jsd_d89719b847aaa9c4 \
    import JSONSchemaValidatorD89719B847AaA9C4 \
    as JSONSchemaValidatorD89719B847AaA9C4_v2_1_1
from .validators.v2_1_1.jsd_cfbd3870405aad55 \
    import JSONSchemaValidatorCfbd3870405AAd55 \
    as JSONSchemaValidatorCfbd3870405AAd55_v2_1_1
from .validators.v2_1_1.jsd_3e94cb1b485b8b0e \
    import JSONSchemaValidator3E94Cb1B485B8B0E \
    as JSONSchemaValidator3E94Cb1B485B8B0E_v2_1_1
from .validators.v2_1_1.jsd_398668874439a41d \
    import JSONSchemaValidator398668874439A41D \
    as JSONSchemaValidator398668874439A41D_v2_1_1
from .validators.v2_1_1.jsd_fb9bf80f491a9851 \
    import JSONSchemaValidatorFb9BF80F491A9851 \
    as JSONSchemaValidatorFb9BF80F491A9851_v2_1_1
from .validators.v2_1_1.jsd_fa9a98174129af50 \
    import JSONSchemaValidatorFa9A98174129Af50 \
    as JSONSchemaValidatorFa9A98174129Af50_v2_1_1
from .validators.v2_1_2.jsd_eb8c2a8345aa871f \
    import JSONSchemaValidatorEb8C2A8345Aa871F \
    as JSONSchemaValidatorEb8C2A8345Aa871F_v2_1_2
from .validators.v2_1_2.jsd_3b9898f04cfbb74b \
    import JSONSchemaValidator3B9898F04CfbB74B \
    as JSONSchemaValidator3B9898F04CfbB74B_v2_1_2
from .validators.v2_1_2.jsd_f6bfc880435aae2a \
    import JSONSchemaValidatorF6BfC880435AAe2A \
    as JSONSchemaValidatorF6BfC880435AAe2A_v2_1_2
from .validators.v2_1_2.jsd_3b9ef9674429be4c \
    import JSONSchemaValidator3B9EF9674429Be4C \
    as JSONSchemaValidator3B9EF9674429Be4C_v2_1_2
from .validators.v2_1_2.jsd_4bb22af046fa8f08 \
    import JSONSchemaValidator4Bb22Af046Fa8F08 \
    as JSONSchemaValidator4Bb22Af046Fa8F08_v2_1_2
from .validators.v2_1_2.jsd_aeb9eb67460b92df \
    import JSONSchemaValidatorAeb9Eb67460B92Df \
    as JSONSchemaValidatorAeb9Eb67460B92Df_v2_1_2
from .validators.v2_1_2.jsd_b9855ad54ae98156 \
    import JSONSchemaValidatorB9855Ad54Ae98156 \
    as JSONSchemaValidatorB9855Ad54Ae98156_v2_1_2
from .validators.v2_1_2.jsd_cd98780f4888a66d \
    import JSONSchemaValidatorCd98780F4888A66D \
    as JSONSchemaValidatorCd98780F4888A66D_v2_1_2
from .validators.v2_1_2.jsd_eeb168eb41988e07 \
    import JSONSchemaValidatorEeb168Eb41988E07 \
    as JSONSchemaValidatorEeb168Eb41988E07_v2_1_2
from .validators.v2_1_2.jsd_50b589fd4c7a930a \
    import JSONSchemaValidator50B589Fd4C7A930A \
    as JSONSchemaValidator50B589Fd4C7A930A_v2_1_2
from .validators.v2_1_2.jsd_eeb7eb4b4bd8a1dd \
    import JSONSchemaValidatorEeb7Eb4B4Bd8A1Dd \
    as JSONSchemaValidatorEeb7Eb4B4Bd8A1Dd_v2_1_2
from .validators.v2_1_2.jsd_08bd88834a68a2e6 \
    import JSONSchemaValidator08Bd88834A68A2E6 \
    as JSONSchemaValidator08Bd88834A68A2E6_v2_1_2
from .validators.v2_1_2.jsd_85a2883749099021 \
    import JSONSchemaValidator85A2883749099021 \
    as JSONSchemaValidator85A2883749099021_v2_1_2
from .validators.v2_1_2.jsd_c085eaf54f89ba34 \
    import JSONSchemaValidatorC085Eaf54F89Ba34 \
    as JSONSchemaValidatorC085Eaf54F89Ba34_v2_1_2
from .validators.v2_1_2.jsd_f1a7a8e74cf99c8f \
    import JSONSchemaValidatorF1A7A8E74Cf99C8F \
    as JSONSchemaValidatorF1A7A8E74Cf99C8F_v2_1_2
from .validators.v2_1_2.jsd_00a2fa6146089317 \
    import JSONSchemaValidator00A2Fa6146089317 \
    as JSONSchemaValidator00A2Fa6146089317_v2_1_2
from .validators.v2_1_2.jsd_1399891c42a8be64 \
    import JSONSchemaValidator1399891C42A8Be64 \
    as JSONSchemaValidator1399891C42A8Be64_v2_1_2
from .validators.v2_1_2.jsd_45bc7a8344a8bc1e \
    import JSONSchemaValidator45Bc7A8344A8Bc1E \
    as JSONSchemaValidator45Bc7A8344A8Bc1E_v2_1_2
from .validators.v2_1_2.jsd_4d86a993469a9da9 \
    import JSONSchemaValidator4D86A993469A9Da9 \
    as JSONSchemaValidator4D86A993469A9Da9_v2_1_2
from .validators.v2_1_2.jsd_10b06a6a4f7bb3cb \
    import JSONSchemaValidator10B06A6A4F7BB3Cb \
    as JSONSchemaValidator10B06A6A4F7BB3Cb_v2_1_2
from .validators.v2_1_2.jsd_1da5ebdd434aacfe \
    import JSONSchemaValidator1Da5Ebdd434AAcfe \
    as JSONSchemaValidator1Da5Ebdd434AAcfe_v2_1_2
from .validators.v2_1_2.jsd_17929bc7465bb564 \
    import JSONSchemaValidator17929Bc7465BB564 \
    as JSONSchemaValidator17929Bc7465BB564_v2_1_2
from .validators.v2_1_2.jsd_47a1b84b4e1b8044 \
    import JSONSchemaValidator47A1B84B4E1B8044 \
    as JSONSchemaValidator47A1B84B4E1B8044_v2_1_2
from .validators.v2_1_2.jsd_4d9ca8e2431a8a24 \
    import JSONSchemaValidator4D9CA8E2431A8A24 \
    as JSONSchemaValidator4D9CA8E2431A8A24_v2_1_2
from .validators.v2_1_2.jsd_55b439dc4239b140 \
    import JSONSchemaValidator55B439Dc4239B140 \
    as JSONSchemaValidator55B439Dc4239B140_v2_1_2
from .validators.v2_1_2.jsd_6bacb8d14639bdc7 \
    import JSONSchemaValidator6BacB8D14639Bdc7 \
    as JSONSchemaValidator6BacB8D14639Bdc7_v2_1_2
from .validators.v2_1_2.jsd_709fda3c42b8877a \
    import JSONSchemaValidator709FDa3C42B8877A \
    as JSONSchemaValidator709FDa3C42B8877A_v2_1_2
from .validators.v2_1_2.jsd_7aa3da9d4e098ef2 \
    import JSONSchemaValidator7Aa3Da9D4E098Ef2 \
    as JSONSchemaValidator7Aa3Da9D4E098Ef2_v2_1_2
from .validators.v2_1_2.jsd_89b36b4649999d81 \
    import JSONSchemaValidator89B36B4649999D81 \
    as JSONSchemaValidator89B36B4649999D81_v2_1_2
from .validators.v2_1_2.jsd_948ea8194348bc0b \
    import JSONSchemaValidator948EA8194348Bc0B \
    as JSONSchemaValidator948EA8194348Bc0B_v2_1_2
from .validators.v2_1_2.jsd_979688084b7ba60d \
    import JSONSchemaValidator979688084B7BA60D \
    as JSONSchemaValidator979688084B7BA60D_v2_1_2
from .validators.v2_1_2.jsd_9788b8fc4418831d \
    import JSONSchemaValidator9788B8Fc4418831D \
    as JSONSchemaValidator9788B8Fc4418831D_v2_1_2
from .validators.v2_1_2.jsd_a5ac99774c6bb541 \
    import JSONSchemaValidatorA5Ac99774C6BB541 \
    as JSONSchemaValidatorA5Ac99774C6BB541_v2_1_2
from .validators.v2_1_2.jsd_bf859ac64a0ba19c \
    import JSONSchemaValidatorBf859Ac64A0BA19C \
    as JSONSchemaValidatorBf859Ac64A0BA19C_v2_1_2
from .validators.v2_1_2.jsd_c5acd9fa4c1a8abc \
    import JSONSchemaValidatorC5AcD9Fa4C1A8Abc \
    as JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v2_1_2
from .validators.v2_1_2.jsd_b68a6bd8473a9a25 \
    import JSONSchemaValidatorB68A6Bd8473A9A25 \
    as JSONSchemaValidatorB68A6Bd8473A9A25_v2_1_2
from .validators.v2_1_2.jsd_fba0d80747eb82e8 \
    import JSONSchemaValidatorFba0D80747Eb82E8 \
    as JSONSchemaValidatorFba0D80747Eb82E8_v2_1_2
from .validators.v2_1_2.jsd_d6b8ca774739adf4 \
    import JSONSchemaValidatorD6B8Ca774739Adf4 \
    as JSONSchemaValidatorD6B8Ca774739Adf4_v2_1_2
from .validators.v2_1_2.jsd_a395fae644ca899c \
    import JSONSchemaValidatorA395Fae644Ca899C \
    as JSONSchemaValidatorA395Fae644Ca899C_v2_1_2
from .validators.v2_1_2.jsd_00aec9b1422ab27e \
    import JSONSchemaValidator00AeC9B1422AB27E \
    as JSONSchemaValidator00AeC9B1422AB27E_v2_1_2
from .validators.v2_1_2.jsd_6099da82477b858a \
    import JSONSchemaValidator6099Da82477B858A \
    as JSONSchemaValidator6099Da82477B858A_v2_1_2
from .validators.v2_1_2.jsd_62b05b2c40a9b216 \
    import JSONSchemaValidator62B05B2C40A9B216 \
    as JSONSchemaValidator62B05B2C40A9B216_v2_1_2
from .validators.v2_1_2.jsd_7781fa0548a98342 \
    import JSONSchemaValidator7781Fa0548A98342 \
    as JSONSchemaValidator7781Fa0548A98342_v2_1_2
from .validators.v2_1_2.jsd_9480fa1f47ca9254 \
    import JSONSchemaValidator9480Fa1F47Ca9254 \
    as JSONSchemaValidator9480Fa1F47Ca9254_v2_1_2
from .validators.v2_1_2.jsd_f393abe84989bb48 \
    import JSONSchemaValidatorF393Abe84989Bb48 \
    as JSONSchemaValidatorF393Abe84989Bb48_v2_1_2
from .validators.v2_1_2.jsd_f6b119ad4d4aaf16 \
    import JSONSchemaValidatorF6B119Ad4D4AAf16 \
    as JSONSchemaValidatorF6B119Ad4D4AAf16_v2_1_2
from .validators.v2_1_2.jsd_0b836b7b4b6a9fd5 \
    import JSONSchemaValidator0B836B7B4B6A9Fd5 \
    as JSONSchemaValidator0B836B7B4B6A9Fd5_v2_1_2
from .validators.v2_1_2.jsd_1e962af345b8b59f \
    import JSONSchemaValidator1E962Af345B8B59F \
    as JSONSchemaValidator1E962Af345B8B59F_v2_1_2
from .validators.v2_1_2.jsd_09b0f9ce4239ae10 \
    import JSONSchemaValidator09B0F9Ce4239Ae10 \
    as JSONSchemaValidator09B0F9Ce4239Ae10_v2_1_2
from .validators.v2_1_2.jsd_21a6db2540298f55 \
    import JSONSchemaValidator21A6Db2540298F55 \
    as JSONSchemaValidator21A6Db2540298F55_v2_1_2
from .validators.v2_1_2.jsd_3086c9624f498b85 \
    import JSONSchemaValidator3086C9624F498B85 \
    as JSONSchemaValidator3086C9624F498B85_v2_1_2
from .validators.v2_1_2.jsd_5889fb844939a13b \
    import JSONSchemaValidator5889Fb844939A13B \
    as JSONSchemaValidator5889Fb844939A13B_v2_1_2
from .validators.v2_1_2.jsd_6f9819e84178870c \
    import JSONSchemaValidator6F9819E84178870C \
    as JSONSchemaValidator6F9819E84178870C_v2_1_2
from .validators.v2_1_2.jsd_848b5a7b4f9b8c12 \
    import JSONSchemaValidator848B5A7B4F9B8C12 \
    as JSONSchemaValidator848B5A7B4F9B8C12_v2_1_2
from .validators.v2_1_2.jsd_8da0391947088a5a \
    import JSONSchemaValidator8Da0391947088A5A \
    as JSONSchemaValidator8Da0391947088A5A_v2_1_2
from .validators.v2_1_2.jsd_9e857b5a4a0bbcdb \
    import JSONSchemaValidator9E857B5A4A0BBcdb \
    as JSONSchemaValidator9E857B5A4A0BBcdb_v2_1_2
from .validators.v2_1_2.jsd_a4b6c87a4ffb9efa \
    import JSONSchemaValidatorA4B6C87A4Ffb9Efa \
    as JSONSchemaValidatorA4B6C87A4Ffb9Efa_v2_1_2
from .validators.v2_1_2.jsd_cf9418234d9ab37e \
    import JSONSchemaValidatorCf9418234D9AB37E \
    as JSONSchemaValidatorCf9418234D9AB37E_v2_1_2
from .validators.v2_1_2.jsd_f3b26b5544cabab9 \
    import JSONSchemaValidatorF3B26B5544CaBab9 \
    as JSONSchemaValidatorF3B26B5544CaBab9_v2_1_2
from .validators.v2_1_2.jsd_d8a619974a8a8c48 \
    import JSONSchemaValidatorD8A619974A8A8C48 \
    as JSONSchemaValidatorD8A619974A8A8C48_v2_1_2
from .validators.v2_1_2.jsd_8cb6783b4faba1f4 \
    import JSONSchemaValidator8Cb6783B4FabA1F4 \
    as JSONSchemaValidator8Cb6783B4FabA1F4_v2_1_2
from .validators.v2_1_2.jsd_bc8aab4746ca883d \
    import JSONSchemaValidatorBc8AAb4746Ca883D \
    as JSONSchemaValidatorBc8AAb4746Ca883D_v2_1_2
from .validators.v2_1_2.jsd_fb9beb664f2aba4c \
    import JSONSchemaValidatorFb9BEb664F2ABa4C \
    as JSONSchemaValidatorFb9BEb664F2ABa4C_v2_1_2
from .validators.v2_1_2.jsd_4ababa75489ab24b \
    import JSONSchemaValidator4AbaBa75489AB24B \
    as JSONSchemaValidator4AbaBa75489AB24B_v2_1_2
from .validators.v2_1_2.jsd_3faaa9944b49bc9f \
    import JSONSchemaValidator3FaaA9944B49Bc9F \
    as JSONSchemaValidator3FaaA9944B49Bc9F_v2_1_2
from .validators.v2_1_2.jsd_64b9dad0403aaca1 \
    import JSONSchemaValidator64B9Dad0403AAca1 \
    as JSONSchemaValidator64B9Dad0403AAca1_v2_1_2
from .validators.v2_1_2.jsd_03b4c8b44919b964 \
    import JSONSchemaValidator03B4C8B44919B964 \
    as JSONSchemaValidator03B4C8B44919B964_v2_1_2
from .validators.v2_1_2.jsd_5087daae4cc98566 \
    import JSONSchemaValidator5087Daae4Cc98566 \
    as JSONSchemaValidator5087Daae4Cc98566_v2_1_2
from .validators.v2_1_2.jsd_4f947a1c4fc884f6 \
    import JSONSchemaValidator4F947A1C4Fc884F6 \
    as JSONSchemaValidator4F947A1C4Fc884F6_v2_1_2
from .validators.v2_1_2.jsd_4da91a544e29842d \
    import JSONSchemaValidator4Da91A544E29842D \
    as JSONSchemaValidator4Da91A544E29842D_v2_1_2
from .validators.v2_1_2.jsd_698bfbb44dcb9fca \
    import JSONSchemaValidator698BFbb44Dcb9Fca \
    as JSONSchemaValidator698BFbb44Dcb9Fca_v2_1_2
from .validators.v2_1_2.jsd_a39a1a214debb781 \
    import JSONSchemaValidatorA39A1A214DebB781 \
    as JSONSchemaValidatorA39A1A214DebB781_v2_1_2
from .validators.v2_1_2.jsd_be892bd84a78865a \
    import JSONSchemaValidatorBe892Bd84A78865A \
    as JSONSchemaValidatorBe892Bd84A78865A_v2_1_2
from .validators.v2_1_2.jsd_fbb95b37484a9fce \
    import JSONSchemaValidatorFbb95B37484A9Fce \
    as JSONSchemaValidatorFbb95B37484A9Fce_v2_1_2
from .validators.v2_1_2.jsd_f793192a43dabed9 \
    import JSONSchemaValidatorF793192A43DaBed9 \
    as JSONSchemaValidatorF793192A43DaBed9_v2_1_2
from .validators.v2_1_2.jsd_0fa00adf48698287 \
    import JSONSchemaValidator0Fa00Adf48698287 \
    as JSONSchemaValidator0Fa00Adf48698287_v2_1_2
from .validators.v2_1_2.jsd_66951aaa407ba89c \
    import JSONSchemaValidator66951Aaa407BA89C \
    as JSONSchemaValidator66951Aaa407BA89C_v2_1_2
from .validators.v2_1_2.jsd_2f97e8fa45f8b2a3 \
    import JSONSchemaValidator2F97E8Fa45F8B2A3 \
    as JSONSchemaValidator2F97E8Fa45F8B2A3_v2_1_2
from .validators.v2_1_2.jsd_6f9cda9a465884b4 \
    import JSONSchemaValidator6F9CDa9A465884B4 \
    as JSONSchemaValidator6F9CDa9A465884B4_v2_1_2
from .validators.v2_1_2.jsd_579a6a7248cb94cf \
    import JSONSchemaValidator579A6A7248Cb94Cf \
    as JSONSchemaValidator579A6A7248Cb94Cf_v2_1_2
from .validators.v2_1_2.jsd_4f9f7a7b40f990de \
    import JSONSchemaValidator4F9F7A7B40F990De \
    as JSONSchemaValidator4F9F7A7B40F990De_v2_1_2
from .validators.v2_1_2.jsd_208579ea4ed98f4f \
    import JSONSchemaValidator208579Ea4Ed98F4F \
    as JSONSchemaValidator208579Ea4Ed98F4F_v2_1_2
from .validators.v2_1_2.jsd_6db9292d4f28a26b \
    import JSONSchemaValidator6Db9292D4F28A26B \
    as JSONSchemaValidator6Db9292D4F28A26B_v2_1_2
from .validators.v2_1_2.jsd_87a8ba444ce9bc59 \
    import JSONSchemaValidator87A8Ba444Ce9Bc59 \
    as JSONSchemaValidator87A8Ba444Ce9Bc59_v2_1_2
from .validators.v2_1_2.jsd_518c59cd441aa9fc \
    import JSONSchemaValidator518C59Cd441AA9Fc \
    as JSONSchemaValidator518C59Cd441AA9Fc_v2_1_2
from .validators.v2_1_2.jsd_9582ab824ce8b29d \
    import JSONSchemaValidator9582Ab824Ce8B29D \
    as JSONSchemaValidator9582Ab824Ce8B29D_v2_1_2
from .validators.v2_1_2.jsd_bca339d844c8a3c0 \
    import JSONSchemaValidatorBca339D844C8A3C0 \
    as JSONSchemaValidatorBca339D844C8A3C0_v2_1_2
from .validators.v2_1_2.jsd_8984ea7744d98a54 \
    import JSONSchemaValidator8984Ea7744D98A54 \
    as JSONSchemaValidator8984Ea7744D98A54_v2_1_2
from .validators.v2_1_2.jsd_dd85c91042489a3f \
    import JSONSchemaValidatorDd85C91042489A3F \
    as JSONSchemaValidatorDd85C91042489A3F_v2_1_2
from .validators.v2_1_2.jsd_bead7b3443b996a7 \
    import JSONSchemaValidatorBead7B3443B996A7 \
    as JSONSchemaValidatorBead7B3443B996A7_v2_1_2
from .validators.v2_1_2.jsd_c2a43ad24098baa7 \
    import JSONSchemaValidatorC2A43Ad24098Baa7 \
    as JSONSchemaValidatorC2A43Ad24098Baa7_v2_1_2
from .validators.v2_1_2.jsd_d2b4d9d04a4b884c \
    import JSONSchemaValidatorD2B4D9D04A4B884C \
    as JSONSchemaValidatorD2B4D9D04A4B884C_v2_1_2
from .validators.v2_1_2.jsd_1eb72ad34e098990 \
    import JSONSchemaValidator1Eb72Ad34E098990 \
    as JSONSchemaValidator1Eb72Ad34E098990_v2_1_2
from .validators.v2_1_2.jsd_709769624bf988d5 \
    import JSONSchemaValidator709769624Bf988D5 \
    as JSONSchemaValidator709769624Bf988D5_v2_1_2
from .validators.v2_1_2.jsd_8a96fb954d09a349 \
    import JSONSchemaValidator8A96Fb954D09A349 \
    as JSONSchemaValidator8A96Fb954D09A349_v2_1_2
from .validators.v2_1_2.jsd_b78329674878b815 \
    import JSONSchemaValidatorB78329674878B815 \
    as JSONSchemaValidatorB78329674878B815_v2_1_2
from .validators.v2_1_2.jsd_87a5ab044139862d \
    import JSONSchemaValidator87A5Ab044139862D \
    as JSONSchemaValidator87A5Ab044139862D_v2_1_2
from .validators.v2_1_2.jsd_d09b08a3447aa3b9 \
    import JSONSchemaValidatorD09B08A3447AA3B9 \
    as JSONSchemaValidatorD09B08A3447AA3B9_v2_1_2
from .validators.v2_1_2.jsd_e9b99b2248c88014 \
    import JSONSchemaValidatorE9B99B2248C88014 \
    as JSONSchemaValidatorE9B99B2248C88014_v2_1_2
from .validators.v2_1_2.jsd_cfbd3870405aad55 \
    import JSONSchemaValidatorCfbd3870405AAd55 \
    as JSONSchemaValidatorCfbd3870405AAd55_v2_1_2
from .validators.v2_1_2.jsd_398668874439a41d \
    import JSONSchemaValidator398668874439A41D \
    as JSONSchemaValidator398668874439A41D_v2_1_2
from .validators.v2_1_2.jsd_3e94cb1b485b8b0e \
    import JSONSchemaValidator3E94Cb1B485B8B0E \
    as JSONSchemaValidator3E94Cb1B485B8B0E_v2_1_2
from .validators.v2_1_2.jsd_fb9bf80f491a9851 \
    import JSONSchemaValidatorFb9BF80F491A9851 \
    as JSONSchemaValidatorFb9BF80F491A9851_v2_1_2
from .validators.v2_1_2.jsd_fa9a98174129af50 \
    import JSONSchemaValidatorFa9A98174129Af50 \
    as JSONSchemaValidatorFa9A98174129Af50_v2_1_2


class JSONSchemaValidator(object):
    """Validates a DNA Center JSON request."""

    def __init__(self):
        super(JSONSchemaValidator, self).__init__()
        self._validator = fastjsonschema.compile({})

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(
                request, e.message
            ))


class SchemaValidator:
    def __init__(self, version):
        self.json_schema_validators = {}
        self.load_validators(version)

    def load_validators(self, version):
        if version == '1.2.10':
            self.json_schema_validators['jsd_00aec9b1422ab27e_v1_2_10'] =\
                JSONSchemaValidator00AeC9B1422AB27E_v1_2_10()
            self.json_schema_validators['jsd_7781fa0548a98342_v1_2_10'] =\
                JSONSchemaValidator7781Fa0548A98342_v1_2_10()
            self.json_schema_validators['jsd_6099da82477b858a_v1_2_10'] =\
                JSONSchemaValidator6099Da82477B858A_v1_2_10()
            self.json_schema_validators['jsd_9480fa1f47ca9254_v1_2_10'] =\
                JSONSchemaValidator9480Fa1F47Ca9254_v1_2_10()
            self.json_schema_validators['jsd_62b05b2c40a9b216_v1_2_10'] =\
                JSONSchemaValidator62B05B2C40A9B216_v1_2_10()
            self.json_schema_validators['jsd_f393abe84989bb48_v1_2_10'] =\
                JSONSchemaValidatorF393Abe84989Bb48_v1_2_10()
            self.json_schema_validators['jsd_f6b119ad4d4aaf16_v1_2_10'] =\
                JSONSchemaValidatorF6B119Ad4D4AAf16_v1_2_10()
            self.json_schema_validators['jsd_00a2fa6146089317_v1_2_10'] =\
                JSONSchemaValidator00A2Fa6146089317_v1_2_10()
            self.json_schema_validators['jsd_1399891c42a8be64_v1_2_10'] =\
                JSONSchemaValidator1399891C42A8Be64_v1_2_10()
            self.json_schema_validators['jsd_45bc7a8344a8bc1e_v1_2_10'] =\
                JSONSchemaValidator45Bc7A8344A8Bc1E_v1_2_10()
            self.json_schema_validators['jsd_4d86a993469a9da9_v1_2_10'] =\
                JSONSchemaValidator4D86A993469A9Da9_v1_2_10()
            self.json_schema_validators['jsd_17929bc7465bb564_v1_2_10'] =\
                JSONSchemaValidator17929Bc7465BB564_v1_2_10()
            self.json_schema_validators['jsd_10b06a6a4f7bb3cb_v1_2_10'] =\
                JSONSchemaValidator10B06A6A4F7BB3Cb_v1_2_10()
            self.json_schema_validators['jsd_1da5ebdd434aacfe_v1_2_10'] =\
                JSONSchemaValidator1Da5Ebdd434AAcfe_v1_2_10()
            self.json_schema_validators['jsd_55b439dc4239b140_v1_2_10'] =\
                JSONSchemaValidator55B439Dc4239B140_v1_2_10()
            self.json_schema_validators['jsd_6bacb8d14639bdc7_v1_2_10'] =\
                JSONSchemaValidator6BacB8D14639Bdc7_v1_2_10()
            self.json_schema_validators['jsd_4d9ca8e2431a8a24_v1_2_10'] =\
                JSONSchemaValidator4D9CA8E2431A8A24_v1_2_10()
            self.json_schema_validators['jsd_709fda3c42b8877a_v1_2_10'] =\
                JSONSchemaValidator709FDa3C42B8877A_v1_2_10()
            self.json_schema_validators['jsd_7aa3da9d4e098ef2_v1_2_10'] =\
                JSONSchemaValidator7Aa3Da9D4E098Ef2_v1_2_10()
            self.json_schema_validators['jsd_9788b8fc4418831d_v1_2_10'] =\
                JSONSchemaValidator9788B8Fc4418831D_v1_2_10()
            self.json_schema_validators['jsd_948ea8194348bc0b_v1_2_10'] =\
                JSONSchemaValidator948EA8194348Bc0B_v1_2_10()
            self.json_schema_validators['jsd_47a1b84b4e1b8044_v1_2_10'] =\
                JSONSchemaValidator47A1B84B4E1B8044_v1_2_10()
            self.json_schema_validators['jsd_a5ac99774c6bb541_v1_2_10'] =\
                JSONSchemaValidatorA5Ac99774C6BB541_v1_2_10()
            self.json_schema_validators['jsd_b68a6bd8473a9a25_v1_2_10'] =\
                JSONSchemaValidatorB68A6Bd8473A9A25_v1_2_10()
            self.json_schema_validators['jsd_bf859ac64a0ba19c_v1_2_10'] =\
                JSONSchemaValidatorBf859Ac64A0BA19C_v1_2_10()
            self.json_schema_validators['jsd_c5acd9fa4c1a8abc_v1_2_10'] =\
                JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v1_2_10()
            self.json_schema_validators['jsd_89b36b4649999d81_v1_2_10'] =\
                JSONSchemaValidator89B36B4649999D81_v1_2_10()
            self.json_schema_validators['jsd_fba0d80747eb82e8_v1_2_10'] =\
                JSONSchemaValidatorFba0D80747Eb82E8_v1_2_10()
            self.json_schema_validators['jsd_979688084b7ba60d_v1_2_10'] =\
                JSONSchemaValidator979688084B7BA60D_v1_2_10()
            self.json_schema_validators['jsd_d6b8ca774739adf4_v1_2_10'] =\
                JSONSchemaValidatorD6B8Ca774739Adf4_v1_2_10()
            self.json_schema_validators['jsd_a395fae644ca899c_v1_2_10'] =\
                JSONSchemaValidatorA395Fae644Ca899C_v1_2_10()
            self.json_schema_validators['jsd_8cb6783b4faba1f4_v1_2_10'] =\
                JSONSchemaValidator8Cb6783B4FabA1F4_v1_2_10()
            self.json_schema_validators['jsd_bc8aab4746ca883d_v1_2_10'] =\
                JSONSchemaValidatorBc8AAb4746Ca883D_v1_2_10()
            self.json_schema_validators['jsd_fb9beb664f2aba4c_v1_2_10'] =\
                JSONSchemaValidatorFb9BEb664F2ABa4C_v1_2_10()
            self.json_schema_validators['jsd_21a6db2540298f55_v1_2_10'] =\
                JSONSchemaValidator21A6Db2540298F55_v1_2_10()
            self.json_schema_validators['jsd_3086c9624f498b85_v1_2_10'] =\
                JSONSchemaValidator3086C9624F498B85_v1_2_10()
            self.json_schema_validators['jsd_0b836b7b4b6a9fd5_v1_2_10'] =\
                JSONSchemaValidator0B836B7B4B6A9Fd5_v1_2_10()
            self.json_schema_validators['jsd_1e962af345b8b59f_v1_2_10'] =\
                JSONSchemaValidator1E962Af345B8B59F_v1_2_10()
            self.json_schema_validators['jsd_09b0f9ce4239ae10_v1_2_10'] =\
                JSONSchemaValidator09B0F9Ce4239Ae10_v1_2_10()
            self.json_schema_validators['jsd_5889fb844939a13b_v1_2_10'] =\
                JSONSchemaValidator5889Fb844939A13B_v1_2_10()
            self.json_schema_validators['jsd_6f9819e84178870c_v1_2_10'] =\
                JSONSchemaValidator6F9819E84178870C_v1_2_10()
            self.json_schema_validators['jsd_8da0391947088a5a_v1_2_10'] =\
                JSONSchemaValidator8Da0391947088A5A_v1_2_10()
            self.json_schema_validators['jsd_9e857b5a4a0bbcdb_v1_2_10'] =\
                JSONSchemaValidator9E857B5A4A0BBcdb_v1_2_10()
            self.json_schema_validators['jsd_a4b6c87a4ffb9efa_v1_2_10'] =\
                JSONSchemaValidatorA4B6C87A4Ffb9Efa_v1_2_10()
            self.json_schema_validators['jsd_cf9418234d9ab37e_v1_2_10'] =\
                JSONSchemaValidatorCf9418234D9AB37E_v1_2_10()
            self.json_schema_validators['jsd_d8a619974a8a8c48_v1_2_10'] =\
                JSONSchemaValidatorD8A619974A8A8C48_v1_2_10()
            self.json_schema_validators['jsd_848b5a7b4f9b8c12_v1_2_10'] =\
                JSONSchemaValidator848B5A7B4F9B8C12_v1_2_10()
            self.json_schema_validators['jsd_f3b26b5544cabab9_v1_2_10'] =\
                JSONSchemaValidatorF3B26B5544CaBab9_v1_2_10()
            self.json_schema_validators['jsd_828828f44f28bd0d_v1_2_10'] =\
                JSONSchemaValidator828828F44F28Bd0D_v1_2_10()
            self.json_schema_validators['jsd_3b9ef9674429be4c_v1_2_10'] =\
                JSONSchemaValidator3B9EF9674429Be4C_v1_2_10()
            self.json_schema_validators['jsd_4bb22af046fa8f08_v1_2_10'] =\
                JSONSchemaValidator4Bb22Af046Fa8F08_v1_2_10()
            self.json_schema_validators['jsd_b9855ad54ae98156_v1_2_10'] =\
                JSONSchemaValidatorB9855Ad54Ae98156_v1_2_10()
            self.json_schema_validators['jsd_aeb9eb67460b92df_v1_2_10'] =\
                JSONSchemaValidatorAeb9Eb67460B92Df_v1_2_10()
            self.json_schema_validators['jsd_cd98780f4888a66d_v1_2_10'] =\
                JSONSchemaValidatorCd98780F4888A66D_v1_2_10()
            self.json_schema_validators['jsd_eeb168eb41988e07_v1_2_10'] =\
                JSONSchemaValidatorEeb168Eb41988E07_v1_2_10()
            self.json_schema_validators['jsd_50b589fd4c7a930a_v1_2_10'] =\
                JSONSchemaValidator50B589Fd4C7A930A_v1_2_10()
            self.json_schema_validators['jsd_8a96fb954d09a349_v1_2_10'] =\
                JSONSchemaValidator8A96Fb954D09A349_v1_2_10()
            self.json_schema_validators['jsd_db9f997f4e59aec1_v1_2_10'] =\
                JSONSchemaValidatorDb9F997F4E59Aec1_v1_2_10()
            self.json_schema_validators['jsd_bead7b3443b996a7_v1_2_10'] =\
                JSONSchemaValidatorBead7B3443B996A7_v1_2_10()
        if version == '1.3.0':
            self.json_schema_validators['jsd_00aec9b1422ab27e_v1_3_0'] =\
                JSONSchemaValidator00AeC9B1422AB27E_v1_3_0()
            self.json_schema_validators['jsd_6099da82477b858a_v1_3_0'] =\
                JSONSchemaValidator6099Da82477B858A_v1_3_0()
            self.json_schema_validators['jsd_7781fa0548a98342_v1_3_0'] =\
                JSONSchemaValidator7781Fa0548A98342_v1_3_0()
            self.json_schema_validators['jsd_9480fa1f47ca9254_v1_3_0'] =\
                JSONSchemaValidator9480Fa1F47Ca9254_v1_3_0()
            self.json_schema_validators['jsd_f393abe84989bb48_v1_3_0'] =\
                JSONSchemaValidatorF393Abe84989Bb48_v1_3_0()
            self.json_schema_validators['jsd_62b05b2c40a9b216_v1_3_0'] =\
                JSONSchemaValidator62B05B2C40A9B216_v1_3_0()
            self.json_schema_validators['jsd_f6b119ad4d4aaf16_v1_3_0'] =\
                JSONSchemaValidatorF6B119Ad4D4AAf16_v1_3_0()
            self.json_schema_validators['jsd_00a2fa6146089317_v1_3_0'] =\
                JSONSchemaValidator00A2Fa6146089317_v1_3_0()
            self.json_schema_validators['jsd_1399891c42a8be64_v1_3_0'] =\
                JSONSchemaValidator1399891C42A8Be64_v1_3_0()
            self.json_schema_validators['jsd_45bc7a8344a8bc1e_v1_3_0'] =\
                JSONSchemaValidator45Bc7A8344A8Bc1E_v1_3_0()
            self.json_schema_validators['jsd_4d86a993469a9da9_v1_3_0'] =\
                JSONSchemaValidator4D86A993469A9Da9_v1_3_0()
            self.json_schema_validators['jsd_17929bc7465bb564_v1_3_0'] =\
                JSONSchemaValidator17929Bc7465BB564_v1_3_0()
            self.json_schema_validators['jsd_10b06a6a4f7bb3cb_v1_3_0'] =\
                JSONSchemaValidator10B06A6A4F7BB3Cb_v1_3_0()
            self.json_schema_validators['jsd_1da5ebdd434aacfe_v1_3_0'] =\
                JSONSchemaValidator1Da5Ebdd434AAcfe_v1_3_0()
            self.json_schema_validators['jsd_47a1b84b4e1b8044_v1_3_0'] =\
                JSONSchemaValidator47A1B84B4E1B8044_v1_3_0()
            self.json_schema_validators['jsd_4d9ca8e2431a8a24_v1_3_0'] =\
                JSONSchemaValidator4D9CA8E2431A8A24_v1_3_0()
            self.json_schema_validators['jsd_55b439dc4239b140_v1_3_0'] =\
                JSONSchemaValidator55B439Dc4239B140_v1_3_0()
            self.json_schema_validators['jsd_6bacb8d14639bdc7_v1_3_0'] =\
                JSONSchemaValidator6BacB8D14639Bdc7_v1_3_0()
            self.json_schema_validators['jsd_948ea8194348bc0b_v1_3_0'] =\
                JSONSchemaValidator948EA8194348Bc0B_v1_3_0()
            self.json_schema_validators['jsd_89b36b4649999d81_v1_3_0'] =\
                JSONSchemaValidator89B36B4649999D81_v1_3_0()
            self.json_schema_validators['jsd_979688084b7ba60d_v1_3_0'] =\
                JSONSchemaValidator979688084B7BA60D_v1_3_0()
            self.json_schema_validators['jsd_a5ac99774c6bb541_v1_3_0'] =\
                JSONSchemaValidatorA5Ac99774C6BB541_v1_3_0()
            self.json_schema_validators['jsd_9788b8fc4418831d_v1_3_0'] =\
                JSONSchemaValidator9788B8Fc4418831D_v1_3_0()
            self.json_schema_validators['jsd_b68a6bd8473a9a25_v1_3_0'] =\
                JSONSchemaValidatorB68A6Bd8473A9A25_v1_3_0()
            self.json_schema_validators['jsd_fba0d80747eb82e8_v1_3_0'] =\
                JSONSchemaValidatorFba0D80747Eb82E8_v1_3_0()
            self.json_schema_validators['jsd_bf859ac64a0ba19c_v1_3_0'] =\
                JSONSchemaValidatorBf859Ac64A0BA19C_v1_3_0()
            self.json_schema_validators['jsd_c5acd9fa4c1a8abc_v1_3_0'] =\
                JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v1_3_0()
            self.json_schema_validators['jsd_709fda3c42b8877a_v1_3_0'] =\
                JSONSchemaValidator709FDa3C42B8877A_v1_3_0()
            self.json_schema_validators['jsd_7aa3da9d4e098ef2_v1_3_0'] =\
                JSONSchemaValidator7Aa3Da9D4E098Ef2_v1_3_0()
            self.json_schema_validators['jsd_d6b8ca774739adf4_v1_3_0'] =\
                JSONSchemaValidatorD6B8Ca774739Adf4_v1_3_0()
            self.json_schema_validators['jsd_a395fae644ca899c_v1_3_0'] =\
                JSONSchemaValidatorA395Fae644Ca899C_v1_3_0()
            self.json_schema_validators['jsd_07913b7f4e1880de_v1_3_0'] =\
                JSONSchemaValidator07913B7F4E1880De_v1_3_0()
            self.json_schema_validators['jsd_20872aec43b9bf50_v1_3_0'] =\
                JSONSchemaValidator20872Aec43B9Bf50_v1_3_0()
            self.json_schema_validators['jsd_a0be3a2f47ab9f3c_v1_3_0'] =\
                JSONSchemaValidatorA0Be3A2F47Ab9F3C_v1_3_0()
            self.json_schema_validators['jsd_47ba59204e0ab742_v1_3_0'] =\
                JSONSchemaValidator47Ba59204E0AB742_v1_3_0()
            self.json_schema_validators['jsd_db9f997f4e59aec1_v1_3_0'] =\
                JSONSchemaValidatorDb9F997F4E59Aec1_v1_3_0()
            self.json_schema_validators['jsd_8a96fb954d09a349_v1_3_0'] =\
                JSONSchemaValidator8A96Fb954D09A349_v1_3_0()
            self.json_schema_validators['jsd_a4b56a5f478a97dd_v1_3_0'] =\
                JSONSchemaValidatorA4B56A5F478A97Dd_v1_3_0()
            self.json_schema_validators['jsd_3b9ef9674429be4c_v1_3_0'] =\
                JSONSchemaValidator3B9EF9674429Be4C_v1_3_0()
            self.json_schema_validators['jsd_4bb22af046fa8f08_v1_3_0'] =\
                JSONSchemaValidator4Bb22Af046Fa8F08_v1_3_0()
            self.json_schema_validators['jsd_b9855ad54ae98156_v1_3_0'] =\
                JSONSchemaValidatorB9855Ad54Ae98156_v1_3_0()
            self.json_schema_validators['jsd_cd98780f4888a66d_v1_3_0'] =\
                JSONSchemaValidatorCd98780F4888A66D_v1_3_0()
            self.json_schema_validators['jsd_aeb9eb67460b92df_v1_3_0'] =\
                JSONSchemaValidatorAeb9Eb67460B92Df_v1_3_0()
            self.json_schema_validators['jsd_33aab9b842388023_v1_3_0'] =\
                JSONSchemaValidator33AaB9B842388023_v1_3_0()
            self.json_schema_validators['jsd_23896b124bd8b9bf_v1_3_0'] =\
                JSONSchemaValidator23896B124Bd8B9Bf_v1_3_0()
            self.json_schema_validators['jsd_eeb168eb41988e07_v1_3_0'] =\
                JSONSchemaValidatorEeb168Eb41988E07_v1_3_0()
            self.json_schema_validators['jsd_0b836b7b4b6a9fd5_v1_3_0'] =\
                JSONSchemaValidator0B836B7B4B6A9Fd5_v1_3_0()
            self.json_schema_validators['jsd_09b0f9ce4239ae10_v1_3_0'] =\
                JSONSchemaValidator09B0F9Ce4239Ae10_v1_3_0()
            self.json_schema_validators['jsd_1e962af345b8b59f_v1_3_0'] =\
                JSONSchemaValidator1E962Af345B8B59F_v1_3_0()
            self.json_schema_validators['jsd_21a6db2540298f55_v1_3_0'] =\
                JSONSchemaValidator21A6Db2540298F55_v1_3_0()
            self.json_schema_validators['jsd_3086c9624f498b85_v1_3_0'] =\
                JSONSchemaValidator3086C9624F498B85_v1_3_0()
            self.json_schema_validators['jsd_5889fb844939a13b_v1_3_0'] =\
                JSONSchemaValidator5889Fb844939A13B_v1_3_0()
            self.json_schema_validators['jsd_6f9819e84178870c_v1_3_0'] =\
                JSONSchemaValidator6F9819E84178870C_v1_3_0()
            self.json_schema_validators['jsd_8da0391947088a5a_v1_3_0'] =\
                JSONSchemaValidator8Da0391947088A5A_v1_3_0()
            self.json_schema_validators['jsd_848b5a7b4f9b8c12_v1_3_0'] =\
                JSONSchemaValidator848B5A7B4F9B8C12_v1_3_0()
            self.json_schema_validators['jsd_a4b6c87a4ffb9efa_v1_3_0'] =\
                JSONSchemaValidatorA4B6C87A4Ffb9Efa_v1_3_0()
            self.json_schema_validators['jsd_9e857b5a4a0bbcdb_v1_3_0'] =\
                JSONSchemaValidator9E857B5A4A0BBcdb_v1_3_0()
            self.json_schema_validators['jsd_cf9418234d9ab37e_v1_3_0'] =\
                JSONSchemaValidatorCf9418234D9AB37E_v1_3_0()
            self.json_schema_validators['jsd_f3b26b5544cabab9_v1_3_0'] =\
                JSONSchemaValidatorF3B26B5544CaBab9_v1_3_0()
            self.json_schema_validators['jsd_d8a619974a8a8c48_v1_3_0'] =\
                JSONSchemaValidatorD8A619974A8A8C48_v1_3_0()
            self.json_schema_validators['jsd_8cb6783b4faba1f4_v1_3_0'] =\
                JSONSchemaValidator8Cb6783B4FabA1F4_v1_3_0()
            self.json_schema_validators['jsd_fb9beb664f2aba4c_v1_3_0'] =\
                JSONSchemaValidatorFb9BEb664F2ABa4C_v1_3_0()
            self.json_schema_validators['jsd_bc8aab4746ca883d_v1_3_0'] =\
                JSONSchemaValidatorBc8AAb4746Ca883D_v1_3_0()
            self.json_schema_validators['jsd_828828f44f28bd0d_v1_3_0'] =\
                JSONSchemaValidator828828F44F28Bd0D_v1_3_0()
            self.json_schema_validators['jsd_2f97e8fa45f8b2a3_v1_3_0'] =\
                JSONSchemaValidator2F97E8Fa45F8B2A3_v1_3_0()
        if version == '1.3.1':
            self.json_schema_validators['jsd_00a2fa6146089317_v1_3_1'] =\
                JSONSchemaValidator00A2Fa6146089317_v1_3_1()
            self.json_schema_validators['jsd_1399891c42a8be64_v1_3_1'] =\
                JSONSchemaValidator1399891C42A8Be64_v1_3_1()
            self.json_schema_validators['jsd_45bc7a8344a8bc1e_v1_3_1'] =\
                JSONSchemaValidator45Bc7A8344A8Bc1E_v1_3_1()
            self.json_schema_validators['jsd_4d86a993469a9da9_v1_3_1'] =\
                JSONSchemaValidator4D86A993469A9Da9_v1_3_1()
            self.json_schema_validators['jsd_10b06a6a4f7bb3cb_v1_3_1'] =\
                JSONSchemaValidator10B06A6A4F7BB3Cb_v1_3_1()
            self.json_schema_validators['jsd_1da5ebdd434aacfe_v1_3_1'] =\
                JSONSchemaValidator1Da5Ebdd434AAcfe_v1_3_1()
            self.json_schema_validators['jsd_47a1b84b4e1b8044_v1_3_1'] =\
                JSONSchemaValidator47A1B84B4E1B8044_v1_3_1()
            self.json_schema_validators['jsd_55b439dc4239b140_v1_3_1'] =\
                JSONSchemaValidator55B439Dc4239B140_v1_3_1()
            self.json_schema_validators['jsd_709fda3c42b8877a_v1_3_1'] =\
                JSONSchemaValidator709FDa3C42B8877A_v1_3_1()
            self.json_schema_validators['jsd_7aa3da9d4e098ef2_v1_3_1'] =\
                JSONSchemaValidator7Aa3Da9D4E098Ef2_v1_3_1()
            self.json_schema_validators['jsd_6bacb8d14639bdc7_v1_3_1'] =\
                JSONSchemaValidator6BacB8D14639Bdc7_v1_3_1()
            self.json_schema_validators['jsd_89b36b4649999d81_v1_3_1'] =\
                JSONSchemaValidator89B36B4649999D81_v1_3_1()
            self.json_schema_validators['jsd_9788b8fc4418831d_v1_3_1'] =\
                JSONSchemaValidator9788B8Fc4418831D_v1_3_1()
            self.json_schema_validators['jsd_a5ac99774c6bb541_v1_3_1'] =\
                JSONSchemaValidatorA5Ac99774C6BB541_v1_3_1()
            self.json_schema_validators['jsd_948ea8194348bc0b_v1_3_1'] =\
                JSONSchemaValidator948EA8194348Bc0B_v1_3_1()
            self.json_schema_validators['jsd_b68a6bd8473a9a25_v1_3_1'] =\
                JSONSchemaValidatorB68A6Bd8473A9A25_v1_3_1()
            self.json_schema_validators['jsd_979688084b7ba60d_v1_3_1'] =\
                JSONSchemaValidator979688084B7BA60D_v1_3_1()
            self.json_schema_validators['jsd_fba0d80747eb82e8_v1_3_1'] =\
                JSONSchemaValidatorFba0D80747Eb82E8_v1_3_1()
            self.json_schema_validators['jsd_17929bc7465bb564_v1_3_1'] =\
                JSONSchemaValidator17929Bc7465BB564_v1_3_1()
            self.json_schema_validators['jsd_4d9ca8e2431a8a24_v1_3_1'] =\
                JSONSchemaValidator4D9CA8E2431A8A24_v1_3_1()
            self.json_schema_validators['jsd_bf859ac64a0ba19c_v1_3_1'] =\
                JSONSchemaValidatorBf859Ac64A0BA19C_v1_3_1()
            self.json_schema_validators['jsd_c5acd9fa4c1a8abc_v1_3_1'] =\
                JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v1_3_1()
            self.json_schema_validators['jsd_d6b8ca774739adf4_v1_3_1'] =\
                JSONSchemaValidatorD6B8Ca774739Adf4_v1_3_1()
            self.json_schema_validators['jsd_a395fae644ca899c_v1_3_1'] =\
                JSONSchemaValidatorA395Fae644Ca899C_v1_3_1()
            self.json_schema_validators['jsd_00aec9b1422ab27e_v1_3_1'] =\
                JSONSchemaValidator00AeC9B1422AB27E_v1_3_1()
            self.json_schema_validators['jsd_62b05b2c40a9b216_v1_3_1'] =\
                JSONSchemaValidator62B05B2C40A9B216_v1_3_1()
            self.json_schema_validators['jsd_6099da82477b858a_v1_3_1'] =\
                JSONSchemaValidator6099Da82477B858A_v1_3_1()
            self.json_schema_validators['jsd_7781fa0548a98342_v1_3_1'] =\
                JSONSchemaValidator7781Fa0548A98342_v1_3_1()
            self.json_schema_validators['jsd_f6b119ad4d4aaf16_v1_3_1'] =\
                JSONSchemaValidatorF6B119Ad4D4AAf16_v1_3_1()
            self.json_schema_validators['jsd_f393abe84989bb48_v1_3_1'] =\
                JSONSchemaValidatorF393Abe84989Bb48_v1_3_1()
            self.json_schema_validators['jsd_9480fa1f47ca9254_v1_3_1'] =\
                JSONSchemaValidator9480Fa1F47Ca9254_v1_3_1()
            self.json_schema_validators['jsd_0b836b7b4b6a9fd5_v1_3_1'] =\
                JSONSchemaValidator0B836B7B4B6A9Fd5_v1_3_1()
            self.json_schema_validators['jsd_09b0f9ce4239ae10_v1_3_1'] =\
                JSONSchemaValidator09B0F9Ce4239Ae10_v1_3_1()
            self.json_schema_validators['jsd_1e962af345b8b59f_v1_3_1'] =\
                JSONSchemaValidator1E962Af345B8B59F_v1_3_1()
            self.json_schema_validators['jsd_5889fb844939a13b_v1_3_1'] =\
                JSONSchemaValidator5889Fb844939A13B_v1_3_1()
            self.json_schema_validators['jsd_6f9819e84178870c_v1_3_1'] =\
                JSONSchemaValidator6F9819E84178870C_v1_3_1()
            self.json_schema_validators['jsd_848b5a7b4f9b8c12_v1_3_1'] =\
                JSONSchemaValidator848B5A7B4F9B8C12_v1_3_1()
            self.json_schema_validators['jsd_a4b6c87a4ffb9efa_v1_3_1'] =\
                JSONSchemaValidatorA4B6C87A4Ffb9Efa_v1_3_1()
            self.json_schema_validators['jsd_9e857b5a4a0bbcdb_v1_3_1'] =\
                JSONSchemaValidator9E857B5A4A0BBcdb_v1_3_1()
            self.json_schema_validators['jsd_21a6db2540298f55_v1_3_1'] =\
                JSONSchemaValidator21A6Db2540298F55_v1_3_1()
            self.json_schema_validators['jsd_3086c9624f498b85_v1_3_1'] =\
                JSONSchemaValidator3086C9624F498B85_v1_3_1()
            self.json_schema_validators['jsd_8da0391947088a5a_v1_3_1'] =\
                JSONSchemaValidator8Da0391947088A5A_v1_3_1()
            self.json_schema_validators['jsd_f3b26b5544cabab9_v1_3_1'] =\
                JSONSchemaValidatorF3B26B5544CaBab9_v1_3_1()
            self.json_schema_validators['jsd_cf9418234d9ab37e_v1_3_1'] =\
                JSONSchemaValidatorCf9418234D9AB37E_v1_3_1()
            self.json_schema_validators['jsd_d8a619974a8a8c48_v1_3_1'] =\
                JSONSchemaValidatorD8A619974A8A8C48_v1_3_1()
            self.json_schema_validators['jsd_8cb6783b4faba1f4_v1_3_1'] =\
                JSONSchemaValidator8Cb6783B4FabA1F4_v1_3_1()
            self.json_schema_validators['jsd_bc8aab4746ca883d_v1_3_1'] =\
                JSONSchemaValidatorBc8AAb4746Ca883D_v1_3_1()
            self.json_schema_validators['jsd_fb9beb664f2aba4c_v1_3_1'] =\
                JSONSchemaValidatorFb9BEb664F2ABa4C_v1_3_1()
            self.json_schema_validators['jsd_6f9cda9a465884b4_v1_3_1'] =\
                JSONSchemaValidator6F9CDa9A465884B4_v1_3_1()
            self.json_schema_validators['jsd_2f97e8fa45f8b2a3_v1_3_1'] =\
                JSONSchemaValidator2F97E8Fa45F8B2A3_v1_3_1()
            self.json_schema_validators['jsd_4bb22af046fa8f08_v1_3_1'] =\
                JSONSchemaValidator4Bb22Af046Fa8F08_v1_3_1()
            self.json_schema_validators['jsd_aeb9eb67460b92df_v1_3_1'] =\
                JSONSchemaValidatorAeb9Eb67460B92Df_v1_3_1()
            self.json_schema_validators['jsd_3b9ef9674429be4c_v1_3_1'] =\
                JSONSchemaValidator3B9EF9674429Be4C_v1_3_1()
            self.json_schema_validators['jsd_b9855ad54ae98156_v1_3_1'] =\
                JSONSchemaValidatorB9855Ad54Ae98156_v1_3_1()
            self.json_schema_validators['jsd_cd98780f4888a66d_v1_3_1'] =\
                JSONSchemaValidatorCd98780F4888A66D_v1_3_1()
            self.json_schema_validators['jsd_eeb7eb4b4bd8a1dd_v1_3_1'] =\
                JSONSchemaValidatorEeb7Eb4B4Bd8A1Dd_v1_3_1()
            self.json_schema_validators['jsd_eeb168eb41988e07_v1_3_1'] =\
                JSONSchemaValidatorEeb168Eb41988E07_v1_3_1()
            self.json_schema_validators['jsd_50b589fd4c7a930a_v1_3_1'] =\
                JSONSchemaValidator50B589Fd4C7A930A_v1_3_1()
            self.json_schema_validators['jsd_4f9f7a7b40f990de_v1_3_1'] =\
                JSONSchemaValidator4F9F7A7B40F990De_v1_3_1()
            self.json_schema_validators['jsd_579a6a7248cb94cf_v1_3_1'] =\
                JSONSchemaValidator579A6A7248Cb94Cf_v1_3_1()
            self.json_schema_validators['jsd_1eb72ad34e098990_v1_3_1'] =\
                JSONSchemaValidator1Eb72Ad34E098990_v1_3_1()
            self.json_schema_validators['jsd_cfbd3870405aad55_v1_3_1'] =\
                JSONSchemaValidatorCfbd3870405AAd55_v1_3_1()
            self.json_schema_validators['jsd_709769624bf988d5_v1_3_1'] =\
                JSONSchemaValidator709769624Bf988D5_v1_3_1()
            self.json_schema_validators['jsd_8a96fb954d09a349_v1_3_1'] =\
                JSONSchemaValidator8A96Fb954D09A349_v1_3_1()
            self.json_schema_validators['jsd_87a5ab044139862d_v1_3_1'] =\
                JSONSchemaValidator87A5Ab044139862D_v1_3_1()
            self.json_schema_validators['jsd_b78329674878b815_v1_3_1'] =\
                JSONSchemaValidatorB78329674878B815_v1_3_1()
            self.json_schema_validators['jsd_d09b08a3447aa3b9_v1_3_1'] =\
                JSONSchemaValidatorD09B08A3447AA3B9_v1_3_1()
            self.json_schema_validators['jsd_e9b99b2248c88014_v1_3_1'] =\
                JSONSchemaValidatorE9B99B2248C88014_v1_3_1()
            self.json_schema_validators['jsd_8984ea7744d98a54_v1_3_1'] =\
                JSONSchemaValidator8984Ea7744D98A54_v1_3_1()
            self.json_schema_validators['jsd_9582ab824ce8b29d_v1_3_1'] =\
                JSONSchemaValidator9582Ab824Ce8B29D_v1_3_1()
            self.json_schema_validators['jsd_87a8ba444ce9bc59_v1_3_1'] =\
                JSONSchemaValidator87A8Ba444Ce9Bc59_v1_3_1()
            self.json_schema_validators['jsd_bca339d844c8a3c0_v1_3_1'] =\
                JSONSchemaValidatorBca339D844C8A3C0_v1_3_1()
            self.json_schema_validators['jsd_208579ea4ed98f4f_v1_3_1'] =\
                JSONSchemaValidator208579Ea4Ed98F4F_v1_3_1()
            self.json_schema_validators['jsd_bead7b3443b996a7_v1_3_1'] =\
                JSONSchemaValidatorBead7B3443B996A7_v1_3_1()
            self.json_schema_validators['jsd_3e94cb1b485b8b0e_v1_3_1'] =\
                JSONSchemaValidator3E94Cb1B485B8B0E_v1_3_1()
            self.json_schema_validators['jsd_fb9bf80f491a9851_v1_3_1'] =\
                JSONSchemaValidatorFb9BF80F491A9851_v1_3_1()
            self.json_schema_validators['jsd_398668874439a41d_v1_3_1'] =\
                JSONSchemaValidator398668874439A41D_v1_3_1()
        if version == '1.3.3':
            self.json_schema_validators['jsd_00a2fa6146089317_v1_3_3'] =\
                JSONSchemaValidator00A2Fa6146089317_v1_3_3()
            self.json_schema_validators['jsd_1399891c42a8be64_v1_3_3'] =\
                JSONSchemaValidator1399891C42A8Be64_v1_3_3()
            self.json_schema_validators['jsd_45bc7a8344a8bc1e_v1_3_3'] =\
                JSONSchemaValidator45Bc7A8344A8Bc1E_v1_3_3()
            self.json_schema_validators['jsd_4d86a993469a9da9_v1_3_3'] =\
                JSONSchemaValidator4D86A993469A9Da9_v1_3_3()
            self.json_schema_validators['jsd_17929bc7465bb564_v1_3_3'] =\
                JSONSchemaValidator17929Bc7465BB564_v1_3_3()
            self.json_schema_validators['jsd_10b06a6a4f7bb3cb_v1_3_3'] =\
                JSONSchemaValidator10B06A6A4F7BB3Cb_v1_3_3()
            self.json_schema_validators['jsd_1da5ebdd434aacfe_v1_3_3'] =\
                JSONSchemaValidator1Da5Ebdd434AAcfe_v1_3_3()
            self.json_schema_validators['jsd_47a1b84b4e1b8044_v1_3_3'] =\
                JSONSchemaValidator47A1B84B4E1B8044_v1_3_3()
            self.json_schema_validators['jsd_4d9ca8e2431a8a24_v1_3_3'] =\
                JSONSchemaValidator4D9CA8E2431A8A24_v1_3_3()
            self.json_schema_validators['jsd_55b439dc4239b140_v1_3_3'] =\
                JSONSchemaValidator55B439Dc4239B140_v1_3_3()
            self.json_schema_validators['jsd_709fda3c42b8877a_v1_3_3'] =\
                JSONSchemaValidator709FDa3C42B8877A_v1_3_3()
            self.json_schema_validators['jsd_6bacb8d14639bdc7_v1_3_3'] =\
                JSONSchemaValidator6BacB8D14639Bdc7_v1_3_3()
            self.json_schema_validators['jsd_7aa3da9d4e098ef2_v1_3_3'] =\
                JSONSchemaValidator7Aa3Da9D4E098Ef2_v1_3_3()
            self.json_schema_validators['jsd_89b36b4649999d81_v1_3_3'] =\
                JSONSchemaValidator89B36B4649999D81_v1_3_3()
            self.json_schema_validators['jsd_9788b8fc4418831d_v1_3_3'] =\
                JSONSchemaValidator9788B8Fc4418831D_v1_3_3()
            self.json_schema_validators['jsd_948ea8194348bc0b_v1_3_3'] =\
                JSONSchemaValidator948EA8194348Bc0B_v1_3_3()
            self.json_schema_validators['jsd_a5ac99774c6bb541_v1_3_3'] =\
                JSONSchemaValidatorA5Ac99774C6BB541_v1_3_3()
            self.json_schema_validators['jsd_979688084b7ba60d_v1_3_3'] =\
                JSONSchemaValidator979688084B7BA60D_v1_3_3()
            self.json_schema_validators['jsd_b68a6bd8473a9a25_v1_3_3'] =\
                JSONSchemaValidatorB68A6Bd8473A9A25_v1_3_3()
            self.json_schema_validators['jsd_bf859ac64a0ba19c_v1_3_3'] =\
                JSONSchemaValidatorBf859Ac64A0BA19C_v1_3_3()
            self.json_schema_validators['jsd_c5acd9fa4c1a8abc_v1_3_3'] =\
                JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v1_3_3()
            self.json_schema_validators['jsd_fba0d80747eb82e8_v1_3_3'] =\
                JSONSchemaValidatorFba0D80747Eb82E8_v1_3_3()
            self.json_schema_validators['jsd_d6b8ca774739adf4_v1_3_3'] =\
                JSONSchemaValidatorD6B8Ca774739Adf4_v1_3_3()
            self.json_schema_validators['jsd_a395fae644ca899c_v1_3_3'] =\
                JSONSchemaValidatorA395Fae644Ca899C_v1_3_3()
            self.json_schema_validators['jsd_00aec9b1422ab27e_v1_3_3'] =\
                JSONSchemaValidator00AeC9B1422AB27E_v1_3_3()
            self.json_schema_validators['jsd_62b05b2c40a9b216_v1_3_3'] =\
                JSONSchemaValidator62B05B2C40A9B216_v1_3_3()
            self.json_schema_validators['jsd_6099da82477b858a_v1_3_3'] =\
                JSONSchemaValidator6099Da82477B858A_v1_3_3()
            self.json_schema_validators['jsd_7781fa0548a98342_v1_3_3'] =\
                JSONSchemaValidator7781Fa0548A98342_v1_3_3()
            self.json_schema_validators['jsd_9480fa1f47ca9254_v1_3_3'] =\
                JSONSchemaValidator9480Fa1F47Ca9254_v1_3_3()
            self.json_schema_validators['jsd_f393abe84989bb48_v1_3_3'] =\
                JSONSchemaValidatorF393Abe84989Bb48_v1_3_3()
            self.json_schema_validators['jsd_f6b119ad4d4aaf16_v1_3_3'] =\
                JSONSchemaValidatorF6B119Ad4D4AAf16_v1_3_3()
            self.json_schema_validators['jsd_0b836b7b4b6a9fd5_v1_3_3'] =\
                JSONSchemaValidator0B836B7B4B6A9Fd5_v1_3_3()
            self.json_schema_validators['jsd_09b0f9ce4239ae10_v1_3_3'] =\
                JSONSchemaValidator09B0F9Ce4239Ae10_v1_3_3()
            self.json_schema_validators['jsd_21a6db2540298f55_v1_3_3'] =\
                JSONSchemaValidator21A6Db2540298F55_v1_3_3()
            self.json_schema_validators['jsd_1e962af345b8b59f_v1_3_3'] =\
                JSONSchemaValidator1E962Af345B8B59F_v1_3_3()
            self.json_schema_validators['jsd_3086c9624f498b85_v1_3_3'] =\
                JSONSchemaValidator3086C9624F498B85_v1_3_3()
            self.json_schema_validators['jsd_5889fb844939a13b_v1_3_3'] =\
                JSONSchemaValidator5889Fb844939A13B_v1_3_3()
            self.json_schema_validators['jsd_6f9819e84178870c_v1_3_3'] =\
                JSONSchemaValidator6F9819E84178870C_v1_3_3()
            self.json_schema_validators['jsd_848b5a7b4f9b8c12_v1_3_3'] =\
                JSONSchemaValidator848B5A7B4F9B8C12_v1_3_3()
            self.json_schema_validators['jsd_8da0391947088a5a_v1_3_3'] =\
                JSONSchemaValidator8Da0391947088A5A_v1_3_3()
            self.json_schema_validators['jsd_9e857b5a4a0bbcdb_v1_3_3'] =\
                JSONSchemaValidator9E857B5A4A0BBcdb_v1_3_3()
            self.json_schema_validators['jsd_a4b6c87a4ffb9efa_v1_3_3'] =\
                JSONSchemaValidatorA4B6C87A4Ffb9Efa_v1_3_3()
            self.json_schema_validators['jsd_cf9418234d9ab37e_v1_3_3'] =\
                JSONSchemaValidatorCf9418234D9AB37E_v1_3_3()
            self.json_schema_validators['jsd_d8a619974a8a8c48_v1_3_3'] =\
                JSONSchemaValidatorD8A619974A8A8C48_v1_3_3()
            self.json_schema_validators['jsd_f3b26b5544cabab9_v1_3_3'] =\
                JSONSchemaValidatorF3B26B5544CaBab9_v1_3_3()
            self.json_schema_validators['jsd_8cb6783b4faba1f4_v1_3_3'] =\
                JSONSchemaValidator8Cb6783B4FabA1F4_v1_3_3()
            self.json_schema_validators['jsd_bc8aab4746ca883d_v1_3_3'] =\
                JSONSchemaValidatorBc8AAb4746Ca883D_v1_3_3()
            self.json_schema_validators['jsd_fb9beb664f2aba4c_v1_3_3'] =\
                JSONSchemaValidatorFb9BEb664F2ABa4C_v1_3_3()
            self.json_schema_validators['jsd_03b4c8b44919b964_v1_3_3'] =\
                JSONSchemaValidator03B4C8B44919B964_v1_3_3()
            self.json_schema_validators['jsd_4da91a544e29842d_v1_3_3'] =\
                JSONSchemaValidator4Da91A544E29842D_v1_3_3()
            self.json_schema_validators['jsd_5087daae4cc98566_v1_3_3'] =\
                JSONSchemaValidator5087Daae4Cc98566_v1_3_3()
            self.json_schema_validators['jsd_4f947a1c4fc884f6_v1_3_3'] =\
                JSONSchemaValidator4F947A1C4Fc884F6_v1_3_3()
            self.json_schema_validators['jsd_698bfbb44dcb9fca_v1_3_3'] =\
                JSONSchemaValidator698BFbb44Dcb9Fca_v1_3_3()
            self.json_schema_validators['jsd_a39a1a214debb781_v1_3_3'] =\
                JSONSchemaValidatorA39A1A214DebB781_v1_3_3()
            self.json_schema_validators['jsd_be892bd84a78865a_v1_3_3'] =\
                JSONSchemaValidatorBe892Bd84A78865A_v1_3_3()
            self.json_schema_validators['jsd_fbb95b37484a9fce_v1_3_3'] =\
                JSONSchemaValidatorFbb95B37484A9Fce_v1_3_3()
            self.json_schema_validators['jsd_f793192a43dabed9_v1_3_3'] =\
                JSONSchemaValidatorF793192A43DaBed9_v1_3_3()
            self.json_schema_validators['jsd_2f97e8fa45f8b2a3_v1_3_3'] =\
                JSONSchemaValidator2F97E8Fa45F8B2A3_v1_3_3()
            self.json_schema_validators['jsd_6f9cda9a465884b4_v1_3_3'] =\
                JSONSchemaValidator6F9CDa9A465884B4_v1_3_3()
            self.json_schema_validators['jsd_3b9ef9674429be4c_v1_3_3'] =\
                JSONSchemaValidator3B9EF9674429Be4C_v1_3_3()
            self.json_schema_validators['jsd_4bb22af046fa8f08_v1_3_3'] =\
                JSONSchemaValidator4Bb22Af046Fa8F08_v1_3_3()
            self.json_schema_validators['jsd_b9855ad54ae98156_v1_3_3'] =\
                JSONSchemaValidatorB9855Ad54Ae98156_v1_3_3()
            self.json_schema_validators['jsd_cd98780f4888a66d_v1_3_3'] =\
                JSONSchemaValidatorCd98780F4888A66D_v1_3_3()
            self.json_schema_validators['jsd_aeb9eb67460b92df_v1_3_3'] =\
                JSONSchemaValidatorAeb9Eb67460B92Df_v1_3_3()
            self.json_schema_validators['jsd_eeb168eb41988e07_v1_3_3'] =\
                JSONSchemaValidatorEeb168Eb41988E07_v1_3_3()
            self.json_schema_validators['jsd_50b589fd4c7a930a_v1_3_3'] =\
                JSONSchemaValidator50B589Fd4C7A930A_v1_3_3()
            self.json_schema_validators['jsd_eeb7eb4b4bd8a1dd_v1_3_3'] =\
                JSONSchemaValidatorEeb7Eb4B4Bd8A1Dd_v1_3_3()
            self.json_schema_validators['jsd_4f9f7a7b40f990de_v1_3_3'] =\
                JSONSchemaValidator4F9F7A7B40F990De_v1_3_3()
            self.json_schema_validators['jsd_579a6a7248cb94cf_v1_3_3'] =\
                JSONSchemaValidator579A6A7248Cb94Cf_v1_3_3()
            self.json_schema_validators['jsd_1eb72ad34e098990_v1_3_3'] =\
                JSONSchemaValidator1Eb72Ad34E098990_v1_3_3()
            self.json_schema_validators['jsd_709769624bf988d5_v1_3_3'] =\
                JSONSchemaValidator709769624Bf988D5_v1_3_3()
            self.json_schema_validators['jsd_87a5ab044139862d_v1_3_3'] =\
                JSONSchemaValidator87A5Ab044139862D_v1_3_3()
            self.json_schema_validators['jsd_8a96fb954d09a349_v1_3_3'] =\
                JSONSchemaValidator8A96Fb954D09A349_v1_3_3()
            self.json_schema_validators['jsd_b78329674878b815_v1_3_3'] =\
                JSONSchemaValidatorB78329674878B815_v1_3_3()
            self.json_schema_validators['jsd_d09b08a3447aa3b9_v1_3_3'] =\
                JSONSchemaValidatorD09B08A3447AA3B9_v1_3_3()
            self.json_schema_validators['jsd_cfbd3870405aad55_v1_3_3'] =\
                JSONSchemaValidatorCfbd3870405AAd55_v1_3_3()
            self.json_schema_validators['jsd_e9b99b2248c88014_v1_3_3'] =\
                JSONSchemaValidatorE9B99B2248C88014_v1_3_3()
            self.json_schema_validators['jsd_208579ea4ed98f4f_v1_3_3'] =\
                JSONSchemaValidator208579Ea4Ed98F4F_v1_3_3()
            self.json_schema_validators['jsd_518c59cd441aa9fc_v1_3_3'] =\
                JSONSchemaValidator518C59Cd441AA9Fc_v1_3_3()
            self.json_schema_validators['jsd_6db9292d4f28a26b_v1_3_3'] =\
                JSONSchemaValidator6Db9292D4F28A26B_v1_3_3()
            self.json_schema_validators['jsd_87a8ba444ce9bc59_v1_3_3'] =\
                JSONSchemaValidator87A8Ba444Ce9Bc59_v1_3_3()
            self.json_schema_validators['jsd_9582ab824ce8b29d_v1_3_3'] =\
                JSONSchemaValidator9582Ab824Ce8B29D_v1_3_3()
            self.json_schema_validators['jsd_8984ea7744d98a54_v1_3_3'] =\
                JSONSchemaValidator8984Ea7744D98A54_v1_3_3()
            self.json_schema_validators['jsd_bead7b3443b996a7_v1_3_3'] =\
                JSONSchemaValidatorBead7B3443B996A7_v1_3_3()
            self.json_schema_validators['jsd_c2a43ad24098baa7_v1_3_3'] =\
                JSONSchemaValidatorC2A43Ad24098Baa7_v1_3_3()
            self.json_schema_validators['jsd_bca339d844c8a3c0_v1_3_3'] =\
                JSONSchemaValidatorBca339D844C8A3C0_v1_3_3()
            self.json_schema_validators['jsd_dd85c91042489a3f_v1_3_3'] =\
                JSONSchemaValidatorDd85C91042489A3F_v1_3_3()
            self.json_schema_validators['jsd_d2b4d9d04a4b884c_v1_3_3'] =\
                JSONSchemaValidatorD2B4D9D04A4B884C_v1_3_3()
            self.json_schema_validators['jsd_398668874439a41d_v1_3_3'] =\
                JSONSchemaValidator398668874439A41D_v1_3_3()
            self.json_schema_validators['jsd_3e94cb1b485b8b0e_v1_3_3'] =\
                JSONSchemaValidator3E94Cb1B485B8B0E_v1_3_3()
            self.json_schema_validators['jsd_fb9bf80f491a9851_v1_3_3'] =\
                JSONSchemaValidatorFb9BF80F491A9851_v1_3_3()
        if version == '2.1.1':
            self.json_schema_validators['jsd_17929bc7465bb564_v2_1_1'] =\
                JSONSchemaValidator17929Bc7465BB564_v2_1_1()
            self.json_schema_validators['jsd_10b06a6a4f7bb3cb_v2_1_1'] =\
                JSONSchemaValidator10B06A6A4F7BB3Cb_v2_1_1()
            self.json_schema_validators['jsd_1da5ebdd434aacfe_v2_1_1'] =\
                JSONSchemaValidator1Da5Ebdd434AAcfe_v2_1_1()
            self.json_schema_validators['jsd_47a1b84b4e1b8044_v2_1_1'] =\
                JSONSchemaValidator47A1B84B4E1B8044_v2_1_1()
            self.json_schema_validators['jsd_4d9ca8e2431a8a24_v2_1_1'] =\
                JSONSchemaValidator4D9CA8E2431A8A24_v2_1_1()
            self.json_schema_validators['jsd_55b439dc4239b140_v2_1_1'] =\
                JSONSchemaValidator55B439Dc4239B140_v2_1_1()
            self.json_schema_validators['jsd_6bacb8d14639bdc7_v2_1_1'] =\
                JSONSchemaValidator6BacB8D14639Bdc7_v2_1_1()
            self.json_schema_validators['jsd_709fda3c42b8877a_v2_1_1'] =\
                JSONSchemaValidator709FDa3C42B8877A_v2_1_1()
            self.json_schema_validators['jsd_7aa3da9d4e098ef2_v2_1_1'] =\
                JSONSchemaValidator7Aa3Da9D4E098Ef2_v2_1_1()
            self.json_schema_validators['jsd_979688084b7ba60d_v2_1_1'] =\
                JSONSchemaValidator979688084B7BA60D_v2_1_1()
            self.json_schema_validators['jsd_89b36b4649999d81_v2_1_1'] =\
                JSONSchemaValidator89B36B4649999D81_v2_1_1()
            self.json_schema_validators['jsd_948ea8194348bc0b_v2_1_1'] =\
                JSONSchemaValidator948EA8194348Bc0B_v2_1_1()
            self.json_schema_validators['jsd_a5ac99774c6bb541_v2_1_1'] =\
                JSONSchemaValidatorA5Ac99774C6BB541_v2_1_1()
            self.json_schema_validators['jsd_9788b8fc4418831d_v2_1_1'] =\
                JSONSchemaValidator9788B8Fc4418831D_v2_1_1()
            self.json_schema_validators['jsd_bf859ac64a0ba19c_v2_1_1'] =\
                JSONSchemaValidatorBf859Ac64A0BA19C_v2_1_1()
            self.json_schema_validators['jsd_b68a6bd8473a9a25_v2_1_1'] =\
                JSONSchemaValidatorB68A6Bd8473A9A25_v2_1_1()
            self.json_schema_validators['jsd_c5acd9fa4c1a8abc_v2_1_1'] =\
                JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v2_1_1()
            self.json_schema_validators['jsd_fba0d80747eb82e8_v2_1_1'] =\
                JSONSchemaValidatorFba0D80747Eb82E8_v2_1_1()
            self.json_schema_validators['jsd_00a2fa6146089317_v2_1_1'] =\
                JSONSchemaValidator00A2Fa6146089317_v2_1_1()
            self.json_schema_validators['jsd_1399891c42a8be64_v2_1_1'] =\
                JSONSchemaValidator1399891C42A8Be64_v2_1_1()
            self.json_schema_validators['jsd_45bc7a8344a8bc1e_v2_1_1'] =\
                JSONSchemaValidator45Bc7A8344A8Bc1E_v2_1_1()
            self.json_schema_validators['jsd_4d86a993469a9da9_v2_1_1'] =\
                JSONSchemaValidator4D86A993469A9Da9_v2_1_1()
            self.json_schema_validators['jsd_d6b8ca774739adf4_v2_1_1'] =\
                JSONSchemaValidatorD6B8Ca774739Adf4_v2_1_1()
            self.json_schema_validators['jsd_a395fae644ca899c_v2_1_1'] =\
                JSONSchemaValidatorA395Fae644Ca899C_v2_1_1()
            self.json_schema_validators['jsd_00aec9b1422ab27e_v2_1_1'] =\
                JSONSchemaValidator00AeC9B1422AB27E_v2_1_1()
            self.json_schema_validators['jsd_6099da82477b858a_v2_1_1'] =\
                JSONSchemaValidator6099Da82477B858A_v2_1_1()
            self.json_schema_validators['jsd_62b05b2c40a9b216_v2_1_1'] =\
                JSONSchemaValidator62B05B2C40A9B216_v2_1_1()
            self.json_schema_validators['jsd_7781fa0548a98342_v2_1_1'] =\
                JSONSchemaValidator7781Fa0548A98342_v2_1_1()
            self.json_schema_validators['jsd_9480fa1f47ca9254_v2_1_1'] =\
                JSONSchemaValidator9480Fa1F47Ca9254_v2_1_1()
            self.json_schema_validators['jsd_f393abe84989bb48_v2_1_1'] =\
                JSONSchemaValidatorF393Abe84989Bb48_v2_1_1()
            self.json_schema_validators['jsd_f6b119ad4d4aaf16_v2_1_1'] =\
                JSONSchemaValidatorF6B119Ad4D4AAf16_v2_1_1()
            self.json_schema_validators['jsd_0b836b7b4b6a9fd5_v2_1_1'] =\
                JSONSchemaValidator0B836B7B4B6A9Fd5_v2_1_1()
            self.json_schema_validators['jsd_09b0f9ce4239ae10_v2_1_1'] =\
                JSONSchemaValidator09B0F9Ce4239Ae10_v2_1_1()
            self.json_schema_validators['jsd_1e962af345b8b59f_v2_1_1'] =\
                JSONSchemaValidator1E962Af345B8B59F_v2_1_1()
            self.json_schema_validators['jsd_21a6db2540298f55_v2_1_1'] =\
                JSONSchemaValidator21A6Db2540298F55_v2_1_1()
            self.json_schema_validators['jsd_3086c9624f498b85_v2_1_1'] =\
                JSONSchemaValidator3086C9624F498B85_v2_1_1()
            self.json_schema_validators['jsd_5889fb844939a13b_v2_1_1'] =\
                JSONSchemaValidator5889Fb844939A13B_v2_1_1()
            self.json_schema_validators['jsd_6f9819e84178870c_v2_1_1'] =\
                JSONSchemaValidator6F9819E84178870C_v2_1_1()
            self.json_schema_validators['jsd_8da0391947088a5a_v2_1_1'] =\
                JSONSchemaValidator8Da0391947088A5A_v2_1_1()
            self.json_schema_validators['jsd_848b5a7b4f9b8c12_v2_1_1'] =\
                JSONSchemaValidator848B5A7B4F9B8C12_v2_1_1()
            self.json_schema_validators['jsd_9e857b5a4a0bbcdb_v2_1_1'] =\
                JSONSchemaValidator9E857B5A4A0BBcdb_v2_1_1()
            self.json_schema_validators['jsd_a4b6c87a4ffb9efa_v2_1_1'] =\
                JSONSchemaValidatorA4B6C87A4Ffb9Efa_v2_1_1()
            self.json_schema_validators['jsd_cf9418234d9ab37e_v2_1_1'] =\
                JSONSchemaValidatorCf9418234D9AB37E_v2_1_1()
            self.json_schema_validators['jsd_d8a619974a8a8c48_v2_1_1'] =\
                JSONSchemaValidatorD8A619974A8A8C48_v2_1_1()
            self.json_schema_validators['jsd_f3b26b5544cabab9_v2_1_1'] =\
                JSONSchemaValidatorF3B26B5544CaBab9_v2_1_1()
            self.json_schema_validators['jsd_8cb6783b4faba1f4_v2_1_1'] =\
                JSONSchemaValidator8Cb6783B4FabA1F4_v2_1_1()
            self.json_schema_validators['jsd_bc8aab4746ca883d_v2_1_1'] =\
                JSONSchemaValidatorBc8AAb4746Ca883D_v2_1_1()
            self.json_schema_validators['jsd_fb9beb664f2aba4c_v2_1_1'] =\
                JSONSchemaValidatorFb9BEb664F2ABa4C_v2_1_1()
            self.json_schema_validators['jsd_3faaa9944b49bc9f_v2_1_1'] =\
                JSONSchemaValidator3FaaA9944B49Bc9F_v2_1_1()
            self.json_schema_validators['jsd_4ababa75489ab24b_v2_1_1'] =\
                JSONSchemaValidator4AbaBa75489AB24B_v2_1_1()
            self.json_schema_validators['jsd_64b9dad0403aaca1_v2_1_1'] =\
                JSONSchemaValidator64B9Dad0403AAca1_v2_1_1()
            self.json_schema_validators['jsd_03b4c8b44919b964_v2_1_1'] =\
                JSONSchemaValidator03B4C8B44919B964_v2_1_1()
            self.json_schema_validators['jsd_5087daae4cc98566_v2_1_1'] =\
                JSONSchemaValidator5087Daae4Cc98566_v2_1_1()
            self.json_schema_validators['jsd_4da91a544e29842d_v2_1_1'] =\
                JSONSchemaValidator4Da91A544E29842D_v2_1_1()
            self.json_schema_validators['jsd_698bfbb44dcb9fca_v2_1_1'] =\
                JSONSchemaValidator698BFbb44Dcb9Fca_v2_1_1()
            self.json_schema_validators['jsd_4f947a1c4fc884f6_v2_1_1'] =\
                JSONSchemaValidator4F947A1C4Fc884F6_v2_1_1()
            self.json_schema_validators['jsd_a39a1a214debb781_v2_1_1'] =\
                JSONSchemaValidatorA39A1A214DebB781_v2_1_1()
            self.json_schema_validators['jsd_be892bd84a78865a_v2_1_1'] =\
                JSONSchemaValidatorBe892Bd84A78865A_v2_1_1()
            self.json_schema_validators['jsd_fbb95b37484a9fce_v2_1_1'] =\
                JSONSchemaValidatorFbb95B37484A9Fce_v2_1_1()
            self.json_schema_validators['jsd_f793192a43dabed9_v2_1_1'] =\
                JSONSchemaValidatorF793192A43DaBed9_v2_1_1()
            self.json_schema_validators['jsd_0fa00adf48698287_v2_1_1'] =\
                JSONSchemaValidator0Fa00Adf48698287_v2_1_1()
            self.json_schema_validators['jsd_2f97e8fa45f8b2a3_v2_1_1'] =\
                JSONSchemaValidator2F97E8Fa45F8B2A3_v2_1_1()
            self.json_schema_validators['jsd_66951aaa407ba89c_v2_1_1'] =\
                JSONSchemaValidator66951Aaa407BA89C_v2_1_1()
            self.json_schema_validators['jsd_6f9cda9a465884b4_v2_1_1'] =\
                JSONSchemaValidator6F9CDa9A465884B4_v2_1_1()
            self.json_schema_validators['jsd_3b9ef9674429be4c_v2_1_1'] =\
                JSONSchemaValidator3B9EF9674429Be4C_v2_1_1()
            self.json_schema_validators['jsd_4bb22af046fa8f08_v2_1_1'] =\
                JSONSchemaValidator4Bb22Af046Fa8F08_v2_1_1()
            self.json_schema_validators['jsd_aeb9eb67460b92df_v2_1_1'] =\
                JSONSchemaValidatorAeb9Eb67460B92Df_v2_1_1()
            self.json_schema_validators['jsd_b9855ad54ae98156_v2_1_1'] =\
                JSONSchemaValidatorB9855Ad54Ae98156_v2_1_1()
            self.json_schema_validators['jsd_cd98780f4888a66d_v2_1_1'] =\
                JSONSchemaValidatorCd98780F4888A66D_v2_1_1()
            self.json_schema_validators['jsd_eeb168eb41988e07_v2_1_1'] =\
                JSONSchemaValidatorEeb168Eb41988E07_v2_1_1()
            self.json_schema_validators['jsd_50b589fd4c7a930a_v2_1_1'] =\
                JSONSchemaValidator50B589Fd4C7A930A_v2_1_1()
            self.json_schema_validators['jsd_eeb7eb4b4bd8a1dd_v2_1_1'] =\
                JSONSchemaValidatorEeb7Eb4B4Bd8A1Dd_v2_1_1()
            self.json_schema_validators['jsd_579a6a7248cb94cf_v2_1_1'] =\
                JSONSchemaValidator579A6A7248Cb94Cf_v2_1_1()
            self.json_schema_validators['jsd_4f9f7a7b40f990de_v2_1_1'] =\
                JSONSchemaValidator4F9F7A7B40F990De_v2_1_1()
            self.json_schema_validators['jsd_208579ea4ed98f4f_v2_1_1'] =\
                JSONSchemaValidator208579Ea4Ed98F4F_v2_1_1()
            self.json_schema_validators['jsd_518c59cd441aa9fc_v2_1_1'] =\
                JSONSchemaValidator518C59Cd441AA9Fc_v2_1_1()
            self.json_schema_validators['jsd_8984ea7744d98a54_v2_1_1'] =\
                JSONSchemaValidator8984Ea7744D98A54_v2_1_1()
            self.json_schema_validators['jsd_6db9292d4f28a26b_v2_1_1'] =\
                JSONSchemaValidator6Db9292D4F28A26B_v2_1_1()
            self.json_schema_validators['jsd_87a8ba444ce9bc59_v2_1_1'] =\
                JSONSchemaValidator87A8Ba444Ce9Bc59_v2_1_1()
            self.json_schema_validators['jsd_9582ab824ce8b29d_v2_1_1'] =\
                JSONSchemaValidator9582Ab824Ce8B29D_v2_1_1()
            self.json_schema_validators['jsd_bca339d844c8a3c0_v2_1_1'] =\
                JSONSchemaValidatorBca339D844C8A3C0_v2_1_1()
            self.json_schema_validators['jsd_d2b4d9d04a4b884c_v2_1_1'] =\
                JSONSchemaValidatorD2B4D9D04A4B884C_v2_1_1()
            self.json_schema_validators['jsd_bead7b3443b996a7_v2_1_1'] =\
                JSONSchemaValidatorBead7B3443B996A7_v2_1_1()
            self.json_schema_validators['jsd_c2a43ad24098baa7_v2_1_1'] =\
                JSONSchemaValidatorC2A43Ad24098Baa7_v2_1_1()
            self.json_schema_validators['jsd_dd85c91042489a3f_v2_1_1'] =\
                JSONSchemaValidatorDd85C91042489A3F_v2_1_1()
            self.json_schema_validators['jsd_1eb72ad34e098990_v2_1_1'] =\
                JSONSchemaValidator1Eb72Ad34E098990_v2_1_1()
            self.json_schema_validators['jsd_709769624bf988d5_v2_1_1'] =\
                JSONSchemaValidator709769624Bf988D5_v2_1_1()
            self.json_schema_validators['jsd_87a5ab044139862d_v2_1_1'] =\
                JSONSchemaValidator87A5Ab044139862D_v2_1_1()
            self.json_schema_validators['jsd_8a96fb954d09a349_v2_1_1'] =\
                JSONSchemaValidator8A96Fb954D09A349_v2_1_1()
            self.json_schema_validators['jsd_b78329674878b815_v2_1_1'] =\
                JSONSchemaValidatorB78329674878B815_v2_1_1()
            self.json_schema_validators['jsd_d09b08a3447aa3b9_v2_1_1'] =\
                JSONSchemaValidatorD09B08A3447AA3B9_v2_1_1()
            self.json_schema_validators['jsd_e9b99b2248c88014_v2_1_1'] =\
                JSONSchemaValidatorE9B99B2248C88014_v2_1_1()
            self.json_schema_validators['jsd_d89719b847aaa9c4_v2_1_1'] =\
                JSONSchemaValidatorD89719B847AaA9C4_v2_1_1()
            self.json_schema_validators['jsd_cfbd3870405aad55_v2_1_1'] =\
                JSONSchemaValidatorCfbd3870405AAd55_v2_1_1()
            self.json_schema_validators['jsd_3e94cb1b485b8b0e_v2_1_1'] =\
                JSONSchemaValidator3E94Cb1B485B8B0E_v2_1_1()
            self.json_schema_validators['jsd_398668874439a41d_v2_1_1'] =\
                JSONSchemaValidator398668874439A41D_v2_1_1()
            self.json_schema_validators['jsd_fb9bf80f491a9851_v2_1_1'] =\
                JSONSchemaValidatorFb9BF80F491A9851_v2_1_1()
            self.json_schema_validators['jsd_fa9a98174129af50_v2_1_1'] =\
                JSONSchemaValidatorFa9A98174129Af50_v2_1_1()
        if version == '2.1.2':
            self.json_schema_validators['jsd_eb8c2a8345aa871f_v2_1_2'] =\
                JSONSchemaValidatorEb8C2A8345Aa871F_v2_1_2()
            self.json_schema_validators['jsd_3b9898f04cfbb74b_v2_1_2'] =\
                JSONSchemaValidator3B9898F04CfbB74B_v2_1_2()
            self.json_schema_validators['jsd_f6bfc880435aae2a_v2_1_2'] =\
                JSONSchemaValidatorF6BfC880435AAe2A_v2_1_2()
            self.json_schema_validators['jsd_3b9ef9674429be4c_v2_1_2'] =\
                JSONSchemaValidator3B9EF9674429Be4C_v2_1_2()
            self.json_schema_validators['jsd_4bb22af046fa8f08_v2_1_2'] =\
                JSONSchemaValidator4Bb22Af046Fa8F08_v2_1_2()
            self.json_schema_validators['jsd_aeb9eb67460b92df_v2_1_2'] =\
                JSONSchemaValidatorAeb9Eb67460B92Df_v2_1_2()
            self.json_schema_validators['jsd_b9855ad54ae98156_v2_1_2'] =\
                JSONSchemaValidatorB9855Ad54Ae98156_v2_1_2()
            self.json_schema_validators['jsd_cd98780f4888a66d_v2_1_2'] =\
                JSONSchemaValidatorCd98780F4888A66D_v2_1_2()
            self.json_schema_validators['jsd_eeb168eb41988e07_v2_1_2'] =\
                JSONSchemaValidatorEeb168Eb41988E07_v2_1_2()
            self.json_schema_validators['jsd_50b589fd4c7a930a_v2_1_2'] =\
                JSONSchemaValidator50B589Fd4C7A930A_v2_1_2()
            self.json_schema_validators['jsd_eeb7eb4b4bd8a1dd_v2_1_2'] =\
                JSONSchemaValidatorEeb7Eb4B4Bd8A1Dd_v2_1_2()
            self.json_schema_validators['jsd_08bd88834a68a2e6_v2_1_2'] =\
                JSONSchemaValidator08Bd88834A68A2E6_v2_1_2()
            self.json_schema_validators['jsd_85a2883749099021_v2_1_2'] =\
                JSONSchemaValidator85A2883749099021_v2_1_2()
            self.json_schema_validators['jsd_c085eaf54f89ba34_v2_1_2'] =\
                JSONSchemaValidatorC085Eaf54F89Ba34_v2_1_2()
            self.json_schema_validators['jsd_f1a7a8e74cf99c8f_v2_1_2'] =\
                JSONSchemaValidatorF1A7A8E74Cf99C8F_v2_1_2()
            self.json_schema_validators['jsd_00a2fa6146089317_v2_1_2'] =\
                JSONSchemaValidator00A2Fa6146089317_v2_1_2()
            self.json_schema_validators['jsd_1399891c42a8be64_v2_1_2'] =\
                JSONSchemaValidator1399891C42A8Be64_v2_1_2()
            self.json_schema_validators['jsd_45bc7a8344a8bc1e_v2_1_2'] =\
                JSONSchemaValidator45Bc7A8344A8Bc1E_v2_1_2()
            self.json_schema_validators['jsd_4d86a993469a9da9_v2_1_2'] =\
                JSONSchemaValidator4D86A993469A9Da9_v2_1_2()
            self.json_schema_validators['jsd_10b06a6a4f7bb3cb_v2_1_2'] =\
                JSONSchemaValidator10B06A6A4F7BB3Cb_v2_1_2()
            self.json_schema_validators['jsd_1da5ebdd434aacfe_v2_1_2'] =\
                JSONSchemaValidator1Da5Ebdd434AAcfe_v2_1_2()
            self.json_schema_validators['jsd_17929bc7465bb564_v2_1_2'] =\
                JSONSchemaValidator17929Bc7465BB564_v2_1_2()
            self.json_schema_validators['jsd_47a1b84b4e1b8044_v2_1_2'] =\
                JSONSchemaValidator47A1B84B4E1B8044_v2_1_2()
            self.json_schema_validators['jsd_4d9ca8e2431a8a24_v2_1_2'] =\
                JSONSchemaValidator4D9CA8E2431A8A24_v2_1_2()
            self.json_schema_validators['jsd_55b439dc4239b140_v2_1_2'] =\
                JSONSchemaValidator55B439Dc4239B140_v2_1_2()
            self.json_schema_validators['jsd_6bacb8d14639bdc7_v2_1_2'] =\
                JSONSchemaValidator6BacB8D14639Bdc7_v2_1_2()
            self.json_schema_validators['jsd_709fda3c42b8877a_v2_1_2'] =\
                JSONSchemaValidator709FDa3C42B8877A_v2_1_2()
            self.json_schema_validators['jsd_7aa3da9d4e098ef2_v2_1_2'] =\
                JSONSchemaValidator7Aa3Da9D4E098Ef2_v2_1_2()
            self.json_schema_validators['jsd_89b36b4649999d81_v2_1_2'] =\
                JSONSchemaValidator89B36B4649999D81_v2_1_2()
            self.json_schema_validators['jsd_948ea8194348bc0b_v2_1_2'] =\
                JSONSchemaValidator948EA8194348Bc0B_v2_1_2()
            self.json_schema_validators['jsd_979688084b7ba60d_v2_1_2'] =\
                JSONSchemaValidator979688084B7BA60D_v2_1_2()
            self.json_schema_validators['jsd_9788b8fc4418831d_v2_1_2'] =\
                JSONSchemaValidator9788B8Fc4418831D_v2_1_2()
            self.json_schema_validators['jsd_a5ac99774c6bb541_v2_1_2'] =\
                JSONSchemaValidatorA5Ac99774C6BB541_v2_1_2()
            self.json_schema_validators['jsd_bf859ac64a0ba19c_v2_1_2'] =\
                JSONSchemaValidatorBf859Ac64A0BA19C_v2_1_2()
            self.json_schema_validators['jsd_c5acd9fa4c1a8abc_v2_1_2'] =\
                JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v2_1_2()
            self.json_schema_validators['jsd_b68a6bd8473a9a25_v2_1_2'] =\
                JSONSchemaValidatorB68A6Bd8473A9A25_v2_1_2()
            self.json_schema_validators['jsd_fba0d80747eb82e8_v2_1_2'] =\
                JSONSchemaValidatorFba0D80747Eb82E8_v2_1_2()
            self.json_schema_validators['jsd_d6b8ca774739adf4_v2_1_2'] =\
                JSONSchemaValidatorD6B8Ca774739Adf4_v2_1_2()
            self.json_schema_validators['jsd_a395fae644ca899c_v2_1_2'] =\
                JSONSchemaValidatorA395Fae644Ca899C_v2_1_2()
            self.json_schema_validators['jsd_00aec9b1422ab27e_v2_1_2'] =\
                JSONSchemaValidator00AeC9B1422AB27E_v2_1_2()
            self.json_schema_validators['jsd_6099da82477b858a_v2_1_2'] =\
                JSONSchemaValidator6099Da82477B858A_v2_1_2()
            self.json_schema_validators['jsd_62b05b2c40a9b216_v2_1_2'] =\
                JSONSchemaValidator62B05B2C40A9B216_v2_1_2()
            self.json_schema_validators['jsd_7781fa0548a98342_v2_1_2'] =\
                JSONSchemaValidator7781Fa0548A98342_v2_1_2()
            self.json_schema_validators['jsd_9480fa1f47ca9254_v2_1_2'] =\
                JSONSchemaValidator9480Fa1F47Ca9254_v2_1_2()
            self.json_schema_validators['jsd_f393abe84989bb48_v2_1_2'] =\
                JSONSchemaValidatorF393Abe84989Bb48_v2_1_2()
            self.json_schema_validators['jsd_f6b119ad4d4aaf16_v2_1_2'] =\
                JSONSchemaValidatorF6B119Ad4D4AAf16_v2_1_2()
            self.json_schema_validators['jsd_0b836b7b4b6a9fd5_v2_1_2'] =\
                JSONSchemaValidator0B836B7B4B6A9Fd5_v2_1_2()
            self.json_schema_validators['jsd_1e962af345b8b59f_v2_1_2'] =\
                JSONSchemaValidator1E962Af345B8B59F_v2_1_2()
            self.json_schema_validators['jsd_09b0f9ce4239ae10_v2_1_2'] =\
                JSONSchemaValidator09B0F9Ce4239Ae10_v2_1_2()
            self.json_schema_validators['jsd_21a6db2540298f55_v2_1_2'] =\
                JSONSchemaValidator21A6Db2540298F55_v2_1_2()
            self.json_schema_validators['jsd_3086c9624f498b85_v2_1_2'] =\
                JSONSchemaValidator3086C9624F498B85_v2_1_2()
            self.json_schema_validators['jsd_5889fb844939a13b_v2_1_2'] =\
                JSONSchemaValidator5889Fb844939A13B_v2_1_2()
            self.json_schema_validators['jsd_6f9819e84178870c_v2_1_2'] =\
                JSONSchemaValidator6F9819E84178870C_v2_1_2()
            self.json_schema_validators['jsd_848b5a7b4f9b8c12_v2_1_2'] =\
                JSONSchemaValidator848B5A7B4F9B8C12_v2_1_2()
            self.json_schema_validators['jsd_8da0391947088a5a_v2_1_2'] =\
                JSONSchemaValidator8Da0391947088A5A_v2_1_2()
            self.json_schema_validators['jsd_9e857b5a4a0bbcdb_v2_1_2'] =\
                JSONSchemaValidator9E857B5A4A0BBcdb_v2_1_2()
            self.json_schema_validators['jsd_a4b6c87a4ffb9efa_v2_1_2'] =\
                JSONSchemaValidatorA4B6C87A4Ffb9Efa_v2_1_2()
            self.json_schema_validators['jsd_cf9418234d9ab37e_v2_1_2'] =\
                JSONSchemaValidatorCf9418234D9AB37E_v2_1_2()
            self.json_schema_validators['jsd_f3b26b5544cabab9_v2_1_2'] =\
                JSONSchemaValidatorF3B26B5544CaBab9_v2_1_2()
            self.json_schema_validators['jsd_d8a619974a8a8c48_v2_1_2'] =\
                JSONSchemaValidatorD8A619974A8A8C48_v2_1_2()
            self.json_schema_validators['jsd_8cb6783b4faba1f4_v2_1_2'] =\
                JSONSchemaValidator8Cb6783B4FabA1F4_v2_1_2()
            self.json_schema_validators['jsd_bc8aab4746ca883d_v2_1_2'] =\
                JSONSchemaValidatorBc8AAb4746Ca883D_v2_1_2()
            self.json_schema_validators['jsd_fb9beb664f2aba4c_v2_1_2'] =\
                JSONSchemaValidatorFb9BEb664F2ABa4C_v2_1_2()
            self.json_schema_validators['jsd_4ababa75489ab24b_v2_1_2'] =\
                JSONSchemaValidator4AbaBa75489AB24B_v2_1_2()
            self.json_schema_validators['jsd_3faaa9944b49bc9f_v2_1_2'] =\
                JSONSchemaValidator3FaaA9944B49Bc9F_v2_1_2()
            self.json_schema_validators['jsd_64b9dad0403aaca1_v2_1_2'] =\
                JSONSchemaValidator64B9Dad0403AAca1_v2_1_2()
            self.json_schema_validators['jsd_03b4c8b44919b964_v2_1_2'] =\
                JSONSchemaValidator03B4C8B44919B964_v2_1_2()
            self.json_schema_validators['jsd_5087daae4cc98566_v2_1_2'] =\
                JSONSchemaValidator5087Daae4Cc98566_v2_1_2()
            self.json_schema_validators['jsd_4f947a1c4fc884f6_v2_1_2'] =\
                JSONSchemaValidator4F947A1C4Fc884F6_v2_1_2()
            self.json_schema_validators['jsd_4da91a544e29842d_v2_1_2'] =\
                JSONSchemaValidator4Da91A544E29842D_v2_1_2()
            self.json_schema_validators['jsd_698bfbb44dcb9fca_v2_1_2'] =\
                JSONSchemaValidator698BFbb44Dcb9Fca_v2_1_2()
            self.json_schema_validators['jsd_a39a1a214debb781_v2_1_2'] =\
                JSONSchemaValidatorA39A1A214DebB781_v2_1_2()
            self.json_schema_validators['jsd_be892bd84a78865a_v2_1_2'] =\
                JSONSchemaValidatorBe892Bd84A78865A_v2_1_2()
            self.json_schema_validators['jsd_fbb95b37484a9fce_v2_1_2'] =\
                JSONSchemaValidatorFbb95B37484A9Fce_v2_1_2()
            self.json_schema_validators['jsd_f793192a43dabed9_v2_1_2'] =\
                JSONSchemaValidatorF793192A43DaBed9_v2_1_2()
            self.json_schema_validators['jsd_0fa00adf48698287_v2_1_2'] =\
                JSONSchemaValidator0Fa00Adf48698287_v2_1_2()
            self.json_schema_validators['jsd_66951aaa407ba89c_v2_1_2'] =\
                JSONSchemaValidator66951Aaa407BA89C_v2_1_2()
            self.json_schema_validators['jsd_2f97e8fa45f8b2a3_v2_1_2'] =\
                JSONSchemaValidator2F97E8Fa45F8B2A3_v2_1_2()
            self.json_schema_validators['jsd_6f9cda9a465884b4_v2_1_2'] =\
                JSONSchemaValidator6F9CDa9A465884B4_v2_1_2()
            self.json_schema_validators['jsd_579a6a7248cb94cf_v2_1_2'] =\
                JSONSchemaValidator579A6A7248Cb94Cf_v2_1_2()
            self.json_schema_validators['jsd_4f9f7a7b40f990de_v2_1_2'] =\
                JSONSchemaValidator4F9F7A7B40F990De_v2_1_2()
            self.json_schema_validators['jsd_208579ea4ed98f4f_v2_1_2'] =\
                JSONSchemaValidator208579Ea4Ed98F4F_v2_1_2()
            self.json_schema_validators['jsd_6db9292d4f28a26b_v2_1_2'] =\
                JSONSchemaValidator6Db9292D4F28A26B_v2_1_2()
            self.json_schema_validators['jsd_87a8ba444ce9bc59_v2_1_2'] =\
                JSONSchemaValidator87A8Ba444Ce9Bc59_v2_1_2()
            self.json_schema_validators['jsd_518c59cd441aa9fc_v2_1_2'] =\
                JSONSchemaValidator518C59Cd441AA9Fc_v2_1_2()
            self.json_schema_validators['jsd_9582ab824ce8b29d_v2_1_2'] =\
                JSONSchemaValidator9582Ab824Ce8B29D_v2_1_2()
            self.json_schema_validators['jsd_bca339d844c8a3c0_v2_1_2'] =\
                JSONSchemaValidatorBca339D844C8A3C0_v2_1_2()
            self.json_schema_validators['jsd_8984ea7744d98a54_v2_1_2'] =\
                JSONSchemaValidator8984Ea7744D98A54_v2_1_2()
            self.json_schema_validators['jsd_dd85c91042489a3f_v2_1_2'] =\
                JSONSchemaValidatorDd85C91042489A3F_v2_1_2()
            self.json_schema_validators['jsd_bead7b3443b996a7_v2_1_2'] =\
                JSONSchemaValidatorBead7B3443B996A7_v2_1_2()
            self.json_schema_validators['jsd_c2a43ad24098baa7_v2_1_2'] =\
                JSONSchemaValidatorC2A43Ad24098Baa7_v2_1_2()
            self.json_schema_validators['jsd_d2b4d9d04a4b884c_v2_1_2'] =\
                JSONSchemaValidatorD2B4D9D04A4B884C_v2_1_2()
            self.json_schema_validators['jsd_1eb72ad34e098990_v2_1_2'] =\
                JSONSchemaValidator1Eb72Ad34E098990_v2_1_2()
            self.json_schema_validators['jsd_709769624bf988d5_v2_1_2'] =\
                JSONSchemaValidator709769624Bf988D5_v2_1_2()
            self.json_schema_validators['jsd_8a96fb954d09a349_v2_1_2'] =\
                JSONSchemaValidator8A96Fb954D09A349_v2_1_2()
            self.json_schema_validators['jsd_b78329674878b815_v2_1_2'] =\
                JSONSchemaValidatorB78329674878B815_v2_1_2()
            self.json_schema_validators['jsd_87a5ab044139862d_v2_1_2'] =\
                JSONSchemaValidator87A5Ab044139862D_v2_1_2()
            self.json_schema_validators['jsd_d09b08a3447aa3b9_v2_1_2'] =\
                JSONSchemaValidatorD09B08A3447AA3B9_v2_1_2()
            self.json_schema_validators['jsd_e9b99b2248c88014_v2_1_2'] =\
                JSONSchemaValidatorE9B99B2248C88014_v2_1_2()
            self.json_schema_validators['jsd_cfbd3870405aad55_v2_1_2'] =\
                JSONSchemaValidatorCfbd3870405AAd55_v2_1_2()
            self.json_schema_validators['jsd_398668874439a41d_v2_1_2'] =\
                JSONSchemaValidator398668874439A41D_v2_1_2()
            self.json_schema_validators['jsd_3e94cb1b485b8b0e_v2_1_2'] =\
                JSONSchemaValidator3E94Cb1B485B8B0E_v2_1_2()
            self.json_schema_validators['jsd_fb9bf80f491a9851_v2_1_2'] =\
                JSONSchemaValidatorFb9BF80F491A9851_v2_1_2()
            self.json_schema_validators['jsd_fa9a98174129af50_v2_1_2'] =\
                JSONSchemaValidatorFa9A98174129Af50_v2_1_2()

    def json_schema_validate(self, model):
        """Factory function for creating JSONSchemaValidator objects.

        Args:
            model(basestring).

        Returns:
            JSONSchemaValidator: The created JSONSchemaValidator object.

        Raises:
            MalformedRequest.
        """
        return self.json_schema_validators.get(model, JSONSchemaValidator())
