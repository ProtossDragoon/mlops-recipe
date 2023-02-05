# 서드파티
import unittest

# 프로젝트
import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_index(self):
        res = self.app.get("/")
        expected = 200
        self.assertEqual(expected, res.status_code)
        expected = "텐서플로 자동차 연비 예측 플라스크 서비스 컨테이너"
        self.assertIn(expected, res.get_data(as_text=True))

    def test_hello(self):
        res = self.app.get("/hello")
        expected = 200
        self.assertEqual(expected, res.status_code)
        expected = "hello ml"
        self.assertIn(expected, res.get_data(as_text=True))

    def test_predict(self):
        res = self.app.post(
            "/predict",
            json={
                "Cylinders": 8,
                "Displacement": 307.0,
                "Horsepower": 130,
                "Weight": 3504,
                "Acceleration": 12,
                "ModelYear": 70,
                "Country": "USA",
            },
        )
        expected = 200
        self.assertEqual(expected, res.status_code)
        self.assertIn("MPG", res.get_json())
        self.assertEqual(1, len(res.get_json()["MPG"]))
        expected_m, expected_M = 0, 100
        self.assertLessEqual(res.get_json()["MPG"][0], expected_M)
        self.assertGreaterEqual(res.get_json()["MPG"][0], expected_m)


if __name__ == "__main__":
    unittest.main()
