import random
from uuid import UUID

from app.common.enums import SampleCarEnum
from app.common.helpers import get_random_string
from app.common.models import SampleResponse


class SampleLogicHandler:

    def handle_request(self, account: UUID) -> SampleResponse:
        response = SampleResponse(
            random_words = [get_random_string() for i in range(10)],
            number = random.randint(1,1000),
            carbrand = random.choice([SampleCarEnum.Mercedes,SampleCarEnum.BMW]),
            account = account
        )
        return response

