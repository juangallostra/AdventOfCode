
import unittest
from d18.ac import  add_nums, check_magnitude, explode_sn, split_sn, part1, part2
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
    
    def test_addition(self):
        # given
        num1 = [[[[4,3],4],4],[7,[[8,4],9]]]
        num2 = [1,1]
        num3 = [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
        num4 = [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
        num5 = [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
        num6 = [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
        num7 = [7,[5,[[3,8],[1,4]]]]
        num8 = [[2,[2,2]],[8,[8,1]]]
        num9 = [2,9]
        num10 = [1,[[[9,3],9],[[9,0],[0,7]]]]
        num11 = [[[5,[7,4]],7],1]
        num12 = [[[[4,2],2],6],[8,7]]
        # when
        r = add_nums(num1, num2)
        r2 = add_nums(num3, num4)
        r3 = add_nums(r2, num5)
        r4 = add_nums(r3, num6)
        r5 = add_nums(r4, num7)
        r6 = add_nums(r5, num8)
        r7 = add_nums(r6, num9)
        r8 = add_nums(r7, num10)
        r9 = add_nums(r8, num11)
        r10 = add_nums(r9, num12)
        # then
        self.assertEqual(r, [[[[0,7],4],[[7,8],[6,0]]],[8,1]])
        self.assertEqual(r2, [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]])
        self.assertEqual(r3, [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]])
        self.assertEqual(r10, [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])

    def test_magnitude(self):
        # given
        
        n1 = [[1,2],[[3,4],5]]
        n2 = [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
        n3 = [[[[1,1],[2,2]],[3,3]],[4,4]]
        n4 = [[[[3,0],[5,3]],[4,4]],[5,5]]
        n5 = [[[[5,0],[7,4]],[5,5]],[6,6]]
        n6 = [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
        # when
        r1 = check_magnitude(n1)
        r2 = check_magnitude(n2)
        r3 = check_magnitude(n3)
        r4 = check_magnitude(n4)
        r5 = check_magnitude(n5)
        r6 = check_magnitude(n6)
        # Then
        self.assertEqual(r1, 143)
        self.assertEqual(r2, 1384)
        self.assertEqual(r3, 445)
        self.assertEqual(r4, 791)
        self.assertEqual(r5, 1137)
        self.assertEqual(r6, 3488)


    def test_part1(self):
        # Given
        input = parse_input(f'd{DAY}/data/test_input.txt')
        expected_sol = parse_input(f'd{DAY}/data/test_sol_1.txt', to_int=True, single_value=True)
        # When
        result = part1(input)
        # Then
        self.assertEqual(expected_sol, result)

    def test_part2(self):
        # Given
        input = parse_input(f'd{DAY}/data/test_input.txt')
        expected_sol = parse_input(f'd{DAY}/data/test_sol_2.txt', to_int=True, single_value=True)
        # When
        result = part2(input)
        # Then
        self.assertEqual(expected_sol, result)


if __name__ == '__main__':
    unittest.main()
