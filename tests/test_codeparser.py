from cfunctree.codeparser import parse_code


def test_parse_code():
    code = r"""

double foo(int a, void* b);
void baz(int t);

int boo(int a, double b, int c, ...) {
    a = b;
    b = c;
    c = a;
    return c;
}

double foo(int a, void* b);

const int data_2 = 100;

double foo(int a, void* b) {
    baz(a);
    return a / 2.0;
}

int main(void) {
    foo(2, (void*)0);
    baz(boo(data_2, foo(3, (void*)120), -1));
    return 0;
}
"""

    data = parse_code(code)

    print(data.get_func_list())
    for func in data.get_func_list():
        print(func, "->", data.get_dep_list(func))

