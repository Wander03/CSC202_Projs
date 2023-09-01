# Start of unittest - add to completely test functions in exp_eval!

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):

    def test_postfix_eval_01a(self) -> None:
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_01b(self) -> None:
        self.assertAlmostEqual(postfix_eval("8 1 >>"), 4)
        self.assertAlmostEqual(postfix_eval("8 1 <<"), 16)

    def test_postfix_eval_01c(self) -> None:
        self.assertAlmostEqual(postfix_eval("8 2 **"), 64)

    def test_postfix_eval_01d(self) -> None:
        self.assertAlmostEqual(postfix_eval("18.5 -2 *"), -37)
        self.assertAlmostEqual(postfix_eval("-18.52 -0.78 +"), -19.3)

    def test_postfix_eval_01e(self) -> None:
        self.assertAlmostEqual(postfix_eval("6 4 3 + 2 - * 6 /"), 5)
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)

    def test_postfix_eval_01f(self) -> None:
        self.assertAlmostEqual(postfix_eval("-5.0"), -5.0)

    def test_postfix_eval_01g(self) -> None:
        self.assertAlmostEqual(postfix_eval("-5.0 1 *"), -5.0)
        self.assertAlmostEqual(postfix_eval("5 0 *"), 0)

    def test_postfix_eval_02a(self) -> None:
        try:
            postfix_eval("blah")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_02b(self) -> None:
        try:
            postfix_eval("7 3 + 4 b /")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_02c(self) -> None:
        try:
            postfix_eval("7 3 + 4 4 / r")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_02d(self) -> None:
        try:
            postfix_eval("7 7 . +")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03a(self) -> None:
        try:
            postfix_eval("4 +")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03b(self) -> None:
        try:
            postfix_eval("")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03c(self) -> None:
        try:
            postfix_eval("+")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03d(self) -> None:
        try:
            postfix_eval(" ")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03e(self) -> None:
        try:
            postfix_eval("1 2 3 << << << <<")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03f(self) -> None:
        try:
            postfix_eval("1 9 / / 0 /")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03g(self) -> None:
        try:
            postfix_eval("-")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03h(self) -> None:
        try:
            postfix_eval("*")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03i(self) -> None:
        try:
            postfix_eval("**")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03j(self) -> None:
        try:
            postfix_eval("<<")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03k(self) -> None:
        try:
            postfix_eval(">>")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04a(self) -> None:
        try:
            postfix_eval("1 2 3 +")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_04b(self) -> None:
        try:
            postfix_eval("0 0 0 0 0")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self) -> None:
        with self.assertRaises(ValueError):
            postfix_eval("1 0 /")

    def test_postfix_eval_06a(self) -> None:
        try:
            postfix_eval("8.0 1 <<")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_06b(self) -> None:
        try:
            postfix_eval("8 1.0 >>")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_06c(self) -> None:
        try:
            postfix_eval("8.0 1.0 >>")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_infix_to_postfix_01a(self) -> None:
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("32 >> 2 >> 1"), "32 2 >> 1 >>")

    def test_infix_to_postfix_01b(self) -> None:
        self.assertEqual(infix_to_postfix("32 >> 2 << 1"), "32 2 >> 1 <<")

    def test_infix_to_postfix_01c(self) -> None:
        self.assertEqual(infix_to_postfix("3 ** 2 ** 2"), "3 2 2 ** **")

    def test_infix_to_postfix_02(self) -> None:
        self.assertEqual(infix_to_postfix("( 5 - 3 ) * 4"), "5 3 - 4 *")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

    def test_infix_to_postfix_03(self) -> None:
        self.assertEqual(infix_to_postfix("70 - -3 * 10"), "70 -3 10 * -")

    def test_infix_to_postfix_04(self) -> None:
        self.assertEqual(infix_to_postfix("70.52 - 3.5 * 10.05"), "70.52 3.5 10.05 * -")

    def test_infix_to_postfix_05(self) -> None:
        self.assertEqual(infix_to_postfix("-70.52 - 3.5 * 10.05"), "-70.52 3.5 10.05 * -")

    def test_infix_to_postfix_06(self) -> None:
        self.assertEqual(infix_to_postfix("5 * ( 6 + 3 - 7 * 3 + 2 ) / 6"), "5 6 3 + 7 3 * - 2 + * 6 /")

    def test_infix_to_postfix_07(self) -> None:
        self.assertEqual(infix_to_postfix("5 * 0"), "5 0 *")

    def test_infix_to_postfix_08(self) -> None:
        self.assertEqual(infix_to_postfix("( 6 / 7 + 3 * 4 ) / ( 5 - 2 ) + 3"), "6 7 / 3 4 * + 5 2 - / 3 +")
        self.assertEqual(infix_to_postfix("( 6 / 7 + 3 ** 4 ) / ( 5 - 2 ) + 3"), "6 7 / 3 4 ** + 5 2 - / 3 +")

    def test_infix_to_postfix_09(self) -> None:
        self.assertEqual(infix_to_postfix("1 + 2 * ( 3 + 4 )"), "1 2 3 4 + * +")
        self.assertEqual(infix_to_postfix("( 1 + 2 * 3 + 4 )"), "1 2 3 * + 4 +")

    def test_infix_to_postfix_10(self) -> None:
        self.assertEqual(infix_to_postfix("( 4 )"), "4")

    def test_check_precedence(self) -> None:
        self.assertTrue(check_precedence("+", "-"))
        self.assertFalse(check_precedence("*", "-"))
        self.assertTrue(check_precedence("+", "*"))
        self.assertFalse(check_precedence("**", "-"))
        self.assertTrue(check_precedence("**", "<<"))
        self.assertTrue(check_precedence("/", "*"))
        self.assertFalse(check_precedence("**", "**"))

    def test_prefix_to_postfix(self) -> None:
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("- + 9 7 0"), "9 7 + 0 -")
        self.assertEqual(prefix_to_postfix("* + 6 8 - 3 5"), "6 8 + 3 5 - *")
        self.assertEqual(prefix_to_postfix("- 1 / 2 * 3 ** 4 5"), "1 2 3 4 5 ** * / -")
        self.assertEqual(prefix_to_postfix("<< 3 9"), "3 9 <<")

if __name__ == "__main__":
    unittest.main()
