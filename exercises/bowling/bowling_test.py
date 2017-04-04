import unittest
import bowling


def int_game():
    game = bowling.Bowl()
    return game


def loop_scores(game, scores):
    for pin in scores:
        result = game.roll(pin)
        if result is not None:
            break
    return game


class Bowling(unittest.TestCase):
    def test_1(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 0)

    def test_2(self):
        scores = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 90)

    def test_3(self):
        scores = [6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 10)

    def test_4(self):
        scores = [6, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 16)

    def test_5(self):
        scores = [5, 5, 3, 7, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 31)

    def test_6(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 7, 3, 7]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 17)

    def test_7(self):
        scores = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 10)

    def test_8(self):
        scores = [10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 26)

    def test_9(self):
        scores = [10, 10, 10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 81)

    def test_10(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 10, 7, 1]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 18)

    def test_11(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 10, 7, 3]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 20)

    def test_12(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 10, 10, 10]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 30)

    def test_13(self):
        scores = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 300)

    def test_14(self):
        game = int_game()
        self.assertEqual(game.roll(-1), "error: Negative roll is invalid")

    def test_15(self):
        game = int_game()
        self.assertEqual(game.roll(11),
                         "error: Pin count exceeds pins on the lane")

    def test_16(self):
        scores = [5]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.roll(6),
                         "error: Pin count exceeds pins on the lane")

    def test_17(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.roll(11),
                         "error: Pin count exceeds pins on the lane")

    def test_18(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 5]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.roll(6),
                         "error: Pin count exceeds pins on the lane")

    def test_19(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 10, 10, 6]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(), 26)

    def test_20(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 6]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.roll(10),
                         "error: Pin count exceeds pins on the lane")

    def test_21(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.roll(11),
                         "error: Pin count exceeds pins on the lane")

    def test_22(self):
        scores = []
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(),
                         "error: Score cannot be taken until"
                         "the end of the game")

    def test_23(self):
        scores = [0, 0]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(),
                         "error: Score cannot be taken until"
                         "the end of the game")

    def test_24(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.roll(0),
                         "error: Cannot roll after game is over")

    def test_25(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(),
                         "error: Score cannot be taken until"
                         "the end of the game")

    def test_26(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(),
                         "error: Score cannot be taken until"
                         "the end of the game")

    def test_27(self):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3]
        game = loop_scores(int_game(), scores)
        self.assertEqual(game.score(),
                         "error: Score cannot be taken until"
                         "the end of the game")


if __name__ == '__main__':
    unittest.main()
