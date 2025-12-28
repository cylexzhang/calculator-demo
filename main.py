from __future__ import annotations

import argparse
import sys
from calculator import add, sub, mul, div, CalculatorError


OPS = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Simple CLI calculator")
    parser.add_argument("op", choices=OPS.keys(), help="Operation")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()

    try:
        result = OPS[args.op](args.a, args.b)
        # 输出更友好一点
        print(f"你的输入是 {args.a} {args.op} {args.b},结果是：{result}")
        return 0
    except CalculatorError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
