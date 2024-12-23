from src.day_23 import solve_first
from src.day_23 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("day_23_example.txt") == 7


def test_solve_first() -> None:
    assert solve_first("day_23.txt") == 1046


def test_solve_second_example() -> None:
    assert solve_second("day_23_example.txt") == "co,de,ka,ta"


def test_solve_second() -> None:
    assert solve_second("day_23.txt") == "de,id,ke,ls,po,sn,tf,tl,tm,uj,un,xw,yz"
