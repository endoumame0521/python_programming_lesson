import logging

logger = logging.getLogger(__name__)

logger.error('Api call is failed')

# このようにkey, value(dict型)で記述していれば、後のログ解析ソフトに掛ける際に、解析しやすい。
logger.error({
    'action': 'create',
    'status': 'fail',
    'message': 'Api call is failed',
})
