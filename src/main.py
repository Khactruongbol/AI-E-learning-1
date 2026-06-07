from __future__ import annotations
from pathlib import Path
import logging
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import einstein_csp

TRACE_LOG = ROOT / "trace.log"
logging.basicConfig(
    filename=str(TRACE_LOG),
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    filemode="w",
)
logger = logging.getLogger(__name__)

def main() -> None:
    print("Einstein's Zebra Puzzle - AC-3 + Backtracking\n")
    logger.info("Bắt đầu chạy chương trình")

    problem = einstein_csp.build_problem()
    logger.debug("Xây dựng CSP hoàn tất")

    print("1) Áp dụng AC-3 để lọc domain ban đầu...")
    logger.info("Áp dụng AC-3 để lọc domain ban đầu")

    ac3_ok = einstein_csp.ac3(problem)
    logger.debug("AC-3 trả về: %s", ac3_ok)

    if not ac3_ok:
        print("AC-3 phát hiện không còn domain hợp lệ. Không có nghiệm.")
        logger.error("AC-3 phát hiện domain trống, không có nghiệm")
        raise SystemExit(1)

    print("AC-3 hoàn tất. Các domain đã được thu hẹp:\n")
    logger.info("AC-3 hoàn tất và domains đã được thu hẹp")
    logger.debug("Domains sau AC-3: %s", {variable: sorted(problem.domains[variable]) for variable in sorted(problem.variables)})

    for variable in sorted(problem.variables):
        domain = sorted(problem.domains[variable])
        print(f"  {variable:12}: {domain}")

    print("\n2) Chạy Backtracking trên CSP đã được lọc:\n")
    logger.info("Bắt đầu backtracking trên CSP đã lọc")

    solution = einstein_csp.backtrack({}, problem)
    logger.debug("Kết quả backtracking: %s", solution)

    if solution is None:
        print("Không tìm thấy nghiệm hợp lệ sau khi Backtracking.")
        logger.error("Backtracking không tìm được nghiệm")
        raise SystemExit(1)

    formatted = einstein_csp.format_solution(solution)
    print(formatted)
    logger.info("Giải pháp tìm được và in ra console")

    zebra_owner = einstein_csp.owner_of('Zebra', solution)
    water_drinker = einstein_csp.owner_of('Water', solution)
    print("\nKết quả trả lời: ")
    print(f"  Ai nuôi ngựa vằn? {zebra_owner}")
    print(f"  Ai uống nước? {water_drinker}")
    logger.info("Ai nuôi ngựa vằn: %s", zebra_owner)
    logger.info("Ai uống nước: %s", water_drinker)


if __name__ == "__main__":
    main()
