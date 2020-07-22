import time

from livecover import get_coverage

from test.test_module.test_file_2 import function_1


def identity(ob):
    return ob


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


@identity
def test_function_1():
    if True:
        x = 3
    y = 2
    pass


def run_functions(runs):
    for i in range(runs):
        test_function_1()
        x = TestClass2()
        x.class_function_2()
        function_1()
    ran_for = time.time() - start


if __name__ == "__main__":
    start = time.time()
    RUNS = 10000
    cover = get_coverage(ratio=1)
    run_functions(RUNS)
    ran_for = time.time() - start
    print(ran_for / RUNS)
