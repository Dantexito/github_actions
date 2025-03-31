import rutpy


def validate(rut: str) -> bool:
    return rutpy.validate(rut)


if __name__ == '__main__':
    rut = "12345678-9"
    print(validate(rut))
