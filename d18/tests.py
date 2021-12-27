
import unittest
from d18.ac import  part1, part2, explode_sn, split_sn
from utils import parse_input

DAY = 18

class AOCTests(unittest.TestCase):

    def test_exploding_pairs(self):
        # Given
        e1 = [[[[[9,8],1],2],3],4]
        e2 = [7,[6,[5,[4,[3,2]]]]]
        e3 = [[6,[5,[4,[3,2]]]],1]
        e4 = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
        e5 = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
        e6 = [[3,[2,[8,0]]],[9,[5,[4,[8,2]]]]]
        e7 = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
        # When
        r1 = explode_sn(e1)
        r2 = explode_sn(e2)
        r3 = explode_sn(e3)
        r4 = explode_sn(e4)
        r5 = explode_sn(e5)
        r6 = explode_sn(e6)
        r7 = explode_sn(e7)
        r8 = explode_sn(r7)
        # Then
        self.assertEqual(r1, [[[[0,9],2],3],4])
        self.assertEqual(r2, [7,[6,[5,[7,0]]]])
        self.assertEqual(r3, [[6,[5,[7,0]]],3])
        self.assertEqual(r4, [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
        self.assertEqual(r5, [[3,[2,[8,0]]],[9,[5,[7,0]]]])
        self.assertEqual(r6, [[3,[2,[8,0]]],[9,[5,[12,0]]]])
        self.assertEqual(r7, [[[[0,7],4],[7,[[8,4],9]]],[1,1]])
        self.assertEqual(r8, [[[[0,7],4],[15,[0,13]]],[1,1]])

    def test_split(self):
        # given
        s1 = [[[[0,7],4],[15,[0,13]]],[1,1]]
        # when
        r1 = split_sn(s1)
        r2 = split_sn(r1)
        # then
        self.assertEqual(r1, [[[[0,7],4],[[7,8],[0,13]]],[1,1]])
        self.assertEqual(r2, [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])
    

    # def test_part1(self):
    #     # Given
    #     input = parse_input(f'd{DAY}/data/test_input.txt')
    #     expected_sol = parse_input(f'd{DAY}/data/test_sol_1.txt', to_int=True, single_value=True)
    #     # When
    #     result = part1(input)
    #     # Then
    #     self.assertEqual(expected_sol, result)

    # def test_part2(self):
    #     # Given
    #     input = parse_input(f'd{DAY}/data/test_input.txt')
    #     expected_sol = parse_input(f'd{DAY}/data/test_sol_2.txt', to_int=True, single_value=True)
    #     # When
    #     result = part2(input)
    #     # Then
    #     self.assertEqual(expected_sol, result)


if __name__ == '__main__':
    unittest.main()
