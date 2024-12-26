from src.day_24 import solve_first
from src.day_24 import solve_second


def test_solve_first_example_1() -> None:
    assert solve_first("day_24_example_1.txt") == 4


def test_solve_first_example_2() -> None:
    assert solve_first("day_24_example_2.txt") == 2024


def test_solve_first() -> None:
    assert solve_first("day_24.txt") == 65635066541798


def test_solve_second() -> None:
    result = solve_second("day_24.txt")
    assert len(solve_second("day_24.txt").split(",")) == 8
    assert result != "z04,z13,z13,z13,z13,z14,z41,z44"
    assert result != "z14,z18,z26,z32,z32,z32,z32,z40"
    assert result != "z01,z02,z03,z04,z05,z06,z07,z29"
    assert result != "dgr,dtv,fgc,gdv,hfp,jkb,mtj,njb"
    assert result != "dgr,dtv,fgc,gdv,jkb,z12,z29,z37"
    assert result == "dgr,dtv,fgc,mtj,vvm,z12,z29,z37"
