from livecover import get_coverage

from test.test_module.test_file_2 import function_1


class TestClass1:
    def class_function_1(self):
        pass

    def class_function_2(self):
        def nested_class_function_1(self):
            pass

        def nested_class_function_2(self):
            pass


class TestClass2:
    def class_function_1(self):
        pass

    def class_function_2(self):
        def nested_class_function_1():
            function_1()

        def nested_class_function_2():
            nested_class_function_1()

        nested_class_function_2()

    def class_function_3(self):
        pass


class TestClass3:
    pass


def test_function_1():
    pass


def run_functions():
    test_function_1()
    x = TestClass1()
    x.class_function_1()
    x.class_function_2()
    function_1()


if __name__ == "__main__":
    cover = get_coverage(ratio=1)
    run_functions()
    cover.finish()
