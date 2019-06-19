from asynctest import skip

from maas.app import app, division
from tests.base import BaseApiTestCase


class OperationTest(BaseApiTestCase):
    async def setUp(self):
        self.client = await self.aiohttp_client(app)

    async def tearDown(self):
        await super(OperationTest, self).tearDown()

    async def test_operation_endpoint(self):
        result = await self.client.post("/", json={"left": 20, "right": 5})
        self.assertEqual(200, result.status)
        data = await result.json()
        self.assertEqual({"result": 4}, data)

    async def test_operatio_devision_division_by_zero(self):
        result = await self.client.post("/", json={"left": 20, "right": 0})
        self.assertEqual(200, result.status)
        data = await result.json()
        self.assertEqual({"result": "Division by zero"}, data)

