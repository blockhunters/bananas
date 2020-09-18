from test.conftest import validate

from bananas.ast import Argv, AssertReturn, Declare, Integer32Const, Invoke, Pointer

declare = """(declare "ptr" (i32.const 16843009) (i32.const 16843009) (i32.const 42))
(assert_return (invoke "foo" (i32.pointer "ptr") (i32.const 2)) (i32.const 1))"""
declare_ast = [
    Declare(
        "ptr",
        (Integer32Const("16843009"), Integer32Const("16843009"), Integer32Const("42")),
    ),
    AssertReturn(
        Invoke("foo", (Pointer("ptr"), Integer32Const("2"))), Integer32Const("1")
    ),
]


def test_declare():
    validate(declare, declare_ast)


argv = r"""(argv "test" "dojpa" "he\"t\`m")
(assert_return (invoke "f" (i32.const 1)) (i32.const 1))"""
argv_ast = [
    Argv(
        (
            "test",
            "dojpa",
            r"he\"t\`m",
        )
    ),
    AssertReturn(Invoke("f", (Integer32Const("1"),)), Integer32Const("1")),
]


def test_argv():
    validate(argv, argv_ast)
